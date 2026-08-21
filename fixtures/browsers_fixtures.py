"""
Browsers fixtures
"""
import pytest
from playwright.sync_api import Playwright, StorageState, ViewportSize
from pages.auth.regustration.registration_page import RegistrationPage

#=======================================================================================================================
# Chromium Page + Storage state 📦
@pytest.fixture
def page(storage_state: StorageState, playwright: Playwright): # Используем фикстуру storage_state с авторизацией + встроенную фикстуру playwright из pytest_playwright plugin
    """
    Fixture for authorized user (registered)

    :param storage_state: Фикстура с сохраненными авторизационными данными
    :param playwright: Playwright
    :return: yield page: Page
    """
    browser = playwright.chromium.launch(                 # Создаем объект браузера на движке chromium c параметрами:
        channel='chromium',                               # - UI оболочка: 'chromium', 'chrome', 'msedge'
        headless=True,                                    # - True/False — НЕ/Показывать браузер
        slow_mo=None)                                     # - Action delay (ms)
    context = browser.new_context(                        # Создание браузерного окружения с Storage state:
        storage_state=storage_state,               # ┐    # - Storage state из фикстуры
        # storage_state='storage_state.json',      # ┘    # - Storage state из JSON-файла (optional)
        locale='en-US',                                   # - Website language (locale)
        viewport=ViewportSize(width=1100, height=1200))   # - Window size
    page = context.new_page()   # Создаем объект страницы page на базе context

    try:
        yield page              # Передаем page (на базе движка chromium)

    finally:                    # Гарантия закрытия, если упадет.
        context.close()         # Закрываем context!
        browser.close()         # Закрываем browser!


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

    # ─────────── User Registration ──────────┐
    registration_page = RegistrationPage(page)  # Инициализация страницы в переменную
    registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.form.fill(
        email='user.name@gmail.com',
        username='username',
        password='password')
    registration_page.click_registration_btn()
    page.wait_for_url('**/dashboard')           # ❗️Дождаться открытие страницы, что бы гарантировано сформировался Storage state
    # ────────────────────────────────────────┘

    storage_state = context.storage_state()                             # v.1 - Storage state в переменную
    # context.storage_state(path='storage_state.json')                  # v.2 - Storage state в 💾JSON-файл  (optional)
    # storage_state = context.storage_state(path='storage_state.json')  # v.3 - Storage state в переменную + 💾JSON-файл  (optional)

    try:
        yield storage_state          # Передаем Storage state

    finally:                         # Гарантия закрытия, если упадет.
        context.close()              # Закрываем context!
        browser.close()              # Закрываем browser!


#-----------------------------------------------------------------------------------------------------------------------
# GUEST Page (NO Storage state)
@pytest.fixture
def page_guest(playwright: Playwright):   # Чистый (без доп. фикстур)
    """
    Fixture for GUEST user (unregister)

    :param playwright: Playwright
    :return: yield page: Page
    """
    browser = playwright.chromium.launch(                 # Создаем объект браузера на движке chromium c параметрами:
        channel='chromium',                               # - UI оболочка: 'chromium', 'chrome', 'opera'
        headless=True,                                    # - True/False — НЕ/Показывать браузер
        slow_mo=None)                                     # - Action delay (ms)
    context = browser.new_context(                        # Создание браузерного окружения (NO Storage state):
        locale='en-US',                                   # - Website language (locale)
        viewport=ViewportSize(width=1100, height=1200))   # - Window size
    page = context.new_page()        # Создаем объект page на базе context

    try:
        yield page                   # Передаем page (на базе context)

    finally:                         # Гарантия закрытия, если упадет.
        context.close()              # Закрываем context!
        browser.close()              # Закрываем browser!

#=======================================================================================================================
