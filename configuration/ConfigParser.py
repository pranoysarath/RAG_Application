import configparser


class ConfigParser:

    config = configparser.ConfigParser()
    config.read('/Users/pranoysarath/PycharmProjects/wrangling/RAG/configuration/config.ini')

    # handle other cases
    @staticmethod
    def get_key_value(key):
        return ConfigParser.config['keys'][key]
