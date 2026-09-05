"""
Registration new user (helper)
"""

from pages.auth.registration.registration_page import RegistrationPage
from config import settings
from pages.dashboard.dashboard_page import DashboardPage

#=======================================================================================================================
# Registration new user (helper)
def registration_new_user(
    page,
    email: str = settings.test_user.email,
    username: str = settings.test_user.username,
    password: str = settings.test_user.password
):
    """
    Registration new user (helper)

    Открывает страницу регистрации, заполняет форму тестовыми данными, сабмитит и ждёт редиректа на /dashboard
    (гарантирует, что Storage state с авторизацией сформировался).

    :param page: Page — страница без авторизации
    :param email: Email
    :param username: Username
    :param password: Password
    :return: None (страница остаётся на /dashboard в авторизованном состоянии)
    """
    registration_page = RegistrationPage(page)
    registration_page.open(registration_page.URL)
    registration_page.form.fill(
        email=email,
        username=username,
        password=password
    )
    registration_page.click_registration_btn()
    page.wait_for_url(DashboardPage.URL)  # ❗️Дождаться открытие страницы, что бы гарантировано сформировался Storage state


#=======================================================================================================================
