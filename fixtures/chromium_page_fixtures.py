"""
Chromium page fixtures
"""
import pytest
from playwright.sync_api import Playwright

#=======================================================================================================================
# Chromium Page (via pytest_playwright plugin)
@pytest.fixture
def chromium_page(playwright: Playwright):        # Используем встроенную фикстуру playwright из pytest_playwright plugin
    browser = playwright.chromium.launch(         # Создаем объект браузера на движке chromium c параметрами:
        headless=False,                           # - False — показывать браузер
        slow_mo=500                               # - Action delay (ms)
    )
    page = browser.new_page()                     # Создаем объект страницы page на базе browser
    yield page                                    # Page (на базе движка chromium)
    browser.close()                               # Закрываем браузер!


#=======================================================================================================================
