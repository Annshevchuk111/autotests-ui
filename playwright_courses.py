from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state_for_courses.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state_for_courses.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    header_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(header_courses).to_have_text('Courses')

    text_block = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(text_block).to_have_text('There is no results')

    text_block_child = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_block_child).to_have_text('Results from the load test pipeline will be displayed here')

    icon_block = page.get_by_test_id('courses-list-empty-view-icon').locator('path')
    expect(icon_block).to_have_attribute('d','M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2m0 12H4V8h16z')
    # expect(icon_block).to_be_visible()
    page.wait_for_timeout(5000)