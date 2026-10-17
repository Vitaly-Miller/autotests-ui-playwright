"""
Allure Environment
"""
import platform

from config import Dir, settings

#=======================================================================================================================
def create_allure_environment_file():
    """
    Creates the environment.properties file in the allure-results folder

    Collects information about the test environment (base_url, browser, OS, Python version, host...)
    and writes it in key=value format — Allure displays this data on the "Environment" tab
    """
    properties = {
        'Host-Name': platform.node(),                                                 # MacBookPro.local
        'Architecture': platform.machine(),                                           # arm64

        'OS': platform.platform(terse=True),                                          # macOS-27.2
        'Python': platform.python_version(),                                          # 3.14.3
        'Browser': ', '.join(browser.value for browser in settings.browser).title(),  # Browser
        'Headless': settings.headless,                                                # True
        'Slow-Mo': f'{settings.slow_mo} ms',                                          # 0 ms

        'Base-URL': settings.base_url,                                                # Base URL
        'Test-User-Email': settings.test_user.email,                                  # Test user email
        'Test-User-Username': settings.test_user.username,                            # Test user username
        'Test-User-Password': '***',                                                  # Masked
    }
    content = '\n'.join(f'{key}={value}' for key, value in properties.items())

    Dir.ALLURE_RESULTS.mkdir(parents=True, exist_ok=True)
    file_path = Dir.ALLURE_RESULTS / 'environment.properties'
    file_path.write_text(content, encoding='utf-8')


#=======================================================================================================================
