"""
Test registration
"""

import pytest

from pages.auth.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.auth.regustration.registration_page import RegistrationPage

#=======================================================================================================================
@pytest.mark.auth                    # ┐
@pytest.mark.registration            # │ Pytest Markers
@pytest.mark.regression              # ┘
class TestRegistration:
    @pytest.mark.parametrize(        # ] Pytest Parametrize
        'email, username, password', [
            ('user.name@gmail.com','username', 'password')
        ])
    def test_registration(               # Принимает:
            self,
            registration_page: RegistrationPage,    # Фикстура registration_page
            email: str,                             # email     ┐
            username: str,                          # username  │ из parametrize
            password: str                           # password  ┘
    ):
        # ⿹ Open page
        registration_page.visit(registration_page.URL)

        # ✔️PRE-EXPECTATIONS (Before actions)
        registration_page.check_page()

        # ▶ ACTIONS
        registration_page.form.fill_registration_form(email=email, username=username, password=password)
        registration_page.click_registration_btn()

        # ✔️EXPECTATIONS
        registration_page.check_current_url(DashboardPage.URL)

        # ⏳(optional)
        registration_page.wait()


    def test_login_link_redirect(
            self,
            registration_page: RegistrationPage,
            login_page: LoginPage
    ):
        # ⿹ Open page
        registration_page.visit(registration_page.URL)

        # ✔️PRE-EXPECTATIONS (Before actions)
        registration_page.check_login_link()

        # ▶ ACTIONS
        registration_page.click_login_link()

        # ✔️EXPECTATIONS
        registration_page.check_login_link_redirect()
        login_page.check_page(email='', password='')

        # ⏳(optional)
        registration_page.wait()

#=======================================================================================================================
