# Created by yanaamericana at 11/7/23
Feature: User is able navigate in target help page
  # Enter feature description here

  Scenario: Verify target help page
    Given Open target help page
    Then Verify target help header
    And Verify search help input field
    And Verify search button
    And Verify help options
    And Verify help link options
    And Verify browse all help pages header