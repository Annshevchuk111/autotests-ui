import pytest
from playwright.sync_api import Page

from fixtures.browsers import chromium_page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(chromium_page:LoginPage) -> Page:
    return LoginPage(page=chromium_page)