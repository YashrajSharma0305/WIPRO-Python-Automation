*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Browser And Fill Login Form

    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window

    Input Text    id=user-name    standard_user

    Page Should Contain Element    id=user-name

    Log    Username field was successfully located and filled.

    Close Browser