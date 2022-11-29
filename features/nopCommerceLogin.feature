Feature: nopCommerce Login
  Scenario: Login to nopCommerce with valid email and valid password
    Given I launch Chrome browser
    When I open nopCommerce Home Page
    And Enter email as "admin@yourstore.com" and password as "admin"
    And Click on login button
    Then User must be successfully logged in to the Dashboard page

  Scenario Outline: Login to nopCommerce with multiple email and passwords
    Given I launch Chrome browser
    When I open nopCommerce Home Page
    And Enter email as "<email>" and password as "<password>"
    And Click on login button
    Then User must be successfully logged in to the Dashboard page

    Examples:
      |email|password|
      |  admin@yourstore.com   |     admin   |
      |  admin1@yourstore.com  |     admin   |
      |  admin1@yourstore.com  |    admin123 |
      |  admin@yourstore.com   |    admin112 |