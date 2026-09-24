from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)

linkable_text = driver.find_element(By.LINK_TEXT, "Blog")
linkable_text.click()
time.sleep(2)

driver.quit()