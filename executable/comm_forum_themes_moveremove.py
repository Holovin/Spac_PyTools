#!/usr/bin/python

import logging

from config import Config
from network import Network
from parsers.parse import Parse
from parsers.spac_date import SpacDate


def main():
    # core
    logging.basicConfig(format=Config.LOG_FORMAT, level=Config.LOG_LEVEL)

    sd = SpacDate()
    p = Parse(sd)
    n = Network()

    # auth
    if not n.auth(Config.USER_NAME, Config.USER_PASSWORD):
        logging.fatal("Auth error...")
        exit()

    # comm_forum_themes_moveremove.py
    logging.info("Init ok... Start parsing... [id = " + str(Config.COMM_ID) + "]")

    # reverse for correct removing
    for i in range(Config.END_PAGE, Config.START_PAGE, -1):
        logging.info("Current page: " + str(i) + "...")

        if not n.get_comm_forum_page(Config.FORUM_ID, i):
            logging.fatal("Get comm forum page error")
            exit()

        themes_id = p.xpath_comm_forum_themes_id(n.get_data(), Parse.ForumThemesMode.ALL)
        logging.info("Parsed themes: " + str(len(themes_id)) + " objects...")

        for theme_id in themes_id:
            if not n.get_comm_forum_theme_remove(theme_id):
                logging.error("Error at theme: " + str(theme_id))

            logging.info("Theme processed: " + str(theme_id))

    logging.info("--- APP END ---")
    return

if __name__ == "__main__":
    main()
