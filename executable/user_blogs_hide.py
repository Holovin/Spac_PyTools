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

    # comm_remove_users
    logging.info("Init ok... Start parsing... [user = " + str(Config.USER_NAME) + "]")

    # reverse for correct removing
    for i in range(Config.START_PAGE, Config.END_PAGE):
        logging.info("Current page: " + str(i) + "...")

        if not n.get_user_blogs_page(Config.USER_NAME, i):
            logging.fatal("Get user blogs page error")
            exit()

        blogs = p.xpath_user_blog_page(n.get_data(), Config.BLOG_ACCESS_SEARCH, Config.BLOG_ACCESS_SEARCH_INVERT)

        logging.info("Parsed " + str(len(blogs)) + " objects...")

        for blog in blogs:
            if not n.post_user_blogs_access_change(blog, Config.BLOG_ACCESS_SET_TO.value['int']):
                logging.fatal("Error changing access: " + blog)
                exit()

            logging.info("Blog " + blog + " processed")

    logging.info("--- APP END ---")
    return

if __name__ == "__main__":
    main()
