import time

from Helper.SeleniumHelper import SeleniumHelper
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_full_product_details_displayed(self, item):
        actual_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".product_title.entry-title").text
        assert actual_text == item

    def add_item_to_cart_from_product_page(self):
        SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".single_add_to_cart_button.button").click()

    def change_quantity(self, quantity):
        SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".input-text.qty.text").clear()
        SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".input-text.qty.text").send_keys(quantity)
