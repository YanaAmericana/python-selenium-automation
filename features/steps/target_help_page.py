from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TARGET_HELP_HEADER = (By.XPATH, "//h2[contains(text(), 'Help')]")
SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, ".search-input")
SEARCH_BTN = (By.CSS_SELECTOR, ".search-btn")
BROWSE_ALL_HELP_HEADER = (By.XPATH, "//h2[contains(text(), 'Browse all Help')]")


@given('Open target help page')
def open_target_help_page(context):
    context.driver.get("https://help.target.com/help")


@given('Open Help page for Returns')
def open_target_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {help_topic}')
def select_promotions(context, help_topic):
    context.app.help_page.select_topic(help_topic)


@then('Verify Returns page opened')
def verify_returns_opened(context):
    context.app.help_page.verify_returns_opened()


@then('Verify Current promotions page opened')
def verify_promotions_opened(context):
    context.app.help_page.verify_promotions_opened()

@then('Verify target help header')
def verify_target_help_header(context):
    context.driver.find_element(*TARGET_HELP_HEADER)


@then('Verify search help input field')
def verify_search_field(context):
    context.driver.find_element(*SEARCH_INPUT_FIELD)


@then('Verify search button')
def verify_search_btn(context):
    context.driver.find_element(*SEARCH_BTN)


@then('Verify help options')
def verify_help_options(context):
    # verify 6 options
    options = context.driver.find_elements(By.CSS_SELECTOR, ".box-column .grid_6")
    expected_options = 6
    assert len(options) == expected_options, f"amount of options does not match"

    # verify manage my account option
    context.driver.find_element(By.CSS_SELECTOR, ".salesforceBox").is_displayed()


@then('Verify help link options')
def verify_help_link_options(context):
    help_links = context.driver.find_elements(By.CSS_SELECTOR, ".grid_4")
    expected_links = 3
    assert len(help_links) == expected_links, f"amount of links to options does not match"


@then('Verify browse all help pages header')
def verify_browse_all_help_pages_header(context):
    context.driver.find_element(*BROWSE_ALL_HELP_HEADER)
