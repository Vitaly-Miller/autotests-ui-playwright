"""
Playwright
"""
from playwright.sync_api import sync_playwright, expect


#=======================================================================================================================
url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                        # Переменная playwright = sync_playwright() (инициализация)
    chromium = playwright.chromium.launch(headless=False)    # Переменная браузера chromium c запуском браузера (с отображением)
    page = chromium.new_page()                               # Переменная страницы page c запуском страницы

    page.goto(url)                                               # ▶ ACTIONS - Команда перехода на страницу по URL

    email_field = page.locator('label:has-text("Email")')        # ㉧ LOCATOR поля ввода Email
    email_field.fill('user.name@gmail.com')                      # ▶ ACTIONS - Fill Email field

    password_field = page.locator('label:has-text("Password")')  # ㉧ LOCATOR поля ввода Password
    password_field.fill('password')                              # ▶ ACTIONS - Fill Password field

    login_btn = page.get_by_role('button', name='Login')    # ㉧ LOCATOR кнопки Login
    login_btn.click()                                            # ▶ ACTIONS - Click button

    error_message = page.get_by_text('Wrong email or password')  # ㉧ LOCATOR сообщения об ошибке при неверном вводе

    expect(error_message).to_be_visible()                          # ✔︎ EXPECTATIONS - Проверка видимости сообщения об ошибке
    expect(error_message).to_have_text('Wrong email or password')  # ✔︎ EXPECTATIONS - Проверка текста сообщения об ошибке

    page.wait_for_timeout(3000)                              # Timeout в конце   (⚠️ optional, чтоб посмотреть)
    chromium.close()                                         # Закрытие браузера (⚠️ optional, т.к. <with>)


#=======================================================================================================================
