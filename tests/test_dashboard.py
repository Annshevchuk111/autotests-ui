from pages.dashboard_page import DashboardPage
import pytest

@pytest.mark.dashboard
@pytest.mark.registration
def test_dashboard_displaying(dashboard_page_with_state:DashboardPage):
    dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard ')
    dashboard_page_with_state.navbar.check_visible('username')
    dashboard_page_with_state.check_dashboard_title()
    dashboard_page_with_state.check_students_widget()
    dashboard_page_with_state.check_activities_widget()
    dashboard_page_with_state.check_courses_widget()
    dashboard_page_with_state.check_scores_widget()

    dashboard_page_with_state.sidebar.check_visible()