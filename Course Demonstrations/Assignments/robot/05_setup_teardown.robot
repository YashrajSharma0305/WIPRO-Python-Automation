*** Settings ***
Library    SeleniumLibrary

Suite Setup       Open SauceDemo
Suite Teardown    Close Browser
Test Setup        Login To SauceDemo
Test Teardown     Logout From SauceDemo


*** Variables ***
${URL}             https://www.saucedemo.com/
${USERNAME}        standard_user
${PASSWORD}        secret_sauce


*** Test Cases ***
Verify Inventory Page

    Location Should Contain    /inventory.html
    Page Should Contain        Products
    Log    Inventory page verified successfully.


Verify Products Page

    Location Should Contain    /inventory.html
    Page Should Contain Element    class=inventory_list
    Log    Products section verified successfully.


*** Keywords ***
Open SauceDemo

    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Log    Browser opened successfully.


Login To SauceDemo

    Input Text    id=user-name    ${USERNAME}
    Input Text    id=password     ${PASSWORD}
    Click Button  id=login-button

    Location Should Contain    /inventory.html
    Log    Login completed successfully.


Logout From SauceDemo

    Click Button    id=react-burger-menu-btn
    Wait Until Element Is Visible    id=logout_sidebar_link    5s
    Click Element    id=logout_sidebar_link

    Log    User logged out successfully.