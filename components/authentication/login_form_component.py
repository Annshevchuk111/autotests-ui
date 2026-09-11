from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.elements.input import Input
import allure

class LoginFormComponent(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.email_input= Input(page,"login-form-email-input",'Login')
        self.password_input = Input(page, "login-form-password-input", 'Password')


    @allure.step('Fill login form')
    def fill_login_form(self, email:str,password:str):
        self.email_input.check_visible()
        self.email_input.fill(email)
        self.password_input.check_visible()
        self.password_input.fill(password)

    @allure.step('Check visible login form with filled email and password')
    def check_visible(self,email:str,password:str):
       self.email_input.check_have_value(email)
       self.password_input.check_have_value(password)
