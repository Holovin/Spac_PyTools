import logging


class JsonApi:
    @staticmethod
    def json_extract_user_id(login, json):
        return next((item for item in json['users'] if item['name'] == login), -1)['nid']

    @staticmethod
    def json_check_success(json, method='login'):
        if json['code'] == '00000' and method == 'login':
            logging.info("Login ok: [name = " + json['attributes']['name'] + "; id = " + str(json['attributes']['nid']) + "]")
            return True

        logging.fatal("Json parse error (code: " + json['code'] + ")")
        return False
