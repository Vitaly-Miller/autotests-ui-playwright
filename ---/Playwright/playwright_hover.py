"""
Playwright hover - наведение курсора мыши на элемент
"""
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                       # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(headless=False)    # Создаем объект браузера chromium c запуском браузера (с отображением)
    page = browser.new_page()                               # Создаем объект страницы page c запуском новой страницы


    page.goto(login_url)                  # ▶ ACTION - Переход на страницу по URL
    registration_link = page.locator('#login-page-registration-link') # ㉧ LOCATOR

    page.wait_for_timeout(1000)           # ⏳
    registration_link.hover()             # ▶ ACTION - Наведение курсора мыши на элемент
    page.wait_for_timeout(2000)           # ⏳


#=======================================================================================================================
