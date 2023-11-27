from selenium.webdriver.common.by import By
from behave import given, when, then



@when('Confirm Sign in')
def confirm_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Sign in page is loaded')
def sign_in_page_is_loaded(context):
    result = context.driver.find_element(By.CSS_SELECTOR, ".kcHdEa").text
    expected_result = "Sign into your Target account"
    assert expected_result in result, f"{expected_result} is not found in {result}"
