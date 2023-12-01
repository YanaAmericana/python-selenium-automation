from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in()

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


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.app.base_page.get_current_window()
    # print(context.original_window)


@when('Click on Target terms and conditions link')
def click_terms_conditions(context):
    context.app.sign_in_page.click_terms_conditions()


@then('Verify user is logged in')
def verify_user_logged_in(context):
    context.app.sign_in_page.user_logged_in()


@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions_opened(context):
    context.app.terms_conditions_page.verify_terms_conditions_opened()
