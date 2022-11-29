Feature: nopCommerce Login

  Background: Common Steps
    Given I launch browser
    When I open nopCommerce Page
    And Enter valid email and password
    And Click on login

  Scenario: Login to nopCommerce
    Then User shall be in homepage

  Scenario: Search User
    When Click on customers and online customers
    Then Online customers should be displayed

  Scenario: Search User
    When Click on promotions and discounts tab
    Then Search discount page should open

