from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SEARCH_PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='PictureSecondary']")
SEARCH_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='product-title']")


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


@then('I confirm product to add to shopping cart')
def confirm_add_item_to_cart(context):
    context.driver.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[data-test='orderPickupButton']")),
        message="Add to cart btn is not present"
    )

    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()


@when('I click on view shopping cart')
def click_view_shopping_cart(context):
    context.driver.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[href='/cart']")),
        message="View cart btn is not present"
    )

    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()


# reusable var and url search (more than 2 words!):
@then('Verify search worked for {product}')
def verify_search(context, product):
    context.app.search_results_page.verify_search_result(product)


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    context.app.search_results_page.verify_search_url(expected_keyword)


@then("Verify search results have images")
def verify_products_image(context):
    product_imgs = context.driver.find_elements(*SEARCH_PRODUCT_IMG)
    assert len(product_imgs) == 4, f"only {len(product_imgs)} have images"


@then("Verify search results have product name")
def verify_product_name(context):
    product_names = context.driver.find_elements(*SEARCH_PRODUCT_NAME)
    assert len(product_names) == 4, f"Only {len(product_names)} have images"