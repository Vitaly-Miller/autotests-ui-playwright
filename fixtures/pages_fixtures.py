"""
Pages fixtures
"""
import pytest
from playwright.sync_api import Page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

#=======================================================================================================================
#------------------------------------------- Chromium Pages (Guest Pages) ----------------------------------------------
@pytest.fixture
def login_page(chromium_page_guest_page: Page) -> LoginPage:
    """
    Фикстура инициализации класса LoginPage()

    :param chromium_page_guest_page: Фикстура guest_page (NO Storage State)
    :return: LoginPage(page=guest_page)
    """
    return LoginPage(page=chromium_page_guest_page)


@pytest.fixture
def registration_page(chromium_page_guest_page: Page) -> RegistrationPage:
    """
    Фикстура инициализации класса RegistrationPage()

    :param chromium_page_guest_page: Фикстура guest_page (NO Storage State)
    :return: RegistrationPage(page=guest_page)
    """
    return RegistrationPage(page=chromium_page_guest_page)


#---------------------------------------- Chromium Pages (+ Storage State 📦) ------------------------------------------
@pytest.fixture
def dashboard_page(chromium_page_with_store_state: Page) -> DashboardPage:
    """
    Фикстура инициализации класса DashboardPage()

    :param chromium_page_with_store_state: Фикстура chromium_page (with Storage State)
    :return: DashboardPage(page=chromium_page)
    """
    return DashboardPage(page=chromium_page_with_store_state)


@pytest.fixture
def courses_list_page(chromium_page_with_store_state: Page) -> CoursesListPage:
    """
    Фикстура инициализации класса CoursesListPage()

    :param chromium_page_with_store_state: Фикстура chromium_page (with Storage State)
    :return: CreateCoursePage(page=chromium_page)
    """
    return CoursesListPage(page=chromium_page_with_store_state)


@pytest.fixture
def create_course_page(chromium_page_with_store_state: Page) -> CreateCoursePage:
    """
    Фикстура инициализации класса CreateCoursePage()

    :param chromium_page_with_store_state: Фикстура chromium_page (with Storage State)
    :return: CreateCoursePage(page=chromium_page)
    """
    return CreateCoursePage(page=chromium_page_with_store_state)

#=======================================================================================================================
