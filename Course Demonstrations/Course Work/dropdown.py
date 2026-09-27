from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  
from webdriver_manager.chrome import ChromeDriverManager
import time

browser_name = "chrome"

if browser_name.lower() == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser_name.lower() == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose either 'chrome' or 'firefox'.")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
dropdown = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
select = Select(dropdown)
select.select_by_value("option1")
select.select_by_value("option2")
select.select_by_value("option3")
time.sleep(2)
driver.quit()