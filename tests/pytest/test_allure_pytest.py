import allure

@allure.step('Opening browser')
def open_browser():
    with allure.step('Preparing browser'):
        ...
    with allure.step('Get browser starting'):
        ...



@allure.step('Check course {title}')
def check_course(title:str):
    ...
@allure.step('Close browser')
def close_browser():
    ...

def test_feature():
    open_browser()
    check_course(title='Playwright')
    check_course(title='Exel')
    check_course(title='SQL')
    close_browser()