"""
Playwright Courses
"""
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

#-------------------------------------------------- 1. Registration ----------------------------------------------------
# Регистрация пользователя + сохранение Storage State в файл
with (sync_playwright() as playwright):         # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch()      # Создаем объект браузера на движке chromium c  default-параметрами
    context = browser.new_context()             # Создание браузерного окружения
    page = context.new_page()                   # Создаем объект страницы page (на базе context)

    #-------------------------------------------------------------------------------------------------------------------
    # ⿹ Open page
    page.goto(registration_url)

    # ㉧ LOCATORS
    email_field = page.get_by_role(role='textbox', name='Email')
    username_field = page.get_by_role(role='textbox', name='Username')
    password_field = page.get_by_role(role='textbox', name='Password')
    registration_btn = page.get_by_role(role='button', name='Registration')

    # ▶ ACTIONS
    email_field.fill('user.name@gmail.com')
    username_field.fill('username')
    password_field.fill('password')
    registration_btn.click()

    #------------------------------------------------------ 💾----------------------------------------------------------
    # Сохраняем в файл состояние сессии (cookies + localStorage) после регистрации
    context.storage_state(path="storage_state.json")


#--------------------------------------------------- 2. Storage state --------------------------------------------------
# Попытка зайти на Courses page WITH Storage state
with (sync_playwright() as playwright):      # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(    # Создаем объект браузера на движке chromium c  параметрами:
        headless=False,                      # - False — показывать браузер
        slow_mo=500                          # - Action delay (ms)
    )
    context = browser.new_context(           # Создание браузерного окружения
        storage_state="storage_state.json"   # 👈 Подтягиваем Storage state из сохраненного файла
    )
    page = context.new_page()                # Создаем объект страницы page (на базе context)
    page.goto(courses_url)                   # Courses page - открывается ✔️

    # ㉧ LOCATORS
    courses_header = page.get_by_role(role='heading', name='Courses')
    folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
    no_result = page.get_by_role(role='heading', name='There is no results')
    description = page.get_by_test_id('courses-list-empty-view-description-text')

    # ✔︎ EXPECTATIONS
    expect(page).to_have_url(courses_url)
    expect(courses_header).to_have_text('Courses')
    expect(folder_icon).to_be_visible()
    expect(no_result).to_have_text('There is no results')
    expect(description).to_have_text('Results from the load test pipeline will be displayed here')



    # ⏳
    page.wait_for_timeout(1000)
#=======================================================================================================================
