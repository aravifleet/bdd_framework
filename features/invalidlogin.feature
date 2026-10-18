
Feature: Invalid login functionality

  Scenario: Login using invalid username and password
    Given the user is on the login page
    When the user enters invalid username and password and clicks Submit
    Then the same page URL will be displayed
    And the "Your username is invalid!" text should be visible
