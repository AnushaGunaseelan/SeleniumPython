from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from Logger.LogGen import LogGen
from Config.readProperties import ReadConfig


def before_all(context):
    logger = LogGen.loggen()
    logger.info("I am inside before all")
    browser_type = ReadConfig.get_browser_type()
    context.browser_type = browser_type
    print(context.browser_type)


def before_scenario(context, scenario):
    logger = LogGen.loggen()
    logger.info("I am inside before scenario")
    context.driver = get_web_driver(context)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    logger = LogGen.loggen()
    logger.info("I am inside after scenario")
    context.driver.close()


def after_all(context):
    logger = LogGen.loggen()
    logger.info("I am inside after all")


def get_web_driver(context):
    if context.browser_type == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        return driver
    elif context.browser_type == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        return driver
