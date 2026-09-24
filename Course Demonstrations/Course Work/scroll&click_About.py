from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

bot = driver.find_element(By.LINK_TEXT, "Elemental Selenium")
print("Bottom link found:", bot.text)

bot.click()
print("Bottom link clicked successfully!")

time.sleep(3)

driver.quit()