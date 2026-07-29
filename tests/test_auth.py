"""
Test authorization (Login) with Parametrize (3-in-1)
"""

import pytest
from pages.login_page import LoginPage

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

@pytest.mark.auth                 # ┐
@pytest.mark.regression           # │ Pytest Markers
@pytest.mark.negative             # ┘
@pytest.mark.parametrize(         # ] Pytest Parametrize
    'email, password',[                                          # Параметризация Email и Password:
        ('user.name@gmail.com', 'password'),       # - Valid (unregistered)
        ('  ', 'password'),                        # - Invalid email
        ('user.name@gmail.com', '  ')              # - Invalid password
    ])
def test_auth_with_wrong_email_or_password(login_page: LoginPage, email: str, password: str):  # Принимает фикстуру login_page, email и password из parametrize
    # ▶ ACTIONS
    login_page.visit(login_url)                                  # Переход на страницу по URL                            # ⚠️Чтобы не передавать URL в тесте - перенести метод visit в класс LoginPage c вшитым URL
    login_page.fill_login_form(email=email, password=password)   # Заполнение Login-формы с данными из параметризации
    login_page.click_login_btn()                                 # Клик по кнопке <Login>

    # ✔️EXPECTATIONS
    login_page.check_wrong_email_password_alert()                # Проверка видимости сообщения об ошибке и ее текст


#=======================================================================================================================
