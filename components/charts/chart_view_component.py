from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.elements.text import Text
from components.elements.image import Image



class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page,identifier:str,chart_type:str):
        super().__init__(page)

        self.title = Text(page,f'{identifier}-widget-title-text','Chart Title')
        self.chart = Image(page,f'{identifier}-{chart_type}-chart','Chart Image')

    def check_visible(self,identifier:str):
        self.title.check_visible()
        self.title.check_have_text(identifier)
        self.chart.check_visible()
