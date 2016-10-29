import logging

from parsers.parse import Parse


class Config:
    #####################################
    # logger settings
    LOG_FORMAT = u'%(levelname)-8s [%(asctime)s] %(message)s'
    LOG_LEVEL = logging.INFO

    #####################################
    # comm module                       #
    COMM_ID = 000                       # comm_id for parse
    START_PAGE = 1                      # [warning] last page excluded: [start, end) or [end, start)!
    END_PAGE = 100                      # same as above

    #####################################
    # forum module
    FORUM_ID = 1                        # forum id for parse themes
    FORUM_MOVE_TO = 2                   # move destination forum

    # blogs module
    BLOG_ACCESS_SEARCH = Parse.BlogAccessMode.PASSWORD
    BLOG_ACCESS_SEARCH_INVERT = True    # false: search only BLOG_ACCESS_SEARCH, otherwise !BLOG_ACCESS_SEARCH
    BLOG_ACCESS_SET_TO = Parse.BlogAccessMode.ONLY_ME

    #####################################
    # search module                     #
    SEARCH_LOGIN = "user"               # nickname for search
    SEARCH_LEVEL = 10                   #
    INSERT_USERS = ['u1', 'u2']         # list or nicknames of users for manually inserting

    STAT_IP_WEIGHT = 1000               # rating value if ip1 == ip2
    STAT_IP_PLACE_WEIGHT = 0.001        # rating value

    SEARCH_DEC = False                  # decrease rating if ua1 != ua2
    SEARCH_DEC_DIV = 100                # if yes -> value for divide original rating

    # search > recount                  #
    STAT_LOG = True                     # enable log scale
    STAT_LOG_BASE = 3                   # log base for rating scale

    #####################################
    # common settings                   #
    DB_HOST = "127.0.0.1"
    DB_PORT = 27017
    DB_NAME = "spaces_users"

    TABLE_NAME_USERS = "users"
    TABLE_NAME_UA_FREQ_STATS = "stats"

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:2.0b7) Gecko/20100101 Firefox/4.0b7',
    }

    #####################################
    # secret settings                   #
    USER_NAME = "user"
    USER_PASSWORD = "password"