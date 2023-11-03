from behave import *

from Pages.ProductPage import ProductPage


@then('verify full product details displayed "{item}"')
def verify_full_product_details_displayed(context, item):
    ProductPage(context.driver).verify_full_product_details_displayed(item)


@when('I Add Item To Cart From Product Details Page')
def add_item_to_cart_from_product_page(context):
    ProductPage(context.driver).add_item_to_cart_from_product_page()


@when('I Change the quantity to "{quantity}"')
def change_quantity(context, quantity):
    ProductPage(context.driver).change_quantity(quantity)
