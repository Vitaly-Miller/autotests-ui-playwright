"""
Test login
"""

import pytest
from pages.auth.login.login_page import LoginPage
from pages.auth.regustration.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.auth              # ┐
@pytest.mark.login             # │ Pytest Markers
@pytest.mark.regression        # ┘
class TestLogin:
    @pytest.mark.e2e
    def test_login(self, login_page: LoginPage):
        # User data
        email = 'user.name@gmail.com'
        username = 'username'
        password = 'password'

        # Pages initialization
        registration_page = RegistrationPage(login_page.page)
        dashboard_page = DashboardPage(login_page.page)

        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴ Precondition ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
        # New user registration
        registration_page.visit(registration_page.URL)                            # ⿹ Open page
        registration_page.form.fill_registration_form(email, username, password)  # ▶︎ Fill registration form
        registration_page.click_registration_btn()                                # ▶︎ Click registration button
        dashboard_page.sidebar.click_logout()                                     # ▶︎ Click Sidebar Logout item
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

        # ⿹ Open page (не требуется - т.к. уже на странице)
        # login_page.visit(login_page.URL)

        # ▶ ACTIONS
        login_page.form.fill_login_form(email=email, password=password)
        login_page.click_login_btn()

        # ✔ Expectations
        login_page.check_current_url(dashboard_page.URL)


@pytest.mark.auth              # ┐
@pytest.mark.login             # │ Pytest Markers
@pytest.mark.regression        # │
@pytest.mark.negative          # ┘
class TestLoginNegative:
    @pytest.mark.parametrize(  # ] Pytest Parametrize
        'email, password', [                                    # Параметризация Email и Password (3-in-1):
            ('user.name@gmail.com', 'password'),  # - Valid (unregistered user)
            ('user.name@gmail.com', '  '),        # - Invalid password
            ('  ', 'password')                    # - Invalid email
        ])
    def test_login_with_wrong_email_or_password_negative(
            self,
            login_page: LoginPage,    # Принимает фикстуру login_page
            email: str,               # Принимает email     ┐ из parametrize
            password: str             # Принимает password  ┘
    ):
        # ⿹ Open page
        login_page.visit(login_page.URL)

        # ✔️EXPECTATIONS (Before fill Login form)
        login_page.check_page()

        # ▶ ACTIONS
        login_page.form.fill_login_form(email=email, password=password)
        login_page.click_login_btn()

        # ✔️EXPECTATIONS
        login_page.check_wrong_email_or_password_alert()

#=======================================================================================================================
