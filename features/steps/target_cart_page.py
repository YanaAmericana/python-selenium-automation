from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify cart is empty message shown')
def verify_empty_cart_message(context):
    context.app.cart_page.verify_message_text()


@then('Verify item is in shopping cart')
def verify_item_in_cart(context):
    context.app.cart_page.verify_item_in_cart()


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.find_item_name_in_cart(context.product_name)


@then('Verify cart has {expected_amount} item(s)')
def verify_cart_items(context, expected_amount):
    context.app.cart_page.find_amount_items_in_cart(expected_amount)
