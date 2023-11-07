from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


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
