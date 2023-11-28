from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then

ACCOUNT_MODAL = By.CSS_SELECTOR, "[data-test='modal-drawer-heading']"

@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)


@when('Click Sing in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    context.driver.wait.until(
        EC.presence_of_element_located(ACCOUNT_MODAL),
        message="Account modal in not present"
    )


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.main_page.click_on_cart_icon()
