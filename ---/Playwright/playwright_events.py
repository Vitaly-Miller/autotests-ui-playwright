"""
Playwright events - события
"""
from playwright.sync_api import sync_playwright, Request, Response

#=======================================================================================================================
#----------------------------------------------------- Playwright setup ------------------------------------------------
login_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                        # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(headless=False)    # Создаем объект браузера chromium c запуском браузера (с отображением)
    page = browser.new_page()                               # Создаем объект страницы page c запуском новой страницы


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
"""
 Request: ⮕ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/
Response: ⬅︎ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/ Status: 200
 Request: ⮕ https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap
 Request: ⮕ https://nikita-filonov.github.io/ui-coverage-report/agent.global.js
 Request: ⮕ https://nikita-filonov.github.io/ui-coverage-scenario-report/agent.global.js
 Request: ⮕ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/static/js/main.ffb16498.js
Response: ⬅︎ https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap Status: 200
Response: ⬅︎ https://nikita-filonov.github.io/ui-coverage-report/agent.global.js Status: 200
Response: ⬅︎ https://nikita-filonov.github.io/ui-coverage-scenario-report/agent.global.js Status: 200
Response: ⬅︎ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/static/js/main.ffb16498.js Status: 200
 Request: ⮕ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/static/js/15.a93772cc.chunk.js
 Request: ⮕ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/static/js/94.c060f753.chunk.js
Response: ⬅︎ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/static/js/15.a93772cc.chunk.js Status: 200
Response: ⬅︎ https://nikita-filonov.github.io/qa-automation-engineer-ui-course/static/js/94.c060f753.chunk.js Status: 200
 Request: ⮕ https://fonts.gstatic.com/s/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBHMdazQ.woff2
Response: ⬅︎ https://fonts.gstatic.com/s/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBHMdazQ.woff2 Status: 200
"""
