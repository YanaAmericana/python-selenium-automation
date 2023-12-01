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

  Scenario: Verify error message when signin with incorrect credentials
    Given Open target main page
    When Click Sing in
    And Confirm Sign in from right navigation menu
    Then Sign in page is loaded
    When Input incorrect email
    And Input incorrect password
    When Click Sing in button
    Then Verify We can't find your account. message

  Scenario: User can open and close Terms and Conditions from sign in page
#    Given Open sign in page
    Given Open target main page
    When Click Sing in
    And Confirm Sign in from right navigation menu
    Then Sign in page is loaded
    When Store original windows
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Return to original window
