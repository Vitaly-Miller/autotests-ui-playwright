"""
Test login (Negative)
"""
import allure
import pytest
from allure_commons.types import Severity

from pages.auth.login.login_page import LoginPage
from tools.allure.annotations import Epic, Feature, Story, Tag

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
    @pytest.mark.parametrize(
        'email, password', [
            ('user.name@gmail.com', 'password'),
            ('user.name@gmail.com', '  '),
            ('  ', 'password')
        ])
    def test_login_with_wrong_email_or_password(
            self,
            login_page: LoginPage,
            email: str,
            password: str
    ):
        # ⿹ Open page
        login_page.open(login_page.URL)

        # ✔️EXPECTATIONS (Before fill Login form)
        login_page.check()

        # ▶ ACTIONS
        login_page.form.fill(email=email, password=password)
        login_page.click_login_btn()

        # ✔️EXPECTATIONS
        login_page.check_alert()


#=======================================================================================================================
