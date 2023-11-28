from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = By.ID, 'search'
    SEARCH_BTN = By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"
    CART_BTN = By.CSS_SELECTOR, "[data-test='@web/CartLink']"

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)  # wait for ads to disappear

    def click_on_cart_icon(self):
        self.click(*self.CART_BTN)


