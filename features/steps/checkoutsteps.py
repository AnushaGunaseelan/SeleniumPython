from behave import *

from Pages.CheckoutPage import CheckoutPage


@when('I enter the billing details')
def enter_the_billing_details(context):
    CheckoutPage(context.driver).enter_billing_details()


@when('I place the order')
def place_the_order(context):
    CheckoutPage(context.driver).place_the_order()


@then('I verify order placed successfully')
def verify_order_placed(context):
    CheckoutPage(context.driver).verify_order_placed()


@when('I apply coupon code "{coupon_code}" in checkout page')
def checkout_apply_coupon_code(context, coupon_code):
    CheckoutPage(context.driver).checkout_apply_coupon_code(coupon_code)


@then('I verify coupon code status message "{status_message}" in checkout page')
def checkout_verify_coupon_code_status_message(context, status_message):
    CheckoutPage(context.driver).checkout_verify_coupon_code_status_message(status_message)


@then('I verify order details "{product}" and "{product_total}" and "{sub_total}" and "{flat_rate}" and "{total}"')
def verify_order_details_in_checkout(context, product, product_total, sub_total, flat_rate, total):
    CheckoutPage(context.driver).verify_order_details_in_checkout(product, product_total, sub_total, flat_rate, total)


@when('I not enter firstname and lastname')
def not_enter_firstname_lastname(context):
    CheckoutPage(context.driver).enter_billing_details(firstname=False, lastname=False)


@when('I not enter address')
def not_enter_address(context):
    CheckoutPage(context.driver).enter_billing_details(address=False)


@when('I not enter phone number')
def not_enter_phone_number(context):
    CheckoutPage(context.driver).enter_billing_details(phone=False)


@when('I not enter email')
def not_enter_email(context):
    CheckoutPage(context.driver).enter_billing_details(email=False)


@when('I enter invalid email')
def enter_invalid_email(context):
    CheckoutPage(context.driver).enter_billing_details(invalid_email=True)


@when('I enter the order notes "{notes}"')
def enter_the_order_notes(context, notes):
    CheckoutPage(context.driver).enter_the_order_notes(notes)


@then('I verify "{field_name}" is a required field message display')
def verify_required_field_message(context, field_name):
    CheckoutPage(context.driver).verify_required_field_message(field_name)


@then('I verify Invalid email message display')
def verify_invalid_email_message(context):
    CheckoutPage(context.driver).verify_invalid_email_message()
