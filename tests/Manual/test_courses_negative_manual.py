"""
Test (negative)
Courses page is not opening without auth
"""

from playwright.sync_api import sync_playwright, expect
import pytest
#=======================================================================================================================
registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.negative
def test_courses_page_is_not_opening_without_auth():
    #------------------------------------------------ Playwright setup -------------------------------------------------
    # Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
    with sync_playwright() as playwright:             # Создаем объект playwright = sync_playwright() (инициализация)
        browser = playwright.chromium.launch(         # Создаем объект браузера на движке chromium c  параметрами:
            headless=True,                            # - True — не показывать браузер
            slow_mo=None                              # - Action delay (ms)
        )
        context = browser.new_context()               # Создание браузерного окружения
        page = context.new_page()                     # Создаем объект страницы page на базе context

        #------------------------------------ ◁ PRECONDITION (Auth + storage_state) ------------------------------------
        # Open page
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

        # НЕ Сохраняем Storage state после регистрации


    #------------------------------------------------ Playwright setup -------------------------------------------------
    # Попытка зайти на Dashboard page
    with (sync_playwright() as playwright):      # Создаем объект playwright = sync_playwright() (инициализация)
        browser = playwright.chromium.launch(    # Создаем объект браузера на движке chromium c  параметрами:
            headless=False,                      # - False — показывать браузер
            slow_mo=500                          # - Action delay (ms)
        )
        context = browser.new_context()          # Без Storage state
        page = context.new_page()                # Создаем объект страницы page (на базе context + Storage state)

        #---------------------------------------------------------------------------------------------------------------
        page.goto(courses_url)

        # ✔️EXPECTATIONS
        expect(page, '❌ Courses page is opening without auth!').to_have_url(login_page) # Courses page - не открыввется —> Redirect на Login page (Auth)

        # ⏳(optional)
        page.wait_for_timeout(1000)
#=======================================================================================================================
