from pytest_bdd import scenario, given, when, then
from playwright.sync_api import expect



@scenario("../features/invalidlogin.feature", "Login using invalid username and password")
def test_invalid_login():
    pass

@given("the user is on the login page")
def user_login_page(browser_page,login_url):
    browser_page.goto(login_url)
    
@when("the user enters invalid username and password and clicks Submit")   
def enter_invaid_credentials(browser_page):
    browser_page.locator("[name='username']").fill("sample1")
    browser_page.locator("[name='password']").fill("sample2")
    browser_page.locator("#submit").click()

@then("the same page URL will be displayed")
def same_page_url(browser_page):
    expect(browser_page).to_have_url("https://practicetestautomation.com/practice-test-login/")
    
@then('the "Your username is invalid!" text should be visible')
def invalid_credentials_message(browser_page):
    expect(browser_page.locator("//div[text()='Your username is invalid!']")).to_be_visible()
       


