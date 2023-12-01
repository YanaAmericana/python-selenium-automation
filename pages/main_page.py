from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    CIRCLE_LINK_FOOTER = (By.CSS_SELECTOR, "a[href*='circle'] [class*='BaseCellWrapper']")
    SIGN_IN_ICON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_RIGHT_NAV_MENU = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGNIN_IN_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")

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

    def hover_over_signin(self):
        signin_btn = self.find_element(*self.SIGNIN_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(signin_btn)
        actions.perform()

    def verify_signin_arrow_shown(self):
        self.wait_for_element_visible(*self.SIGNIN_IN_ARROW)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(1)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(1)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(1)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(1)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(1)

    def click_circle_link_footer(self):
        self.click(*self.CIRCLE_LINK_FOOTER)
