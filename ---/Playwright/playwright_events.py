"""
Playwright events - события
"""
from playwright.sync_api import sync_playwright, Request, Response

#=======================================================================================================================
#----------------------------------------------------- Playwright setup ------------------------------------------------
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                        # Создаем объект playwright = sync_playwright() (инициализация)
    chromium = playwright.chromium.launch(headless=False)    # Создаем объект браузера chromium c запуском браузера (с отображением)
    page = chromium.new_page()                               # Создаем объект страницы page c запуском новой страницы


    #----------------------------------------------- Callbacks functions -----------------------------------------------
    # Логирование запросов
    def log_request(request: Request):
        print(f' Request: ⮕ {request.url}')

    # Логирование ответов
    def log_response(response: Response):
        print(f'Response: ⬅︎ {response.url} Status: {response.status}')

    #----------------------------------------------- Обработчики событий -----------------------------------------------
    # Добавляем обработчики событий
    page.on('request', log_request)    # Событие, callback-function
    page.on('response', log_response)  # Событие, callback-function


    #-------------------------------------------------------------------------------------------------------------------
    page.goto(login_url)                        # ▶ ACTION - Переход на страницу по URL

    page.wait_for_timeout(2000)                 # ⏳

#=======================================================================================================================
