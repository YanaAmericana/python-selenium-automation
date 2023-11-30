from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = By.ID, 'search'
    SEARCH_BTN = By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"
    CART_ICON = By.CSS_SELECTOR, "[data-test='@web/CartLink']"
    SIGN_IN_ICON = By.CSS_SELECTOR, "[data-test='@web/AccountLink']"
    SIGN_IN_RIGHT_NAV_MENU = By.CSS_SELECTOR, "[data-test='accountNav-signIn']"

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)  # wait for ads to disappear

    def click_on_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_on_sign_in(self):
        self.wait_for_element_click(*self.SIGN_IN_ICON)

    def confirm_click_sign_in(self):
        self.wait_for_element_click(*self.SIGN_IN_RIGHT_NAV_MENU)
