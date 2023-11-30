# Created by yanaamericana at 11/6/23
Feature: Sign In
  # Enter feature description here

  Scenario: Logged out user can sign in
    Given Open target main page
    When Click Sing in
    And Confirm Sign in from right navigation menu
    Then Sign in page is loaded
    When Input email
    And Input password
    And Click Sing in button
    Then Verify user is logged in