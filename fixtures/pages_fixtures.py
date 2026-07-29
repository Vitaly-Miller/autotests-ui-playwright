"""
Pages fixtures
"""
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

#=======================================================================================================================
#----------------------------------------------------- Guest Pages -----------------------------------------------------
@pytest.fixture
def login_page(guest_page: Page) -> LoginPage:
    """
    Фикстура инициализации класса LoginPage()

    :param guest_page: Фикстура guest_page (NO Storage State)
    :return: LoginPage(page=guest_page)
    """
    return LoginPage(page=guest_page)

@pytest.fixture
def registration_page(guest_page: Page) -> RegistrationPage:
    """
    Фикстура инициализации класса RegistrationPage()

    :param guest_page: Фикстура guest_page (NO Storage State)
    :return: RegistrationPage(page=guest_page)
    """
    return RegistrationPage(page=guest_page)


@pytest.fixture
def dashboard_page(guest_page: Page) -> DashboardPage:
    """
    Фикстура инициализации класса DashboardPage()

    :param guest_page: Фикстура guest_page (NO Storage State)
    :return: DashboardPage(page=guest_page)
    """
    return DashboardPage(page=guest_page)

#------------------------------------------ Chromium Pages (+ Storage State) -------------------------------------------
@pytest.fixture
def dashboard_page_(chromium_page: Page) -> DashboardPage:
    """
    Фикстура инициализации класса DashboardPage()

    :param chromium_page: Фикстура chromium_page (with Storage State)
    :return: DashboardPage(page=chromium_page)
    """
    return DashboardPage(page=chromium_page)

#=======================================================================================================================
