import pytest
from playwright.sync_api import Page

from fixtures.browsers import chromium_page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage
from pages.courses_list_page import CoursesListPage


@pytest.fixture
def login_page(chromium_page:LoginPage) -> Page:
    return LoginPage(page=chromium_page)

@pytest.fixture
def registration_page(chromium_page:RegistrationPage) -> Page:
    return RegistrationPage(page=chromium_page)

@pytest.fixture
def dashboard_page(chromium_page:DashboardPage) -> Page:
    return DashboardPage(page=chromium_page)

@pytest.fixture
def dashboard_page_with_state(chromium_page_with_state:DashboardPage) -> Page:
    return DashboardPage(page=chromium_page_with_state)

@pytest.fixture
def courses_list_page(chromium_page_with_state:CoursesListPage) -> Page:
    return CoursesListPage(page=chromium_page_with_state)

@pytest.fixture
def create_course_page(chromium_page_with_state:CreateCoursePage) -> Page:
    return CreateCoursePage(page=chromium_page_with_state)

