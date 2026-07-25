"""
Chromium page fixtures
"""
import pytest
from playwright.sync_api import sync_playwright, Page

#=======================================================================================================================
# Chromium Page
@pytest.fixture
def chromium_page() -> Page:
    with sync_playwright() as playwright:             # Создаем объект playwright = sync_playwright() (инициализация)
        browser = playwright.chromium.launch(         # Создаем объект браузера на движке chromium c параметрами:
            headless=False,                           # - False — показывать браузер
            slow_mo=500                               # - Action delay (ms)
        )
        page = browser.new_page()                     # Создаем объект страницы page на базе browser
        yield page                                    # Page (на базе движка chromium)


#=======================================================================================================================
