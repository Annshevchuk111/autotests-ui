import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SideBarListItemComponent
import re

class SideBarComponent(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.logout_list_item = SideBarListItemComponent(page, 'logout')
        self.courses_list_item = SideBarListItemComponent(page, 'courses')
        self.dashboard_list_item = SideBarListItemComponent(page, 'dashboard')

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.check_navigate(re.compile(r'.*/#/auth/login'))

    @allure.step('Click Courses on sidebar')
    def click_courses(self):
        self.courses_list_item.check_navigate(re.compile(r'.*/#/courses'))

    @allure.step('Click Dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.check_navigate(re.compile(r'.*/#/dashboard'))