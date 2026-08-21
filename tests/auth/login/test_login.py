"""
Test login
"""

import pytest
import allure
from tools.allure.annotations import Epic, Feature, Story, Tag
from pages.auth.login.login_page import LoginPage
from pages.auth.regustration.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.auth                                           # ┐
@pytest.mark.login                                          # │  Pytest class markers
@pytest.mark.regression                                     # ┘
@allure.tag(Tag.AUTH, Tag.LOGIN, Tag.REGRESSION)      # ]  Allure tags
@allure.epic(Epic.AUTH)                                     # ┐
@allure.feature(Feature.LOGIN)                              # │  Allure Behaviors
@allure.story(Story.LOGIN)                                  # ┘
class TestLogin:
    @pytest.mark.e2e
    @allure.title('Login successful')
    def test_login_successful(self, login_page: LoginPage):
        # ⏎ INPUT USER DATA
        email = 'user.name@gmail.com'
        username = 'username'
        password = 'password'

        # ⿴ PAGES OBJECTS
        registration_page = RegistrationPage(login_page.page)
        dashboard_page = DashboardPage(login_page.page)

        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴ ◁ PRE-CONDITION ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
        # New user registration
        registration_page.open(registration_page.URL)                             # ⿹ Open page
        registration_page.form.fill_registration_form(email, username, password)  # ▶︎ Fill registration form
        registration_page.click_registration_btn()                                # ▶︎ Click registration button
        dashboard_page.sidebar.click_logout()                                     # ▶︎ Click Sidebar Logout item
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

        # ▶ ACTIONS
        login_page.form.fill_login_form(email=email, password=password)
        login_page.click_login_btn()

        # ✔ Expectations
        login_page.check_current_url(dashboard_page.URL)


#=======================================================================================================================
