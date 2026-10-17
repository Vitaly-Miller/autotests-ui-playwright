"""
conftest.py (via Pytest Plugins)

pytest_plugins is used - all fixtures are in separate module files
"""

#=============================================== Plugins path (Manual) =================================================
# Manual path to fixtures
pytest_plugins = (
    'fixtures.browsers_fixtures',
    'fixtures.pages_fixtures',
    'fixtures.allure_fixtures',
)

#================================================ Plugins path (Auto) ==================================================
# Automatically connects all module files from the fixtures/ (except __init__.py)
# pytest_plugins = [
#     f'fixtures.{file.stem}'
#     for file in Path(__file__).parent.glob('fixtures/*.py')
#     if file.name != '__init__.py'
# ]

#=======================================================================================================================
