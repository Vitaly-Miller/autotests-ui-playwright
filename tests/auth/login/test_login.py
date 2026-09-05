"""
Test login
"""

import pytest
import allure
from config import settings
from tools.allure.annotations import Epic, Feature, Story, Tag
from allure_commons.types import Severity
from pages.auth.login.login_page import LoginPage
from pages.auth.registration.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.registration import registration_new_user

#=======================================================================================================================
@pytest.mark.auth                                           # ┐
@pytest.mark.login                                          # │  Pytest class markers
@pytest.mark.regression                                     # ┘
@allure.severity(Severity.BLOCKER)                          # ]  Allure severity
@allure.tag(Tag.AUTH, Tag.LOGIN, Tag.REGRESSION)      # ]  Allure tags
@allure.epic(Epic.AUTH)                                     # ┐
@allure.feature(Feature.LOGIN)                              # │  Allure Behaviors
@allure.story(Story.LOGIN)                                  # ┘
class TestLogin:
    @pytest.mark.e2e
    @allure.title('Login successful')
    def test_login_successful(self, login_page: LoginPage):

        # ⿰ PAGE OBJECTS
        registration_page = RegistrationPage(login_page.page)
        dashboard_page = DashboardPage(login_page.page)

        # ╴╴╴╴╴╴╴╴╴╴╴╴ ◁ PRE-CONDITION ╴╴╴╴╴╴╴╴╴╴╴╴╴┐
        # Registration new user
        registration_new_user(page=login_page.page)
        DashboardPage(registration_page.page).sidebar.click_logout()
        # ✔ Expectations
        login_page.check_current_url(login_page.URL)
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

        # ▶ ACTIONS
        login_page.form.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_btn()

        # ✔ Expectations
        login_page.check_current_url(DashboardPage.URL)


    @allure.severity(Severity.NORMAL)
    @allure.tag(Tag.NAVIGATE)
    @allure.story(Story.NAVIGATE)
    @allure.title('Registration-link redirect')
    def test_registration_link_redirect(self, login_page: LoginPage):
        # ⿹ Open page
        login_page.open(login_page.URL)

        # ▶ ACTIONS
        login_page.click_registration_link()

        # ✔️EXPECTATIONS
        login_page.check_current_url(RegistrationPage.URL)

#=======================================================================================================================
