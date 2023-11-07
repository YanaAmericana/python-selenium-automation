from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CARDS = (By.CSS_SELECTOR, "li[class*='BenefitCard']")

@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are {number} benefit boxes')
def verify_benefit_boxes(context, number):
    actual_cards_number = context.driver.find_elements(*BENEFIT_CARDS)
    expected_cards_number = int(number)
    assert len(actual_cards_number) == expected_cards_number, \
        f"expected {expected_cards_number} number does not match actual {actual_cards_number} number of cards"
