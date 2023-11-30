from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Sign in page is loaded')
def sign_in_page_is_loaded(context):
    context.app.sign_in_page.verify_sign_in_header()


@when('Input email')
def input_email(context):
    context.app.sign_in_page.input_email()


@when('Input password')
def input_password(context):
    context.app.sign_in_page.input_pw()


@when('Click Sing in button')
def click_login_btn(context):
    context.app.sign_in_page.click_login_btn()


@then('Verify user is logged in')
def verify_user_logged_in(context):
    context.app.sign_in_page.user_logged_in()
