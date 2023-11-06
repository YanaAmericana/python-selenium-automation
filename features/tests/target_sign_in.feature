# Created by yanaamericana at 11/6/23
Feature: Sign In
  # Enter feature description here

  Scenario: Logged out user can sign in
    Given Open target main page
    When Click Sing in
    And Confirm Sign in
    Then Sign in page is loaded