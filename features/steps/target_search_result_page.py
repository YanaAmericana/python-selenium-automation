from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # find_element by default it will pick 1st one
    # all_buttons = context.driver.find_elements(*ADD_TO_CART_BTN)
    # all_buttons[2].click()


@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message='Product name not shown in side navigation'
    )
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text

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


# reusable var and url search (more than 2 words!):
@then('Verify search worked for {product}')
def verify_search(context, product):
    search_results_header = context.driver.find_element(*SEARCH_RESULT_TXT).text
    assert product in search_results_header, f'Expected text {product} not in {search_results_header}'


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, \
        f'Expected {expected_keyword} not in {context.driver.current_url}'


