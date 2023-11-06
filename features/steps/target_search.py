from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(6)  # wait for ads to disappear


@then('Verify search worked')
def verify_search(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert 'coffee' in search_results_header, f'Expected text coffee not in {search_results_header}'


@then('Verify search result url')
def verify_search_url(context):
    assert 'coffee' in context.driver.current_url


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify cart is empty message shown')
def verify_empty_cart_message(context):
    message = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']")

    expected_result = "Your cart is empty"
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_result == actual_result and message.is_displayed(), f"{expected_result} in not visible"


@then('Choose shop in store option')
def choose_shop_in_store(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='facet-card-Shop in store']").click()
    # wait for results to load
    sleep(5)


@when('I chose a product to add to shopping cart')
def choose_item(context):
    results = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage']")
    if len(results) > 0:
        results[0].click()
    sleep(10)


@then('I confirm product to add to shopping cart')
def confirm_add_item_to_cart(context):
    add_to_cart_btn = context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']")

    assert add_to_cart_btn.is_displayed(), f"{add_to_cart_btn} is not present"
    add_to_cart_btn.click()
    sleep(7)


@when('I click on view shopping cart')
def click_view_shopping_cart(context):
    view_cart_btn = context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']")

    assert view_cart_btn.is_displayed(), f"{view_cart_btn} is not present"
    view_cart_btn.click()


@then('Verify item is in shopping cart')
def verify_item_in_cart(context):

    element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    element = element.title()
    assert "Coffee" in element, f"items in the cart does not contain Coffee"

    number_of_items = context.driver.find_element(By.CSS_SELECTOR, ".jaXVgU").text
    assert "1" in number_of_items, f"expected number of item does not match"
