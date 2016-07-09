#!/usr/bin/python

import logging
from time import sleep

from config import Config
from helpers.message import Msg
from network import Network
from parsers.parse import Parse
from parsers.spac_date import SpacDate


def main():
    # core
    logging.basicConfig(format=Config.LOG_FORMAT, level=Config.LOG_LEVEL)

    sd = SpacDate()
    p = Parse(sd)
    n = Network()

    # protection
    sec = 0
    logging.info("Starting in " + str(sec) + " seconds...")
    sleep(sec)

    # auth
    if not n.auth(Config.USER_NAME, Config.USER_PASSWORD):
        logging.fatal("Auth error...")
        exit()

    # comm_remove_users
    ck = n.get_session_ck()

    logging.info("Init ok... Start parsing... [id = " + str(Config.COMM_ID) + "]")

    # reverse for correct removing
    for i in range(Config.END_PAGE, Config.START_PAGE, -1):
        logging.info("Current page: " + str(i) + "...")

        if not n.get_comm_users_page(Config.COMM_ID, i):
            logging.fatal("Get user page error")
            exit()

        users = p.xpath_comm_users_page_delete(n.get_data())
        logging.info("Parsed users: " + str(len(users)) + " objects...")

        for user in users:
            if n.do_get(user) is not Msg.success_ok:
                logging.fatal("Cant remove user [url = " + user + "]")
                exit()

            logging.info("User removed, id: " + p.text_url_param_delete(user))

    logging.info("--- APP END ---")
    return

if __name__ == "__main__":
    main()
