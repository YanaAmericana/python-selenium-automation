from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CartPage(Page):
    MESSAGE = By.XPATH, "//div[@data-test='boxEmptyMsg']"

    def verify_message_text(self):
        expected_text = "Your cart is empty"
        actual_text = self.find_element(*self.MESSAGE).text
        assert expected_text == actual_text, f"{expected_text} in not visible"