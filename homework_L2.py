from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import NoSuchElementException

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
# Return and Orders button and click
return_and_orders = driver.find_element(By.ID, "nav-orders")
return_and_orders.click()

# Verification
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f"result {actual_result} does not match expected result: {expected_result}"
# try:
#     email_field = driver.find_element(By.ID, 'ap_email')
# except NoSuchElementException:
#     assert False, "email field does not exists"

# Task 1: locators
# Amazon logo
amazon_logo = driver.find_element(By.XPATH, '//i[@aria-label="Amazon"]')

# Email field
email_field = driver.find_element(By.ID, 'ap_email')

# Continue button
continue_button = driver.find_element(By.ID, 'continue')

# Conditions of use link
conditions_of_use = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")

# Privacy Notice link
privacy_notice = driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")

# Need help link
need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
# Other issues with Sign-In link
need_help_link.click()
forgot_password = driver.find_element(By.ID, 'auth-fpp-link-bottom')
other_issues = driver.find_element(By.ID, 'ap-other-signin-issues-link')

# Create your Amazon account button
create_account_btn = driver.find_element(By.ID, 'createAccountSubmit')


driver.quit()
