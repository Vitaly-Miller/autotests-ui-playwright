"""
conftest.py (via Pytest Plugins)
"""
"""
Используется pytest_plugins - все фикстуры в отдельных модулях-файлах
"""
from pathlib import Path                  # for <Auto Plugins path>

#================================================ Plugins path (⌨️Manual) ================================================
# Ручной путь к plugins (модулям-файлам с фикстурами) - ⚠ БЕЗ расширения <.py>
pytest_plugins = (
    'fixtures.browsers_fixtures',         # ┐
                                          # │
                                          # │ Browser
                                          # │ fixtures
                                          # │
                                          # ┘
    'fixtures.pages_fixtures',            # ┐
                                          # │
                                          # │ Page
                                          # │ fixtures
                                          # │
                                          # ┘

    #'fixtures.allure_fixtures'           # Allure fixture
)

#================================================ Plugins path (✨Auto) ================================================
# Автоматически подключает все модули-файлы из папки fixtures/ (кроме __init__.py)
# pytest_plugins = [
#     f'fixtures.{file.stem}'
#     for file in Path(__file__).parent.glob('fixtures/*.py')
#     if file.name != '__init__.py'
# ]
#=======================================================================================================================
