"""
Test (negative)
Courses page is not opening without auth
"""

from playwright.sync_api import expect
import pytest
#=======================================================================================================================
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.negative
def test_courses_page_is_not_opening_without_auth(guest_page):
    page = guest_page

    # ⿹ Open page
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    # ✔️EXPECTATIONS
    expect(page, '❌ Courses page is opening without auth!').to_have_url(login_page) # Courses page - не открыввется —> Redirect на Login page (Auth)

    # ⏳(optional)
    page.wait_for_timeout(1000)
#=======================================================================================================================
