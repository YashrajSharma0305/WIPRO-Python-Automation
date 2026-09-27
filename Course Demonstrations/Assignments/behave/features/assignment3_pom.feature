Feature: SauceDemo Login using Page Object Model

  Scenario: Login using Page Object Model
    Given I am on the SauceDemo login page
    When I login with username "standard_user" and password "secret_sauce"
    Then the inventory page should be displayed