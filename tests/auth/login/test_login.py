"""
Test login
"""

import pytest
from pages.auth.login.login_page import LoginPage

#=======================================================================================================================
@pytest.mark.auth              # ┐
@pytest.mark.login             # │ Pytest Markers
@pytest.mark.regression        # ┘
class TestLogin:
    ...



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
        login_page.form.fill_form(email=email, password=password)
        login_page.click_login_btn()

        # ✔️EXPECTATIONS
        login_page.check_wrong_email_or_password_alert()

#=======================================================================================================================
