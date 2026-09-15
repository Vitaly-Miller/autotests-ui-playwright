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
    properties = {
        'Host-Name': platform.node(),                                                 # MacBookPro.local
        'Architecture': platform.machine(),                                           # arm64

        'OS': platform.platform(terse=True),                                          # macOS-26.5.2
        'Python': platform.python_version(),                                          # 3.14.3
        'Browser': ', '.join(browser.value for browser in settings.browser).title(),  # Browser
        'Headless': settings.headless,                                                # True
        'Slow-Mo': f'{settings.slow_mo} ms',                                          # 0 ms

        'Base-URL': settings.base_url,                                                # Base URL
        'Test-User-Email': settings.test_user.email,                                  # Test user email
        'Test-User-Username': settings.test_user.username,                            # Test user username
        'Test-User-Password': settings.test_user.password,                            # Test user password
    }
    content = '\n'.join(f'{key}={value}' for key, value in properties.items())   # Итерация <properties> и склеивание в строку с переносами

    Dir.ALLURE_RESULTS.mkdir(parents=True, exist_ok=True)                        # Создание папки, если её нет
    file_path = Dir.ALLURE_RESULTS / 'environment.properties'                    # Путь для записи файла
    file_path.write_text(content, encoding='utf-8')                              # Запись в файл


#=======================================================================================================================
