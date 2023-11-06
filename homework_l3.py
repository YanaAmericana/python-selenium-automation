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

# find sign in and click
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()

# verify sign in page
expected_result = 'Sign in'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f"result {actual_result} does not match expected result: {expected_result}"

# find create account btn and click
driver.find_element(By.ID, "createAccountSubmit").click()

# verify create account page
expected_result = 'Create account'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
assert expected_result == actual_result, f"result {actual_result} does not match expected result: {expected_result}"

# find amazon logo
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")

# find name input field
driver.find_element(By.ID, "ap_customer_name")

# find mobile number/e-mail input field
driver.find_element(By.ID, "ap_email")

# find password input field
driver.find_element(By.ID, "ap_password")

# find re-enter password input field
driver.find_element(By.ID, "ap_password_check")

# find continue button
driver.find_element(By.ID, "continue")

# verify legal text
expected_result = "Conditions of Use and Privacy Notice"
actual_result = driver.find_element(By.ID, "legalTextRow").text
assert expected_result in actual_result, f"{expected_result} is not in {actual_result}"

# find sign in link
driver.find_element(By.CSS_SELECTOR, "[href*=signin]")

driver.quit()
