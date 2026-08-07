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
        email: str,                             # email     ┐
        username: str,                          # username  │ из parametrize
        password: str                           # password  ┘
):
    # ⿹ Open page
    registration_page.visit(registration_page.URL)

    # ✔️EXPECTATIONS (before actions) - optional
    registration_page.check_toolbar_title()
    registration_page.check_login_link()
    registration_page.check_registration_btn_disable()

    # ▶ ACTIONS
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_btn()

    # ✔️EXPECTATIONS (after actions)
    registration_page.check_current_url(DashboardPage.URL)



    # ⏳(optional)
    registration_page.wait()

#=======================================================================================================================
