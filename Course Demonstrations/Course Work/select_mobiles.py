from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2) 

driver.execute_script("window.scrollTo({top: 800, left: 0, behavior: 'smooth'});")
time.sleep(3)  

parent_menu = driver.find_element(By.XPATH, "//*[contains(text(), 'Point Me')]")
driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", parent_menu)
time.sleep(2)  
sub_option = driver.find_element(By.XPATH, "//a[contains(text(), 'Mobiles')]")
act = ActionChains(driver)
act.move_to_element(parent_menu).pause(2).move_to_element(sub_option).pause(2).click().perform()

print("Hovered over menu and selected Mobiles successfully.")

time.sleep(3)  
driver.quit()