"""
Pytest parametrize (для Тестов)
@pytest.mark.parametrize()
"""
"""
Позволяет запустить одну и ту же функцию (тест) с разными входными данными
@pytest.mark.parametrize('param_name', [value_1, value_2, ...])  - c одним параметром
@pytest.mark.parametrize('param_1_name, param_2_name', [         - c несколькими параметрами
    (param_1_value_1, param_2_value_1)                           - пара-1
    (param_1_value_2, param_2_value_2)                           - пара-2
    (param_1_value_3, param_2_value_3)                           - пара-3 
])
"""
import pytest

#=======================================================================================================================
"""
Задание:
Проверить что число > 0
"""
#================================================ Manual parametrize ===================================================
# Manual
def test_1():
    assert 1 > 0         # ✅ PASSED
    assert 2 > 0         # ✅ PASSED
    assert -1 > 0        # ❌ FAILED
    assert 3 > 0         # -- не дошла очередь

# # 3-in-1 (❌Bad practice)
def test_loop():
    for n in [1, 2, -1, 3]:
        assert n > 0     # PASSED (❌Bad practice - если тест упадет, то остальные параметры не будут проверены)


#==================================================== Parametrize ======================================================
# 3-in-1
@pytest.mark.parametrize('n', [1, 2, -1, 3])  # n = 1, n = 2, n = -1, n = 3
def test_1(n: int):                           # передаем <n>
    assert n > 0                              # подставляет КАЖДЫЙ <n>
                                              # test_1[1]  PASSED ✅
                                              # test_1[2]  PASSED ✅
                                              # test_1[-1] FAILED ❌
                                              # test_1[3]  PASSED ✅

#====================================== Duble Parametrize (c двумя параметрами) ========================================
# 3-in-1
# Возведение в квадрат
@pytest.mark.parametrize('number, expected', [            # 'параметр_1 параметр_2'
    (1, 1),
    (2, 4),
    (3, 9)
])
def test_2(number: int, expected: int):                   # —> передаем <number> и <expected>
    assert number ** 2 == expected                        # подставляет КАЖДЫЙ (<number>, <expected>)
                                                          # test_2[1-1] PASSED
                                                          # test_2[2-4] PASSED
                                                          # test_2[3-9] PASSED

#==================================== Multi Parametrize (Множественная параметризация) =================================
# 12-in-1 (3x4)

@pytest.mark.parametrize('os', [              # каждый параметр <os> будет подставлен 4 раза к каждому <browser>
    'Windows',
    'macOS',
    'Linux'
])
@pytest.mark.parametrize('browser', [         # каждый параметр <browser> будет подставлен 3 раза к каждой <os>
    'Chrome',
    'Firefox',
    'Edge',
    'Safari'
])
def test_multi_param(os: str, browser: str):  # <- Передаем параметры
     ...                                      # test_multi_param[Chrome-Windows]  PASSED
                                              # test_multi_param[Chrome-macOS]    PASSED
                                              # test_multi_param[Chrome-Linux]    PASSED
                                              # test_multi_param[Firefox-Windows] PASSED
                                              # test_multi_param[Firefox-macOS]   PASSED
                                              # test_multi_param[Firefox-Linux]   PASSED
                                              # test_multi_param[Edge-Windows]    PASSED
                                              # test_multi_param[Edge-macOS]      PASSED
                                              # test_multi_param[Edge-Linux]      PASSED
                                              # test_multi_param[Safari-Windows]  PASSED
                                              # test_multi_param[Safari-macOS]    PASSED
                                              # test_multi_param[Safari-Linux]    PASSED



#================================================= Parametrize Class ===================================================
# (2) x (2) = 4 теста
@pytest.mark.parametrize('user', ['User-1', 'User-2'])  # 2 Class-параметра
class TestClass1:
    def test_1(self, user: str):              # <- Передаем 2 Class-параметра (по очереди)
        print(f'Hi, {user}!')                 # test_1[User-1]     PASSED   Hi, User-1!
                                              # test_1[User-2]     PASSED   Hi, User-2!

    def test_2(self,user: str):               # <- Передаем 2 Class-параметра (по очереди)
        print(f'Hello, {user}!')              # test_2[User-1]  PASSED   Hello, User-1!
                                              # test_2[User-2]  PASSED   Hello, User-2!

#-----------------------------------------------------------------------------------------------------------------------
# (2) + (2 x 2) +  = 6 тестов
@pytest.mark.parametrize('user', ['User-1', 'User-2'])         # 2 Class-параметра
class TestClass2:
    def test_3(self,user: str):                                # <- Передаем 2 Class-параметра (по очереди)
        print(f'Hello, {user}!')                               # test_3[User-1] Hello, User-1!  PASSED ┐
                                                               # test_3[User-2] Hello, User-2!  PASSED ┘

    @pytest.mark.parametrize('browser', ['Chrome', 'Safari'])  # 2 Test-параметра
    def test_4(self, user: str, browser: str):                 # <- Передаем 2 Class-параметра + 2 Test-параметра ("перемножение" по очереди)
        print(f'Hi, {user}!')                                  # test_4[Chrome-User-1] Hi, User-1!  PASSED ┐
                                                               # test_4[Chrome-User-2] Hi, User-2!  PASSED │
                                                               # test_4[Safari-User-1] Hi, User-1!  PASSED │
                                                               # test_4[Safari-User-2] Hi, User-2!  PASSED ┘


#=======================================================================================================================

#=======================================================================================================================
