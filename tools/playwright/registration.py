"""
Registration new user (helper)
"""
from playwright.sync_api import Page
from pages.auth.registration.registration_page import RegistrationPage
from config import settings

#=======================================================================================================================
# Registration new user (helper)
def registration_new_user(page: Page):
    """
    Registration new user (helper)

    Открывает страницу регистрации, заполняет форму тестовыми данными, сабмитит и ждёт редиректа на /dashboard
    (гарантирует, что Storage state с авторизацией сформировался).

    :param page: Page — чистая страница без авторизации
    :return: None (страница остаётся на /dashboard в авторизованном состоянии)
    """
    registration_page = RegistrationPage(page)  # Инициализация страницы в переменную
    registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password)
    registration_page.click_registration_btn()
    page.wait_for_url('**/dashboard')           # ❗️Дождаться открытие страницы, что бы гарантировано сформировался Storage state

#=======================================================================================================================
