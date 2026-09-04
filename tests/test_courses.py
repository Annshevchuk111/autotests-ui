import pytest
from _testcapi import awaitType
from playwright.sync_api import sync_playwright,expect, Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page:CoursesListPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible('username')


    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context()
    #
    #     page = context.new_page()
    #
    #     page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    #
    #     email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    #     email_input.fill('user.name@gmail.com')
    #
    #     username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    #     username_input.fill('username')
    #
    #     password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    #     password_input.fill('password')
    #
    #     registration_button = page.get_by_test_id('registration-page-registration-button')
    #     registration_button.click()
    #
    #     context.storage_state(path='browser-state_for_courses.json')
    #
    # with sync_playwright() as playwright:
    #     browser = playwright.chromium.launch(headless=False)
    #     context = browser.new_context(storage_state='browser-state_for_courses.json')
    #     page = context.new_page()



        # chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        #
        # header_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        # expect(header_courses).to_have_text('Courses')
        #
        # text_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        # expect(text_block).to_have_text('There is no results')
        #
        # text_block_child = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        # expect(text_block_child).to_have_text('Results from the load test pipeline will be displayed here')
        #
        # icon_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon').locator('path')
        # expect(icon_block).to_have_attribute('d','M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2m0 12H4V8h16z')
        #
        #
        # chromium_page_with_state.wait_for_timeout(5000)

@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page:CoursesListPage,create_course_page:CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()

    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form(
        title='',
        estimated_time='',
        description='',
        max_score='0',
        min_score='0'
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index='0',
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )
