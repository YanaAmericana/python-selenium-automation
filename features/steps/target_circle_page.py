from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CARDS = (By.CSS_SELECTOR, "li[class*='BenefitCard']")


@given('Open Circle page')
def open_circle(context):
    context.app.circle_page.open_circle()


@then('Verify there are {number} benefit boxes')
def verify_benefit_boxes(context, number):
    actual_cards_number = context.driver.find_elements(*BENEFIT_CARDS)
    expected_cards_number = int(number)
    assert len(actual_cards_number) == expected_cards_number, \
        f"expected {expected_cards_number} number does not match actual {actual_cards_number} number of cards"


@then('Verify that clicking though Circle tabs works')
def verify_can_click_tabs(context):
    context.app.circle_page.verify_can_click_tabs()
