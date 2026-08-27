"""
Test (negative)
Auth unregister user (Login)
"""

import pytest
from playwright.sync_api import expect

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

@pytest.mark.auth
@pytest.mark.regression
@pytest.mark.negative
def test_auth_unregistered_user(guest_page):
    page = guest_page                             # Сохраняем работу фикстуры

    # ⿹ Open page
    page.goto(login_url)                          # ▶ ACTION - Переход на страницу по URL

    # ㉧ LOCATORS
    email_field_locator = page.get_by_label('Email')                                             # by label
    password_field_locator = page.get_by_label('Password')                                       # by label
    login_btn_locator = page.get_by_test_id('login-page-login-button')                           # by test id
    error_message_locator = page.get_by_test_id('login-page-wrong-email-or-password-alert')      # by test id


    # ▶ ACTIONS
    email_field_locator.fill('user.name@gmail.com')       # Fill field
    password_field_locator.fill('password')               # Fill field
    login_btn_locator.click()                             # Click button

    # ✔️EXPECTATIONS
    expect(error_message_locator, '❌ Error message did not appear!').to_be_visible()                         # Проверка видимости сообщения об ошибке
    expect(error_message_locator, '❌ Wrong Error message text!').to_have_text('Wrong email or password')     # Проверка текста сообщения об ошибке

    # ⏳(optional)
    page.wait_for_timeout(1000)


#=======================================================================================================================
