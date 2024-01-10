from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
url = "https://www.saucedemo.com/"
driver.get(url)

# Display cookies before login
cookies_before_login = driver.get_cookies()
print("Cookies before login:", cookies_before_login)

# Locate the username, password, and login button elements
username_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
password_input = driver.find_element(By.XPATH, "//input[@id='password']")
login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

# Enter credentials and click the login button
username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Sleep for a moment to ensure the login process is completed
time.sleep(2)

# Display cookies after login
cookies_after_login = driver.get_cookies()
print("Cookies after login:", cookies_after_login)

# click side button
side_button = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
side_button.click()
time.sleep(2)

# Perform logout
logout_button = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
logout_button.click()

# Close the browser window
driver.quit()