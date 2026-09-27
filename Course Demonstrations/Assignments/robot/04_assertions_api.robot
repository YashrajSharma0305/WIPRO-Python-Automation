*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary


*** Test Cases ***
Verify Login Using Assertions

    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window

    Input Text    id=user-name    standard_user
    Input Text    id=password    secret_sauce
    Click Button    id=login-button

    ${current_url}=    Get Location
    Log    Current URL: ${current_url}

    Should Contain    ${current_url}    /inventory.html

    Page Should Contain    Products

    Log    Login verification passed.

    Close Browser


Verify API Response

    Create Session    jsonplaceholder    https://jsonplaceholder.typicode.com

    ${response}=    GET On Session    jsonplaceholder    /posts/1

    Log    API Status Code: ${response.status_code}
    Log    API Response: ${response.text}

    Should Be Equal As Integers    ${response.status_code}    200

    ${user_id}=    Evaluate    $response.json()["userId"]
    ${post_id}=    Evaluate    $response.json()["id"]

    Should Be Equal As Integers    ${user_id}    1
    Should Be Equal As Integers    ${post_id}    1

    ${title}=    Evaluate    $response.json()["title"]

    Should Be Equal As Strings    ${title}    sunt aut facere repellat provident occaecati excepturi optio reprehenderit

    Log    API response verification passed.