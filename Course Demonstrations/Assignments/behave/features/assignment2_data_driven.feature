Feature: Data Driven SauceDemo Login

  Scenario Outline: Login with different credentials
    Given I open the SauceDemo login page
    When I enter the username "<username>"
    And I enter the password "<password>"
    And I click the login button
    Then the login result should be "<result>"

    Examples:
      | username      | password     | result  |
      | standard_user | secret_sauce | success |
      | standard_user | wrong_pass   | error   |
      | wrong_user    | secret_sauce | error   |
      | wrong_user    | wrong_pass   | error   |