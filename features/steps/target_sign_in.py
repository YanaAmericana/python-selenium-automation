from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click Sing in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(3)

    account_modal = context.driver.find_element(By.CSS_SELECTOR, "[data-test='modal-drawer-heading']")
    assert "Account" in account_modal.text, f"Account modal in not present"


@when('Confirm Sign in')
def confirm_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Sign in page is loaded')
def sign_in_page_is_loaded(context):
    result = context.driver.find_element(By.CSS_SELECTOR, ".kcHdEa").text
    expected_result = "Sign into your Target account"
    assert expected_result in result, f"{expected_result} is not found in {result}"