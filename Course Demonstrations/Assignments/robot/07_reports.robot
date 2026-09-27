*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://www.saucedemo.com/
${USERNAME}    standard_user
${PASSWORD}    secret_sauce


*** Test Cases ***
Generate Execution Logs

    Log    Starting SauceDemo test.
    
    Open Browser    ${URL}    chrome
    Log    SauceDemo website opened successfully.

    Maximize Browser Window
    Log    Browser maximized.

    Input Text    id=user-name    ${USERNAME}
    Log    Username entered successfully.

    Input Text    id=password    ${PASSWORD}
    Log    Password entered successfully.

    Click Button    id=login-button
    Log    Login button clicked.

    Location Should Contain    /inventory.html
    Log    Login verification successful.

    Page Should Contain    Products
    Log    Products page verified successfully.

    Close Browser
    Log    Browser closed successfully.