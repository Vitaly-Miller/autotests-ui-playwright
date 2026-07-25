"""
Pytest fixture
"""
import pytest

#=======================================================================================================================
"""
Область применения фикстуры:

---------- scope -----------
@pytest.fixture(scope='...')

Выполнить ОДИН раз на каждый(ую):
'session'  - Сессию (все тесты запуска)
'package'  - на Директорию (пакет с __init__.py)
'module'   - Файл
'class'    - Класс
'function' - Тест-функцию (Default)

---------- autouse -----------
@pytest.fixture(autouse=True)

✨Не требуется передача в тесте. Добавляется АВТОМАТИЧЕСКИ
autouse=True                   - Для каждого Теста
autouse=True, scope='class'    - Для каждого Класса
autouse=True, scope='session'  - Для каждой Сессии (все тесты запуска)
...
"""

#============================================== файл conftest.py =======================================================
#--------------------------------------- Функции-фикстуры со своей логикой ---------------------------------------------
@pytest.fixture(scope='session')
def func_1():
    print('[SESSION] Один раз на ВСЮ СЕССИЮ')

@pytest.fixture(scope='class')
def func_2():
    print('[CLASS] Один раз на каждый тестовый КЛАСС')

@pytest.fixture(scope='function')
def func_3():
    print('[FUNCTION] Один раз на каждый Тест')


@pytest.fixture(autouse=True)  # Добавляется АВТОМАТИЧЕСКИ в каждый тест!
def func_4():
    print('[AUTOUSE]  Один раз на каждый Тест (✨АВТО) -> Отчет отправлен!')


#------------------------------------------------------ Tests ----------------------------------------------------------
# Передаем фикстуры в тесты
class TestClass1:
    def test_1(self, func_1, func_2, func_3):   # [SESSION]  Один раз на ВСЮ СЕССИЮ
        ...                                     # [CLASS]    Один раз на каждый тестовый КЛАСС
                                                # [AUTOUSE]  Один раз на каждый Тест (АВТО) -> Отчет отправлен!
                                                # [FUNCTION] Один раз на каждый Тест
                                                # ✔️PASSED

    def test_2(self, func_1, func_2, func_3):   # [AUTOUSE]  Один раз на каждый Тест (АВТО) -> Отчет отправлен!
        ...                                     # [FUNCTION] Один раз на каждый Тест
                                                # ✔️PASSED



class TestClass2:
    def test_3(self, func_1, func_2, func_3):   # [CLASS]    Один раз на каждый тестовый КЛАСС
        ...                                     # [AUTOUSE]  Один раз на каждый Тест (✨АВТО) -> Отчет отправлен!
                                                # [FUNCTION] Один раз на каждый Тест
                                                # ✔️PASSED


#------------------------------------------------------- Classic -------------------------------------------------------
@pytest.fixture
def user_data() -> dict:
    return {'username': 'john_connor', 'email': 'john_connor@email.com'}


def test_username(user_data):
    print(user_data)
    assert user_data['username'] == 'john_connor'

def test_user_email(user_data):
    print(user_data)
    assert user_data['email'] == 'john_connor@email.com'

#-----------------------------------------------------------------------------------------------------------------------
