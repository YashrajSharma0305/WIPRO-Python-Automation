*** Settings ***
Library    libraries.custom_library.CustomLibrary

*** Test Cases ***
Test Custom Python Keywords

    ${sum}=    Calculate Sum    10    20
    Log    Calculated sum: ${sum}

    Should Be Equal As Integers    ${sum}    30

    ${greeting}=    Create Greeting    Yashraj
    Log    Greeting: ${greeting}

    Should Be Equal As Strings    ${greeting}    Hello, Yashraj!

Test BuiltIn Operations

    ${text}=    Set Variable    selenium automation

    ${upper_text}=    Evaluate    "${text}".upper()

    Log    Uppercase text: ${upper_text}

    Should Be Equal As Strings    ${upper_text}    SELENIUM AUTOMATION

    ${length}=    Get Length    ${text}

    Log    String length: ${length}

    Should Be Equal As Integers    ${length}    19