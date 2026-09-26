from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
login_button.click()

time.sleep(2)

assert "/inventory.html" in driver.current_url

print("Login successful!")
print("Current URL:", driver.current_url)

driver.quit()