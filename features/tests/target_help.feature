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

  Scenario: User can select Help topic
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify Current promotions page opened

  Scenario: User can click on help topic in the footer of the page
    Given Open target main page
    When Click on target circle link in the footer
    Then Verify circle page is loaded