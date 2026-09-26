from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver, 10)

start_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
)

start_button.click()

message = wait.until(
    EC.visibility_of_element_located((By.ID, "finish"))
)

text = message.text

print("Dynamic text:", text)

assert text == "Hello World!"

print("Assignment 2 completed successfully!")

driver.quit()