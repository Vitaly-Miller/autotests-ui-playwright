"""
Test authorization (Login) with Parametrize (3-in-1)
"""

import pytest
from pages.login_page import LoginPage

#=======================================================================================================================
@pytest.mark.auth                 # ┐
@pytest.mark.regression           # │ Pytest Markers
@pytest.mark.negative             # ┘
@pytest.mark.parametrize(         # ] Pytest Parametrize
    'email, password', [                                      # Параметризация Email и Password (3-in-1):
        ('user.name@gmail.com', 'password'),    # - Valid (unregistered)
        ('user.name@gmail.com', '  '),          # - Invalid password
        ('  ', 'password')                      # - Invalid email
    ])
def test_login_with_wrong_email_or_password(
        login_page: LoginPage,                                # Принимает фикстуру login_page
        email: str,                                           # Принимает email     ┐ из parametrize
        password: str                                         # Принимает password  ┘
):
    # ⿹ Open page
    login_page.visit(login_page.URL)

    # ▶ ACTIONS
    login_page.fill_login_form(email=email, password=password)
    login_page.click_login_btn()

    # ✔️EXPECTATIONS
    login_page.check_wrong_email_or_password_alert_visible()
    login_page.check_wrong_email_or_password_alert_text()



#=======================================================================================================================
