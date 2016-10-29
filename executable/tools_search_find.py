#!/usr/bin/python

import logging
import operator

from config import Config
from storage.database import Database


def main():
    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.INFO)

    db = Database()

    face = db.find_face(Config.SEARCH_LOGIN, Config.SEARCH_LEVEL)
    if face is False or Config.SEARCH_LOGIN == "":
        logging.fatal("Empty result =/")
        exit()

    logging.info(" ")
    logging.info("Result for " + Config.SEARCH_LOGIN + " (with min level " + str(Config.SEARCH_LEVEL) + "):")
    face = sorted(face.items(), key=operator.itemgetter(1), reverse=True)

    for item in face:
        if item[1] < Config.SEARCH_LEVEL:
            break

        logging.info("> " + item[0] + " :: " + str(item[1]))

    logging.info("--- APP END ---")
    return


if __name__ == "__main__":
    main()
