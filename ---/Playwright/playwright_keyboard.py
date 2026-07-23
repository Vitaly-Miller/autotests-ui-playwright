"""
Playwright Keyboard
"""
from playwright.sync_api import sync_playwright

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                       # Создаем объект playwright = sync_playwright() (инициализация)
    chromium = playwright.chromium.launch(headless=False)   # Создаем объект браузера chromium c запуском браузера (с отображением)
    page = chromium.new_page()                              # Создаем объект страницы page c запуском новой страницы

    # Open page
    page.goto(login_url)                                    # ▶ ACTION - Переход на страницу по URL

    # Email field
    email_field = page.get_by_label('Email')                # ㉧ LOCATOR
    email_field.click()                                     # v.1 ▶ ACTION - Click по объекту
    email_field.focus()                                     # v.2 ▶ ACTION - Фокус на объекте

    # Fill out
    page.keyboard.type('keyboard.type', delay=50)      # ▶ ACTION - Печатает текст. Задержка 50 ms между символами
    page.wait_for_timeout(1000)                             # ⏳

    # Выделить всё
    page.keyboard.press('ControlOrMeta+A')                  # ▶ ACTION - press <Command+A> (macOS)
    page.wait_for_timeout(2000)                             # ⏳


#=======================================================================================================================
