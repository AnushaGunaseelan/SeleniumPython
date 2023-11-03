import time

from Helper.SeleniumHelper import SeleniumHelper
from selenium.webdriver.common.by import By


class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        actual_text = self.driver.find_element("xpath", "//h1[@class='page-title']").text
        assert actual_text == "My account"
