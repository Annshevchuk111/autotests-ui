from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.elements.button import Button
from components.elements.text import Text
import allure

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.create_course_title = Text(page,'create-course-toolbar-title-text','Title')
        self.create_course_button = Button(page,'create-course-toolbar-create-course-button','Button')

    @allure.step('Check visible "Create course" toolbar')
    def check_visible_create_course_title(self):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

    @allure.step('Check visible  button for creating course')
    def check_visible(self,is_create_course_disabled=True):
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        if not is_create_course_disabled:
            self.create_course_button.check_enabled()


    def click_create_course_button(self):
        self.create_course_button.click()