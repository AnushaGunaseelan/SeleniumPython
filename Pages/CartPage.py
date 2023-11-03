from selenium.webdriver.support.select import Select

from Helper.SeleniumHelper import SeleniumHelper
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_title(self):
        actual_text = self.driver.find_element("xpath", "//h1[@class='page-title']").text
        assert actual_text == "Cart"

    def verify_item_listed_in_cart(self, item):
        SeleniumHelper(self.driver).element_is_present(f"a[data-product_sku='{item}']")

    def remove_item_from_cart(self, item):
        SeleniumHelper(self.driver).element_is_present(f"a[data-product_sku='{item}']").click()

    def verify_item_removed_from_cart(self, item):
        SeleniumHelper(self.driver).element_not_visible(f"a[data-product_sku='{item}']")

    def proceed_to_checkout(self):
        SeleniumHelper(self.driver).element_to_be_clickable(By.CSS_SELECTOR, ".checkout-button").click()

    def verify_item_details_in_cart(self, item_name, item_price, quantity, total_price):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".woocommerce-cart-form__cart-item.cart_item")
        element = self.get_element_by_name(elements, item_name)

        # Assert
        assert element is not None

        # Assert item price
        actual_price = element.find_element(By.CSS_SELECTOR, ".product-price").text
        print(f"actual price={actual_price} expected price={item_price}")
        assert actual_price == item_price

        # Assert quantity
        actual_quantity = element.find_element(By.CSS_SELECTOR, ".input-text.qty.text").get_attribute("value")
        print(f"actual quantity={actual_quantity} expected quantity={quantity}")
        assert actual_quantity == quantity

        # Assert total price
        actual_total_price = element.find_element(By.CSS_SELECTOR, ".product-subtotal").text
        print(f"actual total price={actual_total_price} expected total price={total_price}")
        assert actual_total_price == total_price

    def change_the_quantity(self, quantity, item_name):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".woocommerce-cart-form__cart-item.cart_item")
        element = self.get_element_by_name(elements, item_name)
        element.find_element(By.CSS_SELECTOR, ".input-text.qty.text").clear()
        element.find_element(By.CSS_SELECTOR, ".input-text.qty.text").send_keys(quantity)

    def update_cart(self):
        SeleniumHelper(self.driver).element_to_be_clickable(By.XPATH, "//button[text()='Update cart']").click()

    def verify_cart_updated_message(self):
        actual_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".woocommerce-message").text
        assert actual_text.strip() == "Cart updated."

    def verify_cart_totals(self, subtotal, flat_rate, total):
        actual_subtotal = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".cart-subtotal "
                                                                                          ".woocommerce-Price-amount"
                                                                                          ".amount").text
        assert actual_subtotal == subtotal

        actual_flat_rate = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".shipping "
                                                                                           ".woocommerce-Price-amount"
                                                                                           ".amount").text
        assert actual_flat_rate == flat_rate

        actual_total = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".order-total "
                                                                                       ".woocommerce-Price-amount"
                                                                                       ".amount").text
        assert actual_total == total

    def cart_apply_coupon_code(self, coupon_code):
        SeleniumHelper(self.driver).element_to_be_clickable(By.NAME, "coupon_code").send_keys(coupon_code)
        SeleniumHelper(self.driver).element_to_be_clickable(By.NAME, "apply_coupon").click()

    def cart_verify_coupon_code_status_message(self, status_message):
        actual_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".woocommerce-error").text
        print(actual_text.strip())
        print(status_message)
        assert actual_text.strip() == status_message

    def change_cart_shipping_address(self, country, county, city, postcode):
        SeleniumHelper(self.driver).element_to_be_clickable(By.CSS_SELECTOR, ".shipping-calculator-button").click()
        element = SeleniumHelper(self.driver).element_is_visible(By.ID, "calc_shipping_country")
        drop_down = Select(element)
        drop_down.select_by_visible_text(country)

        SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "calc_shipping_state").send_keys(county)

        SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "calc_shipping_city").send_keys(city)

        SeleniumHelper(self.driver).element_to_be_clickable(By.ID, "calc_shipping_postcode").send_keys(postcode)

    def click_cart_update_address(self):
        SeleniumHelper(self.driver).element_to_be_clickable(By.NAME, "calc_shipping").click()

    def verify_cart_shipping_address_updated(self, country, county, city, postcode):
        expected_text = f"{city}, {county}, {postcode}, {country}"
        selector = f".//p//strong[contains(text(),'{city}, {county}, {postcode}, {country}')]"
        print(f"selector: {selector}")
        print(f"expected text: {expected_text}")
        actual_text = SeleniumHelper(self.driver).element_is_visible(By.XPATH, selector).text

        print(f"actual_text: {actual_text}")

        assert actual_text.strip() == expected_text

    def get_element_by_name(self, elements, item_name):
        for element in elements:
            name = element.find_element(By.CSS_SELECTOR, ".product-remove > a").get_attribute("data-product_sku")
            if item_name == name:
                return element
