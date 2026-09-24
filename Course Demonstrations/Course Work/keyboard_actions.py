from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

email_field = driver.find_element(By.ID, "email")
email_field.click()

actions = ActionChains(driver)
actions.send_keys("yashraj@gmail.com")

actions.key_down(Keys.SHIFT)

actions.send_keys(Keys.HOME)

actions.key_up(Keys.SHIFT)

actions.perform()

actions.release()

time.sleep(2)
driver.quit()