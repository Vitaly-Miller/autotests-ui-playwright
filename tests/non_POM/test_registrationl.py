"""
Test
Registration successful
"""
import pytest
from playwright.sync_api import expect

#=======================================================================================================================
registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
dashboard_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

@pytest.mark.registration
@pytest.mark.regression
def test_registration_successful(guest_page):
    page = guest_page

    # Open page
    page.goto(registration_url)

    # ㉧ LOCATORS
    email_field = page.get_by_role(role='textbox', name='Email')
    username_field = page.get_by_role(role='textbox', name='Username')
    password_field = page.get_by_role(role='textbox', name='Password')
    registration_btn = page.get_by_role(role='button', name='Registration')
    dashboard_header = page.get_by_role(role='heading', name='Dashboard')
    navbar_header = page.get_by_test_id('navigation-navbar-app-title-text')
    navbar_welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')

    # ✔️EXPECTATIONS (before filling out)
    expect(registration_btn).to_be_disabled()       # v.1 - Button is disabled    (by default)
    expect(registration_btn).not_to_be_enabled()    # v.2 - Button is NOT enabled (by default)                           <— ⚠️ анти-паттерн (двойное отрицание)

    # ▶ ACTIONS (filling out)
    email_field.fill('user.name@gmail.com')         # Fill field
    username_field.fill('username')                 # Fill field
    password_field.fill('password')                 # Fill field

    # ✔️EXPECTATIONS (after filling out)
    expect(registration_btn).to_be_enabled()        # v.1 - Button is enable       (after filling out)
    expect(registration_btn).not_to_be_disabled()   # v.2 - Button is NOT disabled (after filling out)                   <— ⚠️ анти-паттерн (двойное отрицание)

    # ▶ ACTIONS (after filling out)
    registration_btn.click()                        # Click button

    # ✔️EXPECTATIONS (after click registration button)
    expect(page, '❌ Wrong page URL').to_have_url(dashboard_url)                                    # Check Page URL
    expect(navbar_header, '❌ Wrong Navbar header text').to_have_text('UI Course')                  # Check Navbar header text
    expect(navbar_welcome_title, '❌ Wrong Check Navbar welcome text').to_contain_text('Welcome,')  # Check Navbar welcome text contains "Welcome,"
    expect(dashboard_header, '❌ Wrong Dashboard header text').to_have_text('Dashboard')            # Check Dashboard header text

    # ⏳(optional)
    page.wait_for_timeout(1000)


#=======================================================================================================================
