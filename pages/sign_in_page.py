from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_HEADER = By.CSS_SELECTOR, ".kcHdEa"
    EMAIL_INPUT_FIELD = By.ID, "username"
    PW_INPUT_FIELD = By.ID, "password"
    LOGIN_BTN = By.ID, "login"

    def verify_sign_in_header(self):
        self.verify_text("Sign into your Target account", *self.SIGN_IN_HEADER)

    def input_email(self):
        self.input("jinnannie@integrately.net", *self.EMAIL_INPUT_FIELD)

    def input_pw(self):
        self.input("Test@1234", *self.PW_INPUT_FIELD)
        sleep(1)

    def click_login_btn(self):
        self.wait_for_element_click(*self.LOGIN_BTN)

    def user_logged_in(self):
        self.wait_for_element_disappear(*self.SIGN_IN_HEADER)
