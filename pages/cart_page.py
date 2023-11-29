from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    MESSAGE = By.XPATH, "//div[@data-test='boxEmptyMsg']"

    def verify_message_text(self):
        self.verify_text('Your cart is empty', *self.MESSAGE)
