from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.navigation.navbar_component import NavBarComponent
from components.navigation.sidebar_component import SideBarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent

class DashboardPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.navbar = NavBarComponent(page)
        self.sidebar = SideBarComponent(page)
        self.dashboard = DashboardToolbarViewComponent(page)
        self.students_chart = ChartViewComponent(page,'students','bar')
        self.activities_chart = ChartViewComponent(page, 'activities', 'line')
        self.courses_chart = ChartViewComponent(page, 'courses', 'pie')
        self.scores_chart = ChartViewComponent(page, 'scores', 'scatter')



        # self.students_title = page.get_by_test_id('students-widget-title-text')
        # self.students_chart = page.get_by_test_id('students-bar-chart')
        # self.activities_title = page.get_by_test_id('activities-widget-title-text')
        # self.activities_chart = page.get_by_test_id('activities-line-chart')
        # self.courses_title = page.get_by_test_id('courses-widget-title-text')
        # self.courses_chart = page.get_by_test_id('courses-pie-chart')
        # self.scores_title =  page.get_by_test_id('scores-widget-title-text')
        # self.scores_chart = page.get_by_test_id('scores-scatter-chart')




    # def check_students_widget(self):
    #     expect(self.students_title).to_be_visible()
    #     expect(self.students_title).to_have_text('Students')
    #     expect(self.students_chart).to_be_visible()
    #
    # def check_activities_widget(self):
    #     expect(self.activities_title).to_be_visible()
    #     expect(self.activities_title).to_have_text('Activities')
    #     expect(self.activities_title).to_be_visible()
    #
    #
    # def check_courses_widget(self):
    #     expect(self.courses_title).to_be_visible()
    #     expect(self.courses_title).to_have_text('Courses')
    #     expect(self.courses_chart).to_be_visible()
    #
    # def check_scores_widget(self):
    #     expect(self.scores_title).to_be_visible()
    #     expect(self.scores_title).to_have_text('Scores')
    #     expect(self.scores_chart).to_be_visible()

