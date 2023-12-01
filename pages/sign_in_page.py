from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):
    EMAIL_INPUT_FIELD = (By.ID, "username")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='authAlertDisplay']")
    LOGIN_BTN = (By.ID, "login")
    PW_INPUT_FIELD = (By.ID, "password")
    SIGN_IN_HEADER = (By.CSS_SELECTOR, ".kcHdEa")
    TERMS_CONDITIONS_LINK = (By.CSS_SELECTOR, "[aria-label*='terms']")


    def open_sign_in(self):
        self.open_url('https://www.target.com/login')

    def verify_sign_in_header(self):
        self.verify_text("Sign into your Target account", *self.SIGN_IN_HEADER)

    def input_email(self):
        self.input("", *self.EMAIL_INPUT_FIELD)

    def input_incorrect_email(self):
        self.input("jhglygliu@testing.com", *self.EMAIL_INPUT_FIELD)


    def input_pw(self):
        self.input("", *self.PW_INPUT_FIELD)
        sleep(1)

    def input_incorrect_pw(self):
        self.input("Test@12345", *self.PW_INPUT_FIELD)
        sleep(1)

    def click_login_btn(self):
        self.wait_for_element_click(*self.LOGIN_BTN)

    def user_logged_in(self):
        self.wait_for_element_disappear(*self.SIGN_IN_HEADER)

    def click_terms_conditions(self):
        self.click(*self.TERMS_CONDITIONS_LINK)

    def verify_error_message(self, text_message):
        self.verify_partial_text(text_message, *self.ERROR_MESSAGE)
