from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADER = By.CSS_SELECTOR, ".kcHdEa"
    EMAIL_INPUT_FIELD = By.ID, "username"
    PW_INPUT_FIELD = By.ID, "password"
    LOGIN_BTN = By.ID, "login"
    TERMS_CONDITIONS_LINK = (By.CSS_SELECTOR, "[aria-label*='terms']")


    def open_sign_in(self):
        self.open_url('https://www.target.com/login')

    def verify_sign_in_header(self):
        self.verify_text("Sign into your Target account", *self.SIGN_IN_HEADER)

    def input_email(self):
        self.input("", *self.EMAIL_INPUT_FIELD)

    def input_pw(self):
        self.input("", *self.PW_INPUT_FIELD)
        sleep(1)

    def click_login_btn(self):
        self.wait_for_element_click(*self.LOGIN_BTN)

    def user_logged_in(self):
        self.wait_for_element_disappear(*self.SIGN_IN_HEADER)

    def click_terms_conditions(self):
        self.click(*self.TERMS_CONDITIONS_LINK)