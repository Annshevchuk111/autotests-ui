from playwright.sync_api import sync_playwright, Page, Playwright
import allure
from config import settings
from config import Browser
from tools.playwright.mock import mock_static_resources


def initialize_page(
    playwright:Playwright,
    test_name:str,
    browser_type: Browser,
    storage_state:str | None = None
) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        storage_state=storage_state,
        record_video_dir=settings.videos_dir,
        base_url=settings.get_base_url(),

    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    #mock_static_resources(page) # Закоментила, тк ту падает изза self.page.goto(url, wait_until="networkidle")

    yield page
    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)