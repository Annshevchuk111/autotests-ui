from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.elements.button import Button

class CourseViewMenuComponent(BaseComponent):
    def __init__(self,page:Page):
        super().__init__(page)

        self.menu_button = Button(page,'course-view-menu-button', 'Menu')
        self.edit_menu_button = Button(page,'course-view-edit-menu-item','Edit')
        self.delete_menu_button = Button(page,'course-view-delete-menu-item','Delete')

    def edit_button(self,index:str):
        self.menu_button.nth(index).click()
        expect(self.edit_menu_button).nth(index).to_be_visible()
        self.edit_menu_button.nth(index).click()

    def delete_button(self, index: str):
        self.menu_button.nth(index).click()
        expect(self.delete_menu_button).nth(index).to_be_visible()
        self.delete_menu_button.nth(index).click()