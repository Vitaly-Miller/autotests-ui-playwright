"""
pytest-rerunfailures - модуль перезапуска НЕСТАБИЛЬНЫХ (flaky) тестов
"""
"""
Terminal:
pip install pytest-rerunfailures
https://github.com/pytest-dev/pytest-rerunfailures

⚠️Синтаксис: (строгий)
.mark.flaky     - маркер для перезапуска нестабильного теста
reruns=         - параметр количества повторов перезапуска (рекомендуется не более 3)
reruns_delay=  - задержка между повторами перезапуска
condition=     - условие перезапуска нестабильного теста
only_rerun=    - перезапускать только если сообщение об ошибке ... (например ="ConnectionError")
rerun_except=  - НЕ перезапускать, если сообщение об ошибке ... (например ="ConnectionError")
"""
import pytest
import random

#============================================== Unstable test (flaky test) =============================================
#------------------------------------------------------- returns -------------------------------------------------------
# Если нестабильный тест упал - Перезапустить 3 раза (более не нужно),
@pytest.mark.flaky(reruns=3)                    # Маркер нестабильного (flaky) теста
def test_1_reruns():
    assert random.choice([True, False])         # Падает 50%
                                                # ❌RERUN
                                                # ❌RERUN
                                                # ✅PASSED

#---------------------------------------------------- reruns_delay -----------------------------------------------------
# Если нестабильный тест упал - Перезапустить 3 раза, с паузой 2 сек.
@pytest.mark.flaky(reruns=3, reruns_delay=2)    # Маркер нестабильного (flaky) теста
def test_2_reruns_delay():
    assert random.choice([True, False])         # Падает 50%
                                                # ❌RERUN (ждёт 2 сек)
                                                # ❌RERUN (ждёт 2 сек)
                                                # ✅PASSED

#------------------------------------------------------ condition ------------------------------------------------------
# data
PING = 1.0  # sec

# Если нестабильный тест упал - перезапустить 3 раза, с паузой 2 сек —> ТОЛЬКО ЕСЛИ PING > 0.9
@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PING > 0.9)   # Маркер нестабильного (flaky) теста
def test_3_condition():
    assert random.choice([True, False])         # Падает 50%
                                                # ❌RERUN (ждёт 2 сек)
                                                # ❌RERUN (ждёт 2 сек)
                                                # ✅PASSED



#========================================== Unstable Test Class (flaky class) ==========================================
@pytest.mark.flaky(reruns=3)                    # 👈 всё то же самое (распространяется на ВСЕ тестовые методы тестового класса)
class TestClass:                                # Класс с нестабильными тестами
    def test_1(self):
        assert random.choice([True, False])     # Падает 50%
                                                # ❌RERUN
                                                # ✅PASSED
    def test_2(self):
        assert random.choice([True, False])     # Падает 50%
                                                # ❌RERUN
                                                # ❌RERUN
                                                # ✅PASSED

#=======================================================================================================================
