from behave import then
from selenium.webdriver.common.by import By


@then('the login result should be "{result}"')
def verify_login_result(context, result):

    if result == "success":

        assert "/inventory.html" in context.driver.current_url

        print("Login successful.")

    elif result == "error":

        error_message = context.driver.find_element(
            By.CSS_SELECTOR,
            "h3[data-test='error']"
        )

        assert error_message.is_displayed()

        print("Login failed as expected.")
        print("Error message:", error_message.text)

    context.driver.quit()