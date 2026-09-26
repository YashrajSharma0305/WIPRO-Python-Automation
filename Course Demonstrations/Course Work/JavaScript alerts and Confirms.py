from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(
    By.XPATH, "//button[text()='Click for JS Alert']"
).click()

alert = driver.switch_to.alert

print("Alert message:", alert.text)

alert.accept()

driver.find_element(
    By.XPATH, "//button[text()='Click for JS Confirm']"
).click()

confirm = driver.switch_to.alert

print("Confirm message:", confirm.text)

confirm.dismiss()


driver.find_element(
    By.XPATH, "//button[text()='Click for JS Prompt']"
).click()

prompt = driver.switch_to.alert

print("Prompt message:", prompt.text)

prompt.send_keys("[1, 2, 3, 4]")

prompt.accept()

print("Prompt submitted successfully!")

driver.quit()