Feature: nopCommerce Logo
  Scenario: Logo presence on nopCommerce Home page
    Given Launch chrome browser
    When Open nopCommerce home page
    Then Verify that the logo present on page
    And Close browser