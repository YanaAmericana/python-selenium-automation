Feature: Search tests

  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    And Verify search result url

  Scenario: User can see cart is empty message
    Given Open target main page
    When Click on cart icon
    Then Verify cart is empty message shown

  Scenario: User can add a product to the cart
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    And Choose shop in store option
    When I chose a product to add to shopping cart
    Then I confirm product to add to shopping cart
    When I click on view shopping cart
    Then Verify item is in shopping cart

