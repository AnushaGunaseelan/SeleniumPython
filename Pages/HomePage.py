import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Helper.SeleniumHelper import SeleniumHelper


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def check_homepage(self, url):
        time.sleep(3)
        current_url = self.driver.current_url
        assert current_url == url

    def verify_title(self):
        actual_text = self.driver.find_element("xpath", "//p[@class='site-title']//a").text
        assert actual_text == "Katalon Shop"

    def additemstocart(self, item):
        SeleniumHelper(self.driver).element_is_present(f"a[data-product_sku='{item}']").click()
        SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, f"a[data-product_sku='{item}']+a[title='View cart']")

    def navigatetocart(self):
        SeleniumHelper(self.driver).element_is_present(f"a[href='https://cms.demo.katalon.com/cart/']").click()

    def navigatetopage(self, page):
        if page == 'CART':
            SeleniumHelper(self.driver).element_is_present(f"a[href='https://cms.demo.katalon.com/cart/']").click()
        elif page == 'CHECKOUT':
            SeleniumHelper(self.driver).element_is_present(f"a[href='https://cms.demo.katalon.com/checkout/']").click()
        elif page == 'MYACCOUNT':
            SeleniumHelper(self.driver).element_is_present(f"a[href='https://cms.demo.katalon.com/my-account/']").click()

    def searchitem(self, item):
        SeleniumHelper(self.driver).element_to_be_clickable(By.CSS_SELECTOR, ".search-field").send_keys(item)
        SeleniumHelper(self.driver).element_to_be_clickable(By.CSS_SELECTOR, ".search-submit").click()

    def verif_search_item_displayed(self, item):
        actual_title_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".page-title").text
        assert actual_title_text == f"Search Results for: {item}"

        actual_item_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".content-area .entry-title").text
        assert actual_item_text == item

    def click_item(self, item):
        SeleniumHelper(self.driver).element_is_visible(By.XPATH, f"//h2[text()='{item}']").click()

    def click_the_page(self, page_number):
        SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, f"a[href='https://cms.demo.katalon.com/page/{page_number}/']").click()

    def verify_product_list_page_displayed(self, expected_text):
        actual_text = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".woocommerce-result-count").text
        assert actual_text == expected_text

    def sort_product_list(self, sorting_type):
        element = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".orderby")
        drop_down = Select(element)
        drop_down.select_by_visible_text(sorting_type)

    def verify_items_listed(self, first_item_name, first_item_price, last_item_name, last_item_price):
        product_titles = self.driver.find_elements(By.CSS_SELECTOR, ".columns-3 .product "
                                                                    ".woocommerce-loop-product__title")
        count_product_titles = len(product_titles)

        # Assert First Item Name in te list
        assert product_titles[0].text == first_item_name

        # Assert Last Item Name in the list
        assert product_titles[count_product_titles-1].text == last_item_name

        product_prices = self.driver.find_elements(By.CSS_SELECTOR, ".columns-3 .product .price .amount")
        count_product_prices = len(product_prices)

        # Assert First Item price in te list
        assert product_prices[0].text == first_item_price

        # Assert Last Item price in the list
        assert product_prices[count_product_prices - 1].text == last_item_price

    def verify_selected_sorting_option(self, sorting_option):
        element = SeleniumHelper(self.driver).element_is_visible(By.CSS_SELECTOR, ".orderby")
        drop_down = Select(element)
        assert sorting_option == drop_down.first_selected_option.text
