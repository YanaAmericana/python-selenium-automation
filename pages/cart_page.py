from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    MESSAGE = (By.XPATH, "//div[@data-test='boxEmptyMsg']")
    CART_ITEM_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")
    CART_SUMMARY_HEADER = (By.CSS_SELECTOR, ".jaXVgU")

    def verify_message_text(self):
        self.verify_text('Your cart is empty', *self.MESSAGE)

    def verify_item_in_cart(self):
        self.verify_partial_text("Coffee", *self.CART_ITEM_NAME)
        self.verify_partial_text("1", *self.CART_SUMMARY_HEADER)

    def find_amount_items_in_cart(self, expected_amount):
        self.verify_partial_text(expected_amount,*self.CART_SUMMARY)

    def find_item_name_in_cart(self, expected_name):
        self.verify_text(expected_name, *self.CART_ITEM_NAME)
