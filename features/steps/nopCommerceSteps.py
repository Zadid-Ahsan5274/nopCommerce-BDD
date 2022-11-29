from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Edge()

@when('Open nopCommerce home page')
def openHomePage(context):
    context.driver.get("https://demo.nopcommerce.com/")



@then('Verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,"//img[@alt='nopCommerce demo store']").is_displayed()
    assert status is True



@then('Close browser')
def closeBrowser(context):
    context.driver.quit()
