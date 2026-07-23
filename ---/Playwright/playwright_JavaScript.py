"""
Playwright - Выполнение JavaScript кода на странице (page.evaluate())
"""
from playwright.sync_api import sync_playwright
from time import sleep

#=======================================================================================================================
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                        # Создаем объект playwright = sync_playwright() (инициализация)
    chromium = playwright.chromium.launch(headless=False)    # Создаем объект браузера chromium c запуском браузера (с отображением)
    page = chromium.new_page()                               # Создаем объект страницы page c запуском новой страницы

    page.goto(
        login_url,                                       # ▶ ACTION - Переход на страницу по URL
        wait_until='networkidle'                             # ⚠️ Ждем полной загрузки страницы
    )


    # v.1 - Выполняем JS-код для замены текста заголовка (.evaluate)
    page.evaluate("""
                  const title = document.getElementById('authentication-ui-course-title-text');
                  title.textContent = '---- New Text ---- v.1';
                  """)
    page.wait_for_timeout(1000)                             # ⏳


    # v.2 - Передача аргументов через анонимную функцию (.evaluate)
    page.evaluate(
        """
        (text) => {
            const title = document.getElementById('authentication-ui-course-title-text');
            title.textContent = text;
        }
        """,
        '==== New Text ==== v.2'
    )
    page.wait_for_timeout(1000)                             # ⏳
#=======================================================================================================================
