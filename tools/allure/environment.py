"""
Allure Environment
"""

from config import settings, Dir
import platform

#=======================================================================================================================
def create_allure_environment_file():
    """
    Создает файл environment.properties в папке allure-results

    Собирает информацию об окружении теста (base_url, timeout, ОС, версия Python, хост...)
    и записывает ее в формате key=value — Allure отобразит эти данные на вкладке "Environment"
    """
    properties = {                                                                    # Dict
        'Base_URL': settings.base_url,                                                # Base URL
        'Test_User': settings.test_user,
        'Browser': settings.browser,                                                  # Browser
        'OS': platform.platform(terse=True),                                          # macOS-26.5.2
        'Lang': f'{platform.python_implementation()}, {platform.python_version()}',   # CPython, 3.14.3
        'Host_Name': platform.node(),                                                 # MacBookPro.local
        'Headless': settings.headless,                                                # Headless
        'Slow_Mo': settings.slow_mo,                                                  # Slow mo
    }
    content = '\n'.join(f'{key}={value}' for key, value in properties.items())   # Итерация <properties> и склеивание в строку с переносами

    Dir.ALLURE_RESULTS.mkdir(parents=True, exist_ok=True)                        # Создание папки, если её нет
    file_path = Dir.ALLURE_RESULTS / 'environment.properties'                    # Путь для записи файла
    file_path.write_text(content, encoding='utf-8')                              # Запись в файл


#=======================================================================================================================
