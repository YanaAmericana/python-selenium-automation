from selenium.webdriver.common.by import By
from behave import given, when, then


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then('Verify cart is empty message shown')
def verify_empty_cart_message(context):
    message = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']")

    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_result == actual_result and message.is_displayed(), f"{expected_result} in not visible"


@then('Verify item is in shopping cart')
def verify_item_in_cart(context):

    element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    element = element.title()
    assert "Coffee" in element, f"items in the cart does not contain Coffee"

    number_of_items = context.driver.find_element(By.CSS_SELECTOR, ".jaXVgU").text
    assert "1" in number_of_items, f"expected number of item does not match"


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == actual_name, f'Expected {context.product_name}, but got {actual_name}'


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    summary_text = context.driver.find_element(*CART_SUMMARY).text
    assert f'{amount} item' in summary_text, f"Expected '{amount} item' not in {summary_text}"