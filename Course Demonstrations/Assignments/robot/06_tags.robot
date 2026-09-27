*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://www.saucedemo.com/
${USERNAME}    standard_user
${PASSWORD}    secret_sauce


*** Test Cases ***
Valid Login Test
    [Tags]    smoke    login
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Text    id=user-name    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    id=login-button
    Location Should Contain    /inventory.html
    Log    Valid login test passed.
    Close Browser


Verify Products
    [Tags]    regression    products
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Input Text    id=user-name    ${USERNAME}
    Input Text    id=password    ${PASSWORD}
    Click Button    id=login-button
    Page Should Contain    Products
    Page Should Contain Element    class=inventory_list
    Log    Product verification passed.
    Close Browser


Verify Login Page
    [Tags]    smoke    regression
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Page Should Contain Element    id=user-name
    Page Should Contain Element    id=password
    Page Should Contain Element    id=login-button
    Log    Login page verification passed.
    Close Browser