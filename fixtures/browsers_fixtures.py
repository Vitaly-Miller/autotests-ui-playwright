"""
Browsers fixtures
"""
import pytest
from playwright.sync_api import Playwright, StorageState
from _pytest.fixtures import SubRequest                         # naming for tracing
from tools.playwright.init_page import init_playwright_page     # helper
from tools.playwright.registration import registration_new_user # helper
from config import settings

#=======================================================================================================================
# GUEST page
@pytest.fixture
def page_guest(playwright: Playwright, request: SubRequest):
    """
    Fixture GUEST-Page for authentication (NO Storage state)

    :param playwright: Playwright
    :param request: SubRequest.request (for tracing)
    :return: yield from - Page from init_playwright_page() without Storage state
    """
    yield from init_playwright_page(playwright=playwright, test_name=request.node.name)

# Page + Storage state 📦
@pytest.fixture
def page(playwright: Playwright, request: SubRequest, storage_state: StorageState):
    """
    Fixture Page + Storage state for authorized user (registered)

    :param playwright: Playwright
    :param storage_state: Фикстура с сохраненными авторизационными данными
    :param request: SubRequest.request (naming for tracing)
    :return: yield from - Page from init_playwright_page() with Storage state
    """
    yield from init_playwright_page(playwright=playwright, test_name=request.node.name, storage_state=storage_state)


#-----------------------------------------------------------------------------------------------------------------------
# Storage state 📦
@pytest.fixture(scope='session')                # Выполняется один раз за всю тестовую сессию
def storage_state(playwright: Playwright):      # Используем встроенную фикстуру playwright из pytest_playwright plugin
    """
    Фикстура для внутреннего использования, сохраняющая storage_state c авторизационными данными

    :param playwright: Playwright
    :return: yield - StorageState / storage_state.json
    """
    browser = playwright.chromium.launch()      # Создаем объект браузера на движке chromium c параметрами:
    context = browser.new_context()             # Создание браузерного окружения
    page = context.new_page()                   # Создаем объект страницы page на базе context
    registration_new_user(page)                 # Registration new user (helper)
    storage_state = context.storage_state()     # v.1 - Storage state в переменную
    # context.storage_state(path=settings.storage_state_file)                  # v.2 - Storage state в 💾 JSON-файл  (optional)
    # storage_state = context.storage_state(path=settings.storage_state_file)  # v.3 - Storage state в переменную + 💾 JSON-файл  (optional)
    try:
        yield storage_state                     # Передаем Storage state

    finally:                                    # Гарантия закрытия, если упадет.
        context.close()                         # Закрываем context!
        browser.close()                         # Закрываем browser!


#=======================================================================================================================
