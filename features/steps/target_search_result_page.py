from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify search worked')
def verify_search(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert 'coffee' in search_results_header, f'Expected text coffee not in {search_results_header}'


@then('Verify search result url')
def verify_search_url(context):
    assert 'coffee' in context.driver.current_url


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
