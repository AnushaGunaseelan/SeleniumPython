import configparser
from pathlib import Path

config = configparser.ConfigParser()
basePath = Path(__file__).parent.parent
config.read(basePath / "Config/Config.ini")


class ReadConfig:
    @staticmethod
    def get_web_url():
        url = config['common info']['baseUrl']
        return url

    @staticmethod
    def get_browser_type():
        browser = config['behave.userdata']['Browser']
        return browser
