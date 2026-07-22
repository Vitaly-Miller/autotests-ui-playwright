"""
Playwright Registration
"""
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                        # Переменная playwright = sync_playwright() (инициализация)
    chromium = playwright.chromium.launch(headless=False)    # Переменная браузера chromium c запуском браузера (с отображением)
    page = chromium.new_page()                               # Переменная страницы page c запуском новой страницы

    # Open page
    page.goto(login_url)                                        # ▶ ACTION - Переход на страницу по URL

    # ㉧ LOCATORS
    login_btn = page.get_by_test_id('login-page-login-button')  # ㉧ LOCATOR кнопки Login

    # ✔︎ EXPECTATIONS
    expect(login_btn).to_be_disabled()                          # Login button is disable

    page.wait_for_timeout(1000)                                 # ⏳


#=======================================================================================================================
