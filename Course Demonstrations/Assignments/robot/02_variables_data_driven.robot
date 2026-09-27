*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=test_data/login_data.csv

Test Template    Login Test

*** Variables ***
${URL}    https://www.saucedemo.com/

*** Test Cases ***
Login Test

*** Keywords ***
Login Test
    [Arguments]    ${username}    ${password}    ${expected}

    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Input Text    id=user-name    ${username}
    Input Text    id=password    ${password}

    Click Button    id=login-button

    IF    '${expected}' == 'success'
        Location Should Contain    /inventory.html
        Log    Login successful for ${username}
    ELSE
        Page Should Contain Element    css=h3[data-test="error"]
        Log    Login failed as expected for ${username}
    END

    Close Browser