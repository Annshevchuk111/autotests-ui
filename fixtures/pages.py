import pytest
from playwright.sync_api import Page

from fixtures.browsers import page
from pages.courses.create_course_page import CreateCoursePage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.courses.courses_list_page import CoursesListPage


@pytest.fixture
def login_page(page:LoginPage) -> Page:
    return LoginPage(page=page)

@pytest.fixture
def registration_page(page:RegistrationPage) -> Page:
    return RegistrationPage(page=page)

@pytest.fixture
def dashboard_page(page:DashboardPage) -> Page:
    return DashboardPage(page=page)

@pytest.fixture
def dashboard_page_with_state(page_with_state:DashboardPage) -> Page:
    return DashboardPage(page=page_with_state)

@pytest.fixture
def courses_list_page(page_with_state:CoursesListPage) -> Page:
    return CoursesListPage(page=page_with_state)

@pytest.fixture
def create_course_page(page_with_state:CreateCoursePage) -> Page:
    return CreateCoursePage(page=page_with_state)

