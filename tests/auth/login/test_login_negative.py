"""
Test login (Negative)
"""

import pytest
import allure
from allure_commons.types import Severity
from tools.allure.annotations import Epic, Feature, Story, Tag
from pages.auth.login.login_page import LoginPage

#=======================================================================================================================
@pytest.mark.auth
@pytest.mark.login
@pytest.mark.regression
@pytest.mark.negative
@allure.severity(Severity.CRITICAL)
@allure.tag(Tag.AUTH, Tag.LOGIN, Tag.REGRESSION, Tag.NEGATIVE)
@allure.epic(Epic.AUTH)
@allure.feature(Feature.LOGIN)
@allure.story(Story.LOGIN_NEGATIVE)
class TestLoginNegative:
    @allure.title('Login with wrong email or password:')
    @pytest.mark.parametrize(                                   # ] Pytest Parametrize
        'email, password', [                                    # Параметризация Email и Password (3-in-1):
            ('user.name@gmail.com', 'password'),  # 1 - Valid credentials (but unregistered user)
            ('user.name@gmail.com', '  '),        # 2 - Invalid password
            ('  ', 'password')                    # 3 - Invalid email
        ])
    def test_login_with_wrong_email_or_password(                # Принимает:
            self,
            login_page: LoginPage,                              # - Фикстура login_page
            email: str,                                         # - email - from parameterize
            password: str                                       # - password - from parameterize
    ):
        # ⿹ Open page
        login_page.open(login_page.URL)

        # ✔️EXPECTATIONS (Before fill Login form)
        login_page.check()

        # ▶ ACTIONS
        login_page.form.fill(email=email, password=password)
        login_page.click_login_btn()

        # ✔️EXPECTATIONS
        login_page.check_wrong_email_or_password_alert()

#=======================================================================================================================
