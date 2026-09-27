from behave import given, when, then
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given("I am on the SauceDemo login page")
def open_saucedemo(context):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

    context.driver.get("https://www.saucedemo.com/")

    # Create Page Object
    context.login_page = LoginPage(context.driver)


@when('I login with username "{username}" and password "{password}"')
def login_using_pom(context, username, password):

    context.login_page.login(
        username,
        password
    )


@then("the inventory page should be displayed")
def verify_inventory_page(context):

    context.inventory_page = InventoryPage(
        context.driver
    )

    assert context.inventory_page.is_inventory_page_opened()

    print("Inventory page opened successfully.")

    context.driver.quit()