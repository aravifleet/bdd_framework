from pytest_bdd import scenario,given,when,then
from playwright.sync_api import expect



@scenario("../features/validlogin.feature", "Login using valid username and password")
def test_valid_login():
    pass

@given("the user is on the login page")
def login_page(browser_page, login_url):
    browser_page.goto(login_url)
    
@when("the user enters valid username and password and clicks Submit")    
def enter_valid_credentials(browser_page):
    browser_page.locator("[name='username']").fill("student")
    browser_page.locator("[name='password']").fill("Password123")
    browser_page.locator("#submit").click()
    
    
@then("the successful login URL should be displayed")
def title_display(browser_page):
    expect(browser_page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    
    
@then('the "Logged In Successfully" heading should be visible')
def login_display(browser_page):
    expect(browser_page.locator("//*[text()='Logged In Successfully']")).to_be_visible()
    
    
@then('the "Log out" link should be visible')
def logout_display(browser_page):
    expect(browser_page.locator("//a[text()='Log out']")).to_be_visible()
    browser_page.locator("//a[text()='Log out']").click()
    expect(browser_page).to_have_url("https://practicetestautomation.com/practice-test-login/")
    expect(browser_page.locator("//*[text()='Test login']")).to_be_visible()