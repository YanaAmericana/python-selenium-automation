from selenium.webdriver.common.by import By

from pages.base_page import Page


class ProductDetailsPage(Page):
    ADD_TO_CART_BTN = By.CSS_SELECTOR, "[data-test='orderPickupButton']"
    VIEW_CART_RIGHT_NAV_BTN = By.CSS_SELECTOR, "[href='/cart']"

    def click_add_to_cart_btn(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BTN)

    def click_view_cart_right_nav(self):
        self.wait_for_element_click(*self.VIEW_CART_RIGHT_NAV_BTN)

