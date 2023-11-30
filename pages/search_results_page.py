from selenium.webdriver.common.by import By


from pages.base_page import Page


class SearchResultsPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
    PRODUCT_SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage']")
    SEARCH_RESULT_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    SHOP_IN_STORE_BTN = (By.CSS_SELECTOR, "[data-test='facet-card-Shop in store']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")

    def verify_search_result(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT_TXT)

    def verify_search_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)

    def click_shop_in_store_option(self):
        self.wait_for_element_click(*self.SHOP_IN_STORE_BTN)

    def choose_item_to_add(self):
        results = self.find_elements(*self.PRODUCT_SEARCH_RESULTS)
        if len(results) > 0:
            results[0].click()

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def find_product_name(self):
        return self.wait_for_element_appear(*self.SIDE_NAV_PRODUCT_NAME).text
