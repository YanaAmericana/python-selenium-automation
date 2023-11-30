from selenium.webdriver.common.by import By

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
    context.app.main_page.click_on_sign_in()


@when('Confirm Sign in from right navigation menu')
def confirm_sign_in(context):
    context.app.main_page.confirm_click_sign_in()


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.main_page.click_on_cart_icon()
