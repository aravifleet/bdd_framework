
Feature: Valid login functionality

  Scenario: Login using valid username and password
    Given the user is on the login page
    When the user enters valid username and password and clicks Submit
    Then the successful login URL should be displayed
    And the "Logged In Successfully" heading should be visible
    And the "Log out" link should be visible
