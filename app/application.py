from pages.base_page import Page
from pages.circle_page import CirclePage
from pages.cart_page import CartPage
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.partner_page import PartnerPage
from pages.product_details_page import ProductDetailsPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.terms_conditions_page import TermsConditions


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)

        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.partner_page = PartnerPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.terms_conditions_page = TermsConditions(driver)
