from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

DEMO_PAUSE = 1.2

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.6)  # visible scroll pause
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
        time.sleep(DEMO_PAUSE)  # pause after click so the viewer can see the result

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        # Type character by character for demo effect
        for char in text:
            element.send_keys(char)
            time.sleep(0.07)
        time.sleep(DEMO_PAUSE)

    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_displayed(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def take_screenshot(self, name_prefix):
        """Takes a manual screenshot and saves it to the screenshots folder."""
        import os
        from datetime import datetime
        screenshot_dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{name_prefix}_{timestamp}.png"
        path = os.path.join(screenshot_dir, file_name)
        self.driver.save_screenshot(path)
        print(f"\n[MANUAL SCREENSHOT] Saved: {path}")
