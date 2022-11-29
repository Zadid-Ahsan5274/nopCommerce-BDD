from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when('I open nopCommerce Home Page')
def openLoginPage(context):
    context.driver.get("https://admin-demo.nopcommerce.com/login")

@when('Enter email as "{email}" and password as "{password}"')
def provideCreds(context,email,password):
    context.driver.find_element(By.ID, "Email").clear()
    context.driver.find_element(By.ID,"Email").send_keys(email)

    context.driver.find_element(By.ID, "Password").clear()
    context.driver.find_element(By.ID, "Password").send_keys(password)

@when('Click on login button')
def clickLogInButton(context):
    context.driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()

@then('User must be successfully logged in to the Dashboard page')
def verifyDashboardPage(context):
    try:
      actual_title = context.driver.title
    except:
        context.driver.quit()
        assert False,"Test Failed"
    if actual_title == "Dashboard / nopCommerce administration":
        context.driver.quit()
        assert True, "Test Passed"


