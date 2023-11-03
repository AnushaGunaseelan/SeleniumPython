import time

from selenium.webdriver.common.by import By

from Helper.SeleniumHelper import SeleniumHelper
from TestData.test_data import email_id, first_name, last_name, address_line1, city, postcode, phone_number, \
    invalid_email_id


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        actual_text = self.driver.find_element("xpath", "//h1[@class='page-title']").text
        assert actual_text == "Cart"

    def enter_billing_details(self, firstname=True, lastname=True, address=True, phone=True, email=True,
                              invalid_email=False):
        if firstname:
            SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_first_name").send_keys(first_name)

        if lastname:
            SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_last_name").send_keys(last_name)

        if address:
            SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_address_1").send_keys(address_line1)
            SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_city").send_keys(city)
            SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_postcode").send_keys(postcode)

        if phone:
            SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_phone").send_keys(phone_number)

        if email:
            if invalid_email:
                SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_email").send_keys(invalid_email_id)
            else:
                SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "billing_email").send_keys(email_id)

    def place_the_order(self):
        time.sleep(2)
        # SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "place_order").click()
        place_order_element = self.driver.find_element(By.ID, "place_order")
        self.driver.execute_script("arguments[0].click();", place_order_element)

    def verify_order_placed(self):
        actual_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".woocommerce-thankyou-order"
                                                                                      "-received").text
        assert actual_text == "Thank you. Your order has been received."

    def checkout_apply_coupon_code(self, coupon_code):
        SeleniumHelper(self.driver).element_to_be_clickable(By.CSS_SELECTOR, ".showcoupon").click()
        SeleniumHelper(self.driver).element_to_be_clickable(By.NAME, "coupon_code").send_keys(coupon_code)
        SeleniumHelper(self.driver).element_to_be_clickable(By.NAME, "apply_coupon").click()

    def checkout_verify_coupon_code_status_message(self, status_message):
        actual_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".woocommerce-error").text
        print(actual_text.strip())
        print(status_message)
        assert actual_text.strip() == status_message

    def verify_order_details_in_checkout(self, product, product_total, subtotal, flat_rate, total):
        actual_product = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR,
                                                                        ".cart_item .product-name").text
        print(actual_product.strip())
        print(product)
        assert actual_product.strip() == product

        actual_product_total = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".cart_item "
                                                                                               ".product-total").text
        assert actual_product_total == product_total

        actual_subtotal = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".cart-subtotal .amount").text
        assert actual_subtotal == subtotal

        actual_flat_rate = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".shipping .amount").text
        assert actual_flat_rate == flat_rate

        actual_total = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".order-total .amount").text
        assert actual_total == total

    def verify_required_field_message(self, field_name):
        selector = f".//li//strong[contains(text(), '{field_name}')]"
        actual_message = SeleniumHelper(self.driver).element_is_visible(By.XPATH, selector).text
        assert actual_message == field_name

    def verify_invalid_email_message(self):
        SeleniumHelper(self.driver).element_is_visible(By.XPATH,
                                                       ".//li[contains(text(), 'Invalid billing email address')]")

    def enter_the_order_notes(self, notes):
        SeleniumHelper(self.driver).element_is_visible(By.ID, "order_comments").send_keys(notes)
