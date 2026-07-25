"""
Test (negative)
Courses page is not opening without auth
"""

from playwright.sync_api import Page, sync_playwright, expect
import pytest
#=======================================================================================================================
registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.negative
def test_courses_page_is_not_opening_without_auth(chromium_page: Page):
    page = chromium_page
    #------------------------------------ ◁ PRECONDITION (Auth + storage_state) ------------------------------------
    # Open page
    page.goto(registration_url)

    # ㉧ LOCATORS
    email_field = page.get_by_role(role='textbox', name='Email')
    username_field = page.get_by_role(role='textbox', name='Username')
    password_field = page.get_by_role(role='textbox', name='Password')
    registration_btn = page.get_by_role(role='button', name='Registration')

    # ▶ ACTIONS
    email_field.fill('user.name@gmail.com')
    username_field.fill('username')
    password_field.fill('password')
    registration_btn.click()

    # НЕ Сохраняем Storage state после регистрации

    #-------------------------------------------------------------------------------------------------------------------
    # page.goto(courses_url)
    #
    # # ✔️EXPECTATIONS
    # expect(page, '❌ Courses page is opening without auth!').to_have_url(login_page) # Courses page - не открыввется —> Redirect на Login page (Auth)

    # ⏳(optional)
    page.wait_for_timeout(1000)
#=======================================================================================================================
