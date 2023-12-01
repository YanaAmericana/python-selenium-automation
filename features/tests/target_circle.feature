# Created by yanaamericana at 11/7/23
Feature: User able to navigate in Target circle
  # Enter feature description here

  Scenario: Verify there are 5 options in Benefits section
    Given Open circle page
    Then Verify there are 5 benefit boxes


  Scenario: User can click through Circle tabs
    Given Open Circle page
    Then Verify that clicking though Circle tabs works


  Scenario: User is able to navigate to Google Play Target page
    Given Open Circle page
    And Store original window
    When Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current page
    And Return to original window
