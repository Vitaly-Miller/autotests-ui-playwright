"""
Pages fixtures
"""
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

#=======================================================================================================================
@pytest.fixture
def login_page(guest_page: Page) -> LoginPage:
    """
    Фикстура LoginPage

    :param guest_page: Фикстура guest_page без Storage State
    :return: LoginPage c фикстурой guest_page
    """
    return LoginPage(page=guest_page)

#=======================================================================================================================
