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
def login_page(page_guest: Page) -> LoginPage:
    """
    Фикстура инициализации класса LoginPage()

    :param page_guest: Фикстура guest_page (NO Storage State)
    :return: LoginPage(page=guest_page)
    """
    return LoginPage(page=page_guest)


@pytest.fixture
def registration_page(page_guest: Page) -> RegistrationPage:
    """
    Фикстура инициализации класса RegistrationPage()

    :param page_guest: Фикстура guest_page (NO Storage State)
    :return: RegistrationPage(page=guest_page)
    """
    return RegistrationPage(page=page_guest)


#---------------------------------------- Chromium Pages (+ Storage State 📦) ------------------------------------------
@pytest.fixture
def dashboard_page(chromium_page_with_storage_state: Page) -> DashboardPage:
    """
    Фикстура инициализации класса DashboardPage()

    :param chromium_page_with_storage_state: Фикстура chromium_page (with Storage State)
    :return: DashboardPage(page=chromium_page_with_storage_state)
    """
    return DashboardPage(page=chromium_page_with_storage_state)


@pytest.fixture
def courses_list_page(chromium_page_with_storage_state: Page) -> CoursesListPage:
    """
    Фикстура инициализации класса CoursesListPage()

    :param chromium_page_with_storage_state: Фикстура chromium_page (with Storage State)
    :return: CoursesListPage(page=chromium_page_with_storage_state)
    """
    return CoursesListPage(page=chromium_page_with_storage_state)


@pytest.fixture
def create_course_page(chromium_page_with_storage_state: Page) -> CreateCoursePage:
    """
    Фикстура инициализации класса CreateCoursePage()

    :param chromium_page_with_storage_state: Фикстура chromium_page (with Storage State)
    :return: CreateCoursePage(page=chromium_page_with_storage_state)
    """
    return CreateCoursePage(page=chromium_page_with_storage_state)

#=======================================================================================================================
