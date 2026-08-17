"""
Pages fixtures
"""
import pytest
from playwright.sync_api import Page
from pages.courses.courses_list.courses_list_page import CoursesListPage
from pages.courses.create_course.create_course_page import CreateCoursePage
from pages.auth.login.login_page import LoginPage
from pages.auth.regustration.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

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
def dashboard_page(page: Page) -> DashboardPage:
    """
    Фикстура инициализации класса DashboardPage()

    :param page: Фикстура chromium_page (with Storage State)
    :return: DashboardPage(page=page)
    """
    return DashboardPage(page=page)


@pytest.fixture
def courses_list_page(page: Page) -> CoursesListPage:
    """
    Фикстура инициализации класса CoursesListPage()

    :param page: Фикстура chromium_page (with Storage State)
    :return: CoursesListPage(page=page)
    """
    return CoursesListPage(page=page)


@pytest.fixture
def create_course_page(page: Page) -> CreateCoursePage:
    """
    Фикстура инициализации класса CreateCoursePage()

    :param page: Фикстура chromium_page (with Storage State)
    :return: CreateCoursePage(page=page)
    """
    return CreateCoursePage(page=page)

#=======================================================================================================================
