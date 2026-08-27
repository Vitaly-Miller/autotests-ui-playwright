# Playwright Trace Viewer

---
https://playwright.dev/python/docs/trace-viewer

https://trace.playwright.dev

---
playwright show-trace trace.zip

```python
"""
Browsers fixtures
"""
import pytest
import allure
from playwright.sync_api import Playwright, StorageState, ViewportSize
from pages.auth.registration.registration_page import RegistrationPage
from _pytest.fixtures import SubRequest

#=======================================================================================================================
# Chromium Page + Storage state 📦
@pytest.fixture
def page(request: SubRequest, storage_state: StorageState, playwright: Playwright): # Используем фикстуру storage_state с авторизацией + встроенную фикстуру playwright из pytest_playwright plugin
    """
    Fixture for authorized user (registered)

    :param request: SubRequest.request (for tracing)
    :param storage_state: Фикстура с сохраненными авторизационными данными
    :param playwright: Playwright
    :return: yield page: Page
    """
    browser = playwright.chromium.launch(                 # Создаем объект браузера на движке chromium c параметрами:
        channel='chromium',                               # - UI оболочка: 'chromium', 'chrome', 'msedge'
        headless=True,                                    # - True/False — НЕ/Показывать браузер
        slow_mo=None)                                     # - Action delay (ms)
    context = browser.new_context(                        # Создание браузерного окружения с Storage state:
        storage_state=storage_state,               # ┐    # - Storage state из фикстуры
        # storage_state='storage_state.json',      # ┘    # - Storage state из JSON-файла (optional)
        locale='en-US',                                   # - Website language (locale)
        viewport=ViewportSize(width=1100, height=1200))   # - Window size
    context.tracing.start(                                # Включаем Tracing для Playwright Trace Viewer
        screenshots=True,                                 # - Screenshots
        snapshots=True,                                   # - Snapshots
        sources=True                                      # - Sources
    )
    page = context.new_page()                             # Создаем объект страницы page на базе context

    try:
        yield page                                        # Передаем page (на базе движка chromium)

    finally:                                              # Гарантия закрытия, если упадет.
        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')  # Сохраняем трейсинг в zip-файл (c именем текущего теста)
        context.close()                                   # Закрываем context!
        browser.close()                                   # Закрываем browser!
        allure.attach.file(                               # 💾Прикрепляем трейсинг к Allure-отчету
            f'./tracing/{request.node.name}.zip',         # - File path
            name=f'{request.node.name}_trace',            # - Name in Allure-report (Tear down)
            attachment_type=allure.attachment_type.ZIP    # - File type - ZIP
        )
```
