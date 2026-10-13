"""
Pages fixtures
"""
import pytest
from playwright.sync_api import Page

from pages.auth.login.login_page import LoginPage
from pages.auth.registration.registration_page import RegistrationPage
from pages.courses.courses_list.courses_list_page import CoursesListPage
from pages.courses.create_course.create_course_page import CreateCoursePage
from pages.dashboard.dashboard_page import DashboardPage

#=======================================================================================================================
#-------------------------------------------------- Guest Pages --------------------------------------------------------
@pytest.fixture
def login_page(page_guest: Page) -> LoginPage:
    """
    Initialize LoginPage()

    :param page_guest: Fixture page_guest (no Storage State)
    :return: LoginPage(page=page_guest)
    """
    return LoginPage(page_guest)

@pytest.fixture
def registration_page(page_guest: Page) -> RegistrationPage:
    """
    Initialize RegistrationPage()

    :param page_guest: Fixture page_guest (no Storage State)
    :return: RegistrationPage(page=page_guest)
    """
    return RegistrationPage(page_guest)


#--------------------------------------------- Pages + Storage State 📦 ------------------------------------------------
@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    """
    Initialize DashboardPage()

    :param page: Fixture page (with Storage State)
    :return: DashboardPage(page=page)
    """
    return DashboardPage(page)

@pytest.fixture
def courses_list_page(page: Page) -> CoursesListPage:
    """
    Initialize CoursesListPage()

    :param page: Fixture page (with Storage State)
    :return: CoursesListPage(page=page)
    """
    return CoursesListPage(page)

@pytest.fixture
def create_course_page(page: Page) -> CreateCoursePage:
    """
    Initialize CreateCoursePage()

    :param page: Fixture page (with Storage State)
    :return: CreateCoursePage(page=page)
    """
    return CreateCoursePage(page)

#=======================================================================================================================
