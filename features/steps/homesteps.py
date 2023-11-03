from behave import *

from Pages.CartPage import CartPage
from Pages.CheckoutPage import CheckoutPage
from Pages.HomePage import HomePage
from Helper.SeleniumHelper import SeleniumHelper
from Config.readProperties import ReadConfig
from Pages.MyAccountPage import MyAccountPage


@given('open homepage url')
def openhomepage(context):
    SeleniumHelper(context.driver).open_page(ReadConfig.get_web_url())


@when('check homepage')
def checkhomepage(context):
    HomePage(context.driver).check_homepage(ReadConfig.get_web_url())


@then('verify homepage title')
def verifyhomepagetitle(context):
    HomePage(context.driver).verify_title()


@given('I add items to my cart "{itemname}"')
def add_items_to_cart(context, itemname):
    HomePage(context.driver).additemstocart(itemname)


@when('I view my cart')
def view_cart(context):
    HomePage(context.driver).navigatetocart()


@when('I click link "{page}"')
def click_page_link(context, page):
    HomePage(context.driver).navigatetopage(page)


@then('verify page displayed "{page}"')
def verify_page_displayed(context, page):
    if page == 'CART':
        CartPage(context.driver).verify_title()
    elif page == 'CHECKOUT':
        CheckoutPage(context.driver).verify_title()
    elif page == 'MyAccount':
        MyAccountPage(context.driver).verify_title()


@when('I search item "{item}"')
def search_item(context, item):
    HomePage(context.driver).searchitem(item)


@then('verify item "{item}" displayed')
def verify_search_item_displayed(context, item):
    HomePage(context.driver).verif_search_item_displayed(item)


@when('I click the item "{item}"')
def click_item(context, item):
    HomePage(context.driver).click_item(item)


@when('I click the page number "{page_number}"')
def click_the_page(context, page_number):
    HomePage(context.driver).click_the_page(page_number)


@then('verify product list page displayed "{expected_text}"')
def verify_product_list_page_displayed(context, expected_text):
    HomePage(context.driver).verify_product_list_page_displayed(expected_text)


@when('I sort by "{sorting_type}"')
def sort_product_list(context, sorting_type):
    HomePage(context.driver).sort_product_list(sorting_type)


@then(
    'verify items listed by popularity "{first_item_name}" and "{first_item_price}" and "{last_item_name}" and "{'
    'last_item_price}"')
@then(
    'verify items listed by latest "{first_item_name}" and "{first_item_price}" and "{last_item_name}" and "{'
    'last_item_price}"')
@then(
    'verify items listed by average rating "{first_item_name}" and "{first_item_price}" and "{last_item_name}" and "{'
    'last_item_price}"')
@then(
    'verify items listed by default sorting "{first_item_name}" and "{first_item_price}" and "{last_item_name}" and '
    '"{last_item_price}"')
@then(
    'verify items listed by high to low "{first_item_name}" and "{first_item_price}" and "{last_item_name}" and "{'
    'last_item_price}"')
@then('verify items listed by low to high "{first_item_name}" and "{first_item_price}" and "{last_item_name}" and "{'
      'last_item_price}"')
def verify_items_listed(context, first_item_name, first_item_price, last_item_name, last_item_price):
    HomePage(context.driver).verify_items_listed(first_item_name, first_item_price, last_item_name, last_item_price)


@then('verify "{sorting_option}" option selected')
def verify_selected_sorting_option_selected(context, sorting_option):
    HomePage(context.driver).verify_selected_sorting_option(sorting_option)
