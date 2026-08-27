"""
Playwright Auth
"""
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                        # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(headless=False)    # Создаем объект браузера chromium c запуском браузера (с отображением)
    page = browser.new_page()                               # Создаем объект страницы page c запуском новой страницы

    # ⿹ Open page
    page.goto(login_url)                                                 # ▶ ACTION - Переход на страницу по URL

    # Email field
    email_field_locator = page.get_by_label('Email')                                            # ㉧ LOCATOR поля ввода Email  (v.1 - by label)
    email_field_locator_ = page.locator('label:has-text("Email")')                              # ㉧ LOCATOR поля ввода Email  (v.2)
    email_field_locator__ = page.locator('//div[@data-testid="login-form-email-input"]//input') # ㉧ LOCATOR поля ввода Email  (v.3 - by XPath)
    email_field_locator___ = page.get_by_test_id('login-form-email-input').locator('input')     # ㉧ LOCATOR поля ввода Email  (v.4 - by test id + locator)
    email_field_locator.fill('user.name@gmail.com')                                             # ▶ ACTION - fill email field

    # Password field
    password_field_locator = page.get_by_label('Password')                 # ㉧ LOCATOR поля ввода Password  (by label)
    password_field_locator.fill('password')                                # ▶ ACTION - fill password field

    # Login button
    login_btn_locator = page.get_by_test_id('login-page-login-button')     # ㉧ LOCATOR кнопки Login (v.1 - by test_id)
    login_btn_locator_ = page.get_by_role('button', name='Login')     # ㉧ LOCATOR кнопки Login (v.2 - by role)
    login_btn_locator.click()                                              # ▶ ACTION - click button

    # Error message
    error_message_locator = page.get_by_test_id('login-page-wrong-email-or-password-alert')  # ㉧ LOCATOR сообщения об ошибке при неверном вводе (v.1 - by test id)
    error_message_locator_ = page.get_by_text('Wrong email or password')                     # ㉧ LOCATOR сообщения об ошибке при неверном вводе (v.2 - by text)

    # ✔︎ EXPECTATIONS
    expect(error_message_locator).to_be_visible()                          # Проверка видимости сообщения об ошибке
    expect(error_message_locator).to_have_text('Wrong email or password')  # Проверка текста сообщения об ошибке

    # ⏳
    page.wait_for_timeout(1000)
#=======================================================================================================================
