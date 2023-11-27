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


# reusable var and url search (more than 2 words!):
  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee
    And Verify coffee in search result url

  Scenario: User can search for christmas lights
    Given Open target main page
    When Search for christmas lights
    Then Verify search worked for christmas lights
    And Verify christmas+lights in search result url

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search worked for <expected_product>
    And Verify <expected_url> in search result url
    Examples:
    |product          |expected_product    |expected_url     |
    |coffee           |coffee              |coffee           |
    |tea              |tea                 |tea              |
    |mug              |mug                 |mug              |
    |christmas lights |christmas lights    |christmas+lights |



  Scenario: User can add a product to cart
    Given Open target main page
    When Search for AirPods (3rd Generation)
    And Click on Add to Cart button
    And Store product name
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product


  Scenario: Searched product has name a and a image
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    And Verify search results have images
    And Verify search results have product name
