from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Logger.LogGen import LogGen


class SeleniumHelper:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        # log.info(f"Opening page: {page_url}")
        self.driver.get(page_url)

    def insert_text_in_input_field(self, locator, input_text):
        logger = LogGen.loggen()
        logger.info(f"Entering text: {input_text} in locator: {list(locator.values())[0]}")
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).send_keys(input_text)

    def click(self, locator):
        logger = LogGen.loggen()
        logger.info(f"Clicking on: {list(locator.values())[0]}")
        self.driver.find_element(list(locator.keys())[0], list(locator.values())[0]).click()

    def element_is_present(self, locator, timeout=120):
        logger = LogGen.loggen()
        logger.info(locator)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator))
            )
            return element
        except:
            logger.info(f"Element not found {locator}")

    def element_is_visible(self, by, locator, timeout=120):
        logger = LogGen.loggen()
        logger.info(locator)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element
        except:
            logger.info(f"Element not visible {locator}")

    def element_not_visible(self, locator, timeout=120):
        logger = LogGen.loggen()
        logger.info(locator)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, locator))
            )
            return element
        except:
            logger.info(f"Element visible {locator}")

    def element_to_be_clickable(self, by, locator, timeout=120):
        logger = LogGen.loggen()
        logger.info(locator)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            return element
        except:
            logger.info(f"Element not clickable {locator}")

    def presence_of_element_located(self, by, locator, timeout=120):
        logger = LogGen.loggen()
        logger.info(locator)
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except:
            logger.info(f"element not present {locator}")
