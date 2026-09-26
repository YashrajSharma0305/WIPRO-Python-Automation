from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(
    "https://www.selenium.dev/selenium/web/window_switching_tests/page_with_frame.html"
)
time.sleep(2)
wait = WebDriverWait(driver, 10)

main_window = driver.current_window_handle

print("Main window:", main_window)


iframe = wait.until(
    EC.presence_of_element_located((By.TAG_NAME, "iframe"))
)

driver.switch_to.frame(iframe)

print("Successfully switched to iframe.")

driver.switch_to.default_content()

print("Returned to main page.")


driver.find_element(By.LINK_TEXT, "Open new window").click()

wait.until(
    EC.number_of_windows_to_be(2)
)

windows = driver.window_handles

print("Number of windows:", len(windows))

for window in windows:

    if window != main_window:

        driver.switch_to.window(window)

        break


print("New window title:", driver.title)
print("New window URL:", driver.current_url)


driver.close()


driver.switch_to.window(main_window)

print("Returned to main window.")
print("Main window URL:", driver.current_url)

print("Assignment 6 completed successfully!")

driver.quit()