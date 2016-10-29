#!/usr/bin/python

import logging

from config import Config
from network import Network
from models.user import User
from parsers.json_api import JsonApi
from parsers.parse import Parse
from parsers.spac_date import SpacDate
from storage.database import Database


def main():
    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO)

    sd = SpacDate()
    p = Parse(sd)
    d = Network()
    db = Database()

    if not d.auth(Config.USER_NAME, Config.USER_PASSWORD):
        logging.fatal("Auth error...")
        exit()

    logging.info("Init ok... Start parsing... [id = " + str(Config.COMM_ID) + "]")

    for i in range(Config.START_PAGE, Config.END_PAGE):
        logging.info("Trying parse page: " + str(i) + "...")

        if not d.get_comm_users_page(Config.COMM_ID, i):
            logging.fatal("Get user page error")
            exit()

        users = p.xpath_comm_users_page(d.get_data())
        logging.info("Parsed users: " + str(users))

        for user in users:
            if not d.get_user_id(user):
                logging.error("Get user id error (user = " + user + "). Skipping...")
                continue

            u_id = JsonApi.json_extract_user_id(user, d.get_data_json())

            if u_id is False:
                logging.warning("User " + user + " not found")
                continue

            if not d.get_user_hist(user):
                logging.error("Get user hist error (user = " + user + "). Skipping...")
                continue

            u_hist = p.xpath_user_history(d.get_data())

            if not d.get_user_sess(user):
                logging.error("Get user sess error (user = " + user + "). Skipping...")
                continue

            u_sess = p.xpath_user_sessions(d.get_data())

            db_user = User(u_id, user, u_hist, u_sess)
            db.upsert_user(db_user)
            logging.info("User: " + user + ", id: " + str(u_id) + "...")

    logging.info("--- APP END ---")
    return

if __name__ == "__main__":
    main()
