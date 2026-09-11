from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.elements.button import Button
import allure

class CourseViewMenuComponent(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.menu_button = Button(page,'course-view-menu-button', 'Menu')
        self.edit_menu_button = Button(page,'course-view-edit-menu-item','Edit')
        self.delete_menu_button = Button(page,'course-view-delete-menu-item','Delete')

    @allure.step('Click menu of course with index {index} and click edit')
    def edit_button(self,index:str):

        self.menu_button.click(int=index)
        self.edit_menu_button.check_visible(int=index)
        self.edit_menu_button.click(int=index)

    @allure.step('Click menu of course with index {index} and click delete')
    def delete_button(self, index: str):
        self.menu_button.click(int=index)
        self.delete_menu_button.check_visible(int=index)
        self.delete_menu_button.click(int=index)