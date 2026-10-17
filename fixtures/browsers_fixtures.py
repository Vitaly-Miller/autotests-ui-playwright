"""
Browsers fixtures
"""
import pytest
from playwright.sync_api import Playwright, StorageState

from config import settings
from tools.playwright.init_page import init_playwright_page
from tools.registration import registration_new_user

#=======================================================================================================================
# Guest page
@pytest.fixture(params=settings.browser)
def page_guest(playwright: Playwright, request: pytest.FixtureRequest):
    """
    Fixture GUEST-Page for authentication (NO Storage state)

    :param playwright: Playwright
    :param request: pytest.FixtureRequest (test name for tracing + request.param for browser parametrization)
    :return: yield from - Page from init_playwright_page() without Storage state
    """
    yield from init_playwright_page(
        playwright=playwright,
        test_name=request.node.name,
        browser_engine=request.param
    )

# Page with Storage state 📦
@pytest.fixture(params=settings.browser)
def page(playwright: Playwright, request: pytest.FixtureRequest, storage_state: StorageState):
    """
    Fixture Page + Storage state for authorized user (registered)

    :param playwright: Playwright
    :param storage_state: Fixture with saved authorization data
    :param request: pytest.FixtureRequest (test name for tracing + request.param for browser parametrization)
    :return: yield from - Page from init_playwright_page() with Storage state
    """
    yield from init_playwright_page(
        playwright=playwright,
        test_name=request.node.name,
        storage_state=storage_state,
        browser_engine=request.param
    )

#-----------------------------------------------------------------------------------------------------------------------
# Storage state 📦
@pytest.fixture(scope='session')
def storage_state(playwright: Playwright):
    """
    Internal-use fixture for that stores storage_state with authorization data

    :param playwright: Playwright
    :return: yield - StorageState / storage_state.json
    """
    browser = playwright.chromium.launch()
    context = browser.new_context(base_url=settings.base_url)
    page = context.new_page()
    registration_new_user(page)
    page.wait_for_function(                        # ❗Waiting for the user, otherwise the Storage state will be empty.
        expression='email => localStorage.getItem("persist:users")?.includes(email)',
        arg=settings.test_user.email
    )
    storage_state = context.storage_state()                               # v.1 - to Variable
    # context.storage_state(path=Dir.STORAGE_STATE_FILE)                  # v.2 - to 💾 JSON-file (optional)
    # storage_state = context.storage_state(path=Dir.STORAGE_STATE_FILE)  # v.3 - to Variable + 💾 JSON-file  (optional)
    try:
        yield storage_state

    finally:
        context.close()
        browser.close()


#-------------------------------------------------------- OPTIONAL -----------------------------------------------------
# Custom selector (NOT USING)
# @pytest.fixture(scope='session', autouse=True)
# def selector_id_attribute(playwright: Playwright):
#     """
#     Custom selector identification
#
#     Use if not default in the DOM <data-testid='...'>
#
#     :param playwright: Playwright
#     """
#     playwright.selectors.set_test_id_attribute('qa-id')  # for example
#=======================================================================================================================
