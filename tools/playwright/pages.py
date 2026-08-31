"""
Pages (helper)
"""
import allure
from playwright.sync_api import Playwright, StorageState, ViewportSize

#=======================================================================================================================
def init_playwright_page(playwright: Playwright, test_name: str, storage_state: StorageState | None = None):
    """
    Генератор-хелпер для pytest-фикстур
    Поднимает браузер Chromium, создаёт context (со Storage state или без),
    включает Tracing, отдаёт Page тесту, а в teardown останавливает Tracing,
    прикрепляет trace + video к Allure и закрывает context/browser.

    Используется в фикстурах через ``yield from``::

        yield from init_playwright_page(
            playwright=playwright, test_name=request.node.name, storage_state=storage_state
        )

    :param playwright: Playwright (встроенная фикстура из pytest_playwright)
    :param test_name: Имя текущего теста (request.node.name) — для путей video/trace и имён вложений в Allure
    :param storage_state: Авторизационные данные; None → гостевой context без авторизации
    :return: yield page: Page (на движке chromium)
    """
    browser = playwright.chromium.launch(                # Создаем объект браузера на движке chromium c параметрами:
        channel='chromium',                              # - UI оболочка: 'chromium', 'chrome', 'msedge'
        headless=True,                                   # - True/False — НЕ/Показывать браузер
        slow_mo=None                                     # - Action delay (ms)
    )
    context = browser.new_context(                       # Создание браузерного окружения с Storage state:
        storage_state=storage_state,            # ┐      # - Storage state из фикстуры
        # storage_state='storage_state.json',   # ┘      # - Storage state из JSON-файла (optional)
        locale='en-US',  # - Website language (locale)
        viewport=ViewportSize(width=1100, height=1200),  # - Window size
        record_video_dir=f'tracing/videos/{test_name}'   # - Record video directory
    )
    context.tracing.start(                               # Tracing для Playwright Trace Viewer
        screenshots=True,                                # - Screenshots
        snapshots=True,                                  # - Snapshots
        sources=True                                     # - Sources
    )
    page = context.new_page()                            # Создаем объект страницы page на базе context

    try:
        yield page                                       # Передаем page (на базе движка chromium)

    finally:                                             # Гарантия закрытия, если упадет
        context.tracing.stop(
            path=f'tracing/{test_name}.zip')             # Сохраняем трейсинг в zip-файл (c именем текущего теста)
        allure.attach.file(                              # 💾 Прикрепляем трейсинг к Allure-отчету
            source=f'tracing/{test_name}.zip',           # - File path
            name=f'{test_name}_trace',                   # - Name in Allure-report (Tear down)
            attachment_type=allure.attachment_type.ZIP   # - File type - ZIP
        )

        context.close()    # Закрываем context! (Playwright дописывает видео на диск)
        browser.close()    # Закрываем browser!

        allure.attach.file(                              # 💾 Прикрепляем video к Allure-отчету (файл уже финализирован)
            source=page.video.path(),    # NOQA          # - File path (через Page)
            name=f'{test_name}_video',                   # - Name in Allure-report (Tear down)
            attachment_type=allure.attachment_type.WEBM  # - File type - WEBM
        )

#=======================================================================================================================
