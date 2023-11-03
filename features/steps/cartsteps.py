import time

from behave import *

from Pages.CartPage import CartPage
from Pages.HomePage import HomePage
from Helper.SeleniumHelper import SeleniumHelper
from Config.readProperties import ReadConfig


@when('I verify items listed in my cart "{item_name}"')
@then('I verify items listed in my cart "{item_name}"')
def verify_items_listed_in_cart(context, item_name):
    CartPage(context.driver).verify_item_listed_in_cart(item_name)


@when('I remove items from cart "{item_name}"')
def remove_items_from_cart(context, item_name):
    CartPage(context.driver).remove_item_from_cart(item_name)


@then('I verify items removed from cart "{item_name}"')
def remove_items_from_cart(context, item_name):
    CartPage(context.driver).verify_item_removed_from_cart(item_name)


@when('I proceed to checkout')
def proceed_to_checkout(context):
    CartPage(context.driver).proceed_to_checkout()


@then('I verify item details in cart "{item_name}" and "{item_price}" and "{quantity}" and "{total_price}"')
def verify_item_details_in_cart(context, item_name, item_price, quantity, total_price):
    CartPage(context.driver).verify_item_details_in_cart(item_name, item_price, quantity, total_price)


@when('I change quantity to "{quantity}" for item "{item_name}"')
def change_the_quantity(context, quantity, item_name):
    CartPage(context.driver).change_the_quantity(quantity, item_name)


@when('I Update Cart')
def update_cart(context):
    CartPage(context.driver).update_cart()


@then('I verify cart updated message')
def verify_cart_updated_message(context):
    CartPage(context.driver).verify_cart_updated_message()


@then('I verify cart totals "{subtotal}" and "{flat_rate}" and "{total}"')
def verify_cart_total(context, subtotal, flat_rate, total):
    CartPage(context.driver).verify_cart_totals(subtotal, flat_rate, total)


@when('I change shipping address "{country}" and "{county}" and "{city}" and "{postcode}"')
def change_cart_shipping_address(context, country, county, city, postcode):
    CartPage(context.driver).change_cart_shipping_address(country, county, city, postcode)


@when('I click update address')
def click_cart_update_address(context):
    CartPage(context.driver).click_cart_update_address()


@then('I verify shipping address updated "{country}" and "{county}" and "{city}" and "{postcode}"')
def verify_cart_shipping_address_updated(context, country, county, city, postcode):
    CartPage(context.driver).verify_cart_shipping_address_updated(country, county, city, postcode)


@when('I apply coupon code "{coupon_code}"')
def cart_apply_coupon_code(context, coupon_code):
    CartPage(context.driver).cart_apply_coupon_code(coupon_code)


@then('I verify coupon code status message "{status_message}"')
def cart_verify_coupon_code_status_message(context, status_message):
    CartPage(context.driver).cart_verify_coupon_code_status_message(status_message)
