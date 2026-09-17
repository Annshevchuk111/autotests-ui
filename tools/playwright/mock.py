from playwright.sync_api import Playwright, Page, Route

def abort(route: Route):
    print(f'\nAborting: {route.request.url}')

def mock_static_resources (page: Page):
    page.route("**/*.{ico,png,jpg,webp,mp3,mp4,woff,woff2}",abort)