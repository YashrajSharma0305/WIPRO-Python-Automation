import configparser
import os

class ConfigReader:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_path = os.path.join(base_dir, "config", "config.ini")
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    def get_base_url(self):
        return self.config.get("application", "base_url")

    def get_browser_name(self):
        return self.config.get("browser", "browser_name")

    def get_headless_mode(self):
        return self.config.getboolean("browser", "headless")

    def get_implicit_wait(self):
        return self.config.getint("timeouts", "implicit_wait")

    def get_explicit_wait(self):
        return self.config.getint("timeouts", "explicit_wait")