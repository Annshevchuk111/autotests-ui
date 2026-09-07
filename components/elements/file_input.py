from components.elements.base_element import BaseElement
from playwright.sync_api import expect

class FileInput(BaseElement):
    def set_input_files(self,file:str,**kwargs):
        locator=self.get_locator(**kwargs)
        locator.set_input_file(file)