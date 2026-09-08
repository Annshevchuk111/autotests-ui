import re

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from components.elements.button import Button
from components.elements.link import Link



class  RegistrationPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = Button(page,"registration-page-registration-button",'Registration button')
        self.login_button_link = Link(page,"registration-page-login-link",'Login link')


    def click_registration_button(self):
        self.registration_button.click()

    def click_login_button(self):
        self.login_button_link.click()
        self.check_current_url(re.compile('.*#/auth/login') )



