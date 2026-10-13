"""
Allure autouse-fixture
"""
import pytest

from tools.allure.environment import create_allure_environment_file

#=======================================================================================================================
@pytest.fixture(scope='session', autouse=True)
def save_allure_environment_file():
    """
    The autouse fixture creates an <environment.properties> file in the <allure-results> folder.

    .
    """
    yield
    create_allure_environment_file()


#=======================================================================================================================
