"""
Test registration
"""

import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.registration           # ┐ Pytest Markers
@pytest.mark.regression             # ┘
@pytest.mark.parametrize(           # ] Pytest Parametrize
    'email, username, password', [
        ('user.name@gmail.com','username', 'password')
    ])
def test_successful_registration(               # Принимает:
        registration_page: RegistrationPage,    # Фикстура registration_page
        dashboard_page: DashboardPage,          # Фикстура dashboard_page (for URL expect only)
        email: str,                             # email     ┐
        username: str,                          # username  │ из parametrize
        password: str                           # password  ┘
):
    # ⿹ Open page
    registration_page.visit(registration_page.url)

    # ✔️EXPECTATIONS (before actions)
    registration_page.check_header()
    registration_page.check_login_link()

    # ▶ ACTIONS
    registration_page.fill_registration_form(
        email=email,
        username=username,
        password=password
    )
    registration_page.click_registration_btn()

    # ✔️EXPECTATIONS (after actions)
    registration_page.check_new_page_url_after_successful_registration(dashboard_page.url)
    dashboard_page.check_navbar(username)   # ex: Welcome, John!


    # ⏳(optional)
    registration_page.page.wait_for_timeout(2_000)
#=======================================================================================================================
