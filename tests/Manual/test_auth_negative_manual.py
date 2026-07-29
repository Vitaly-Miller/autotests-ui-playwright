"""
Test (negative)
Auth unregister user (Login)
"""

import pytest
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

@pytest.mark.auth
@pytest.mark.regression
@pytest.mark.negative
def test_auth_unregister_user():
    #------------------------------------------------ Playwright setup -------------------------------------------------
    # Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
    with sync_playwright() as playwright:             # Создаем объект playwright = sync_playwright() (инициализация)
        browser = playwright.chromium.launch(         # Создаем объект браузера на движке chromium c  параметрами:
            headless=False,                           # - False — показывать браузер
            slow_mo=500                               # - Action delay (ms)
        )
        page = browser.new_page()                     # Создаем объект страницы page

        #---------------------------------------------------------------------------------------------------------------
        # ⿹ Open page
        page.goto(login_url)                          # ▶ ACTION - Переход на страницу по URL

        # ㉧ LOCATORS
        email_field = page.get_by_label('Email')                                             # by label
        email_field_ = page.locator('label:has-text("Email")')                               # by label has text
        email_field__ = page.locator('//div[@data-testid="login-form-email-input"]//input')  # by XPath
        email_field___ = page.get_by_test_id('login-form-email-input').locator('input')      # by test id + locator
        password_field = page.get_by_label('Password')                                       # by label
        login_btn = page.get_by_test_id('login-page-login-button')                           # by test id
        login_btn_ = page.get_by_role(role='button', name='Login')                           # by role
        error_message = page.get_by_test_id('login-page-wrong-email-or-password-alert')      # by test id
        error_message_ = page.get_by_text('Wrong email or password')                         # by text

        # ▶ ACTIONS
        email_field.fill('user.name@gmail.com')       # Fill field
        password_field.fill('password')               # Fill field
        login_btn.click()                             # Click button

        # ✔️EXPECTATIONS
        expect(error_message, '❌ Error message did not appear!').to_be_visible()                         # Проверка видимости сообщения об ошибке
        expect(error_message, '❌ Wrong Error message text!').to_have_text('Wrong email or password')     # Проверка текста сообщения об ошибке

        # ⏳(optional)
        page.wait_for_timeout(1000)


#=======================================================================================================================
