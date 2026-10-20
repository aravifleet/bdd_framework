import playwright
import pytest
from playwright.sync_api import sync_playwright 




@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        with p.chromium.launch(headless=True, slow_mo=1000) as browser:
            page = browser.new_page()
            yield page
            
@pytest.fixture  
def login_url():
    return "https://practicetestautomation.com/practice-test-login/"