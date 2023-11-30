from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")
SIZE_OPTION = (By.CSS_SELECTOR, "[class*='ButtonSelectorLabel']")

@given('Open target product {item_number} page')
def open_target(context, item_number):
    context.driver.get('https://www.target.com/p/'+item_number)
    sleep(6)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Cream', 'Dark Gray', 'Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]  # 'Color\nBlack' => ['Color', 'Black']
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click through sizes')
def click_and_verify_sizes(context):
    list_sizes = []
    actual_sizes = []
    present_sizes = context.driver.find_elements(*SIZE_OPTION)

    for size in present_sizes:
        list_sizes.append(size.text)
        size.click()
        selected_size = context.driver.find_element(
            By.CSS_SELECTOR, "[role='group'] [class*='CellVariationHeaderWrapper']"
        ).text.split('\n')[1]
        actual_sizes.append(selected_size)

        assert list_sizes == actual_sizes, f"Shown sizes {list_sizes} do not match selected sizes {actual_sizes}"


@then('I confirm product to add to shopping cart')
def confirm_add_item_to_cart(context):
    context.app.product_details_page.click_add_to_cart_btn()