from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("I open the SauceDemo login page")
def open_login_page(context):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    context.driver.get("https://www.saucedemo.com/")


@when('I enter the username "{username}"')
def enter_username(context, username):

    username_field = context.driver.find_element(
        By.ID,
        "user-name"
    )

    username_field.send_keys(username)


@when('I enter the password "{password}"')
def enter_password(context, password):

    password_field = context.driver.find_element(
        By.NAME,
        "password"
    )

    password_field.send_keys(password)


@when("I click the login button")
def click_login(context):

    login_button = context.driver.find_element(
        By.XPATH,
        "//input[@type='submit']"
    )

    login_button.click()


@then("I should be redirected to the inventory page")
def verify_inventory_page(context):

    assert "/inventory.html" in context.driver.current_url

    print("Login successful!")
    print("Current URL:", context.driver.current_url)

    context.driver.quit()