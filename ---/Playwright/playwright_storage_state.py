"""
Playwright Storage State
"""
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
dashboard_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

#-------------------------------------------------- 1. Registration ----------------------------------------------------
# Регристрация пользователя + сохранение Storage State в файл
with (sync_playwright() as playwright):         # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(       # Создаем объект браузера на движке chromium c  параметрами:
        headless=False,                         # - False — показывать браузер
        slow_mo=500                             # - Action delay (ms)
    )
    context = browser.new_context()             # Создание браузерного окружения
    page = context.new_page()                   # Создаем объект страницы page (на базе context)

    #-------------------------------------------------------------------------------------------------------------------
    # ⿹ Open page
    page.goto(registration_url)

    # ㉧ LOCATORS
    email_field = page.get_by_role('textbox', name='Email')
    username_field = page.get_by_role('textbox', name='Username')
    password_field = page.get_by_role('textbox', name='Password')
    registration_btn = page.get_by_role("button", name='Registration')

    # ▶ ACTIONS
    email_field.fill('user.name@gmail.com')
    username_field.fill('username')
    password_field.fill('password')
    registration_btn.click()

    #------------------------------------------------------ 💾----------------------------------------------------------
    # Сохраняем в файл состояние сессии (cookies + localStorage) после регистрации
    context.storage_state(path="storage_state.json")


#------------------------------------------------ 2. БЕЗ Storage state -------------------------------------------------
# Попытка зайти на Dashboard page БЕЗ Storage state
with (sync_playwright() as playwright):      # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(    # Создаем объект браузера на движке chromium c  параметрами:
        headless=False,                      # - False — показывать браузер
        slow_mo=500                          # - Action delay (ms)
    )
    context = browser.new_context()          # Создание браузерного окружения
    page = context.new_page()                # Создаем объект страницы page (на базе context)
    page.goto(dashboard_url)                 # Dashboard page - не открыввется —> Redirect на Login page (Auth)

    # ⏳
    page.wait_for_timeout(2000)

#--------------------------------------------------- 3.Storage state ---------------------------------------------------
# Попытка зайти на Dashboard page WITH Storage state
with (sync_playwright() as playwright):      # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(    # Создаем объект браузера на движке chromium c  параметрами:
        headless=False,                      # - False — показывать браузер
        slow_mo=500                          # - Action delay (ms)
    )
    context = browser.new_context(           # Создание браузерного окружения
        storage_state="storage_state.json"   # 👈 Подтягиваем Storage state из сохраненного файла
    )
    page = context.new_page()                # Создаем объект страницы page (на базе context)
    page.goto(dashboard_url)                 # Dashboard page - открыввется ✔️

    # ⏳
    page.wait_for_timeout(2000)


#=======================================================================================================================
