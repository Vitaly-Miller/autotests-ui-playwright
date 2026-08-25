"""
Test registration
"""

import pytest
import allure
from allure_commons.types import Severity
from pages.dashboard.dashboard_page import DashboardPage
from pages.auth.registration.registration_page import RegistrationPage
from tools.allure.annotations import Epic, Feature, Story, Tag

#=======================================================================================================================
@pytest.mark.auth
@pytest.mark.registration
@pytest.mark.regression
@allure.tag(Tag.AUTH, Tag.REGISTRATION, Tag.REGRESSION)
@allure.epic(Epic.AUTH)
@allure.feature(Feature.REGISTRATION)
class TestRegistration:
    @allure.severity(Severity.BLOCKER)
    @allure.story(Story.REGISTRATION)
    @allure.title('Registration successful')
    def test_registration_successful(self, registration_page: RegistrationPage):
        # 𝌮 User data
        email = 'user.name@gmail.com'
        username = 'username'
        password = 'password'

        # ⿹ Open page
        registration_page.open(registration_page.URL)

        # ✔️PRE-EXPECTATIONS (Before actions)
        registration_page.check()

        # ▶ ACTIONS
        registration_page.form.fill(email=email, username=username, password=password)
        registration_page.click_registration_btn()

        # ✔️EXPECTATIONS
        registration_page.check_current_url(DashboardPage.URL)


    @allure.severity(Severity.NORMAL)
    @allure.tag(Tag.NAVIGATE)
    @allure.story(Story.NAVIGATE)
    @allure.title('Login-link redirect')
    def test_login_link_redirect(self, registration_page: RegistrationPage):
        # ⿹ Open page
        registration_page.open(registration_page.URL)

        # ▶ ACTIONS
        registration_page.click_login_link()

        # ✔️EXPECTATIONS
        registration_page.check_login_link_redirect()


#=======================================================================================================================
