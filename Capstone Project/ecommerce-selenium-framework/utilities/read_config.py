import configparser
import os

config = configparser.RawConfigParser()
config_file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.ini")
config.read(config_file_path)

class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('application', 'base_url')

    @staticmethod
    def get_browser_name():
        return config.get('browser', 'browser_name')

    @staticmethod
    def get_implicit_wait():
        return int(config.get('timeouts', 'implicit_wait'))

    @staticmethod
    def get_explicit_wait():
        return int(config.get('timeouts', 'explicit_wait'))

    @staticmethod
    def get_valid_email():
        return config.get('credentials', 'valid_email')

    @staticmethod
    def get_valid_password():
        return config.get('credentials', 'valid_password')
