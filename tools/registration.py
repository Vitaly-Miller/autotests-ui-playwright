"""
Registration new user (helper)
"""
from playwright.sync_api import Page

from config import settings
from pages.auth.registration.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

#=======================================================================================================================
# Registration new user (helper)
def registration_new_user(
    page: Page,
    email: str = settings.test_user.email,
    username: str = settings.test_user.username,
    password: str = settings.test_user.password
):
    """
    Registration new user (helper)

    Opens the registration page, fills the form with test data, submits it and waits for the redirect to /dashboard

    :param page: Page — unauthenticated page
    :param email: Email
    :param username: Username
    :param password: Password
    :return: None (the page stays on /dashboard in an authenticated state)
    """
    registration_page = RegistrationPage(page)
    registration_page.open(registration_page.URL)
    registration_page.form.fill(
        email=email,
        username=username,
        password=password
    )
    registration_page.click_registration_btn()
    page.wait_for_url(DashboardPage.URL)

#=======================================================================================================================
