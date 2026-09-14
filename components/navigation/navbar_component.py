from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.elements.text import Text
import allure

class NavBarComponent(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.app_title = Text(page,'navigation-navbar-app-title-text','App Title')
        self.welcome_title = Text(page,'navigation-navbar-welcome-title-text','Welcome Title')

    @allure.step('Check NavBar title and Welcome {username}')
    def check_visible(self, username:str):
        self.app_title.check_visible()
        self.app_title.check_have_text(text='UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f'Welcome, {username}!')
