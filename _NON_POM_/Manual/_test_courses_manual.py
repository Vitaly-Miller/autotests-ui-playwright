"""
Test
Courses page is opening
"""
import pytest
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

@pytest.mark.courses
@pytest.mark.regression
def test_courses_page_is_opening():
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
        # ⿹ Open page
        page.goto(registration_url)

        # ㉧ LOCATORS
        email_field_locator = page.get_by_role(role='textbox', name='Email')
        username_field_locator = page.get_by_role(role='textbox', name='Username')
        password_field_locator = page.get_by_role(role='textbox', name='Password')
        registration_btn_locator = page.get_by_role(role='button', name='Registration')

        # ▶ ACTIONS
        email_field_locator.fill('user.name@gmail.com')
        username_field_locator.fill('username')
        password_field_locator.fill('password')
        registration_btn_locator.click()

        # 💾 Сохраняем Storage state (cookies + localStorage) в файл после регистрации
        context.storage_state(path="storage_state.json")   # 👈


    #------------------------------------------------ Playwright setup -------------------------------------------------
    # Попытка зайти на Courses page + Storage state
    with (sync_playwright() as playwright):      # Создаем объект playwright = sync_playwright() (инициализация)
        browser = playwright.chromium.launch(    # Создаем объект браузера на движке chromium c  параметрами:
            headless=False,                      # - False — показывать браузер
            slow_mo=500                          # - Action delay (ms)
        )
        context = browser.new_context(           # Создание браузерного окружения
            storage_state='storage_state.json'   # 👈 Подтягиваем Storage state из файла
        )
        page = context.new_page()                # Создаем объект страницы page (на базе context + Storage state)

        #---------------------------------------------------------------------------------------------------------------
        page.goto(courses_url)                   # Courses page - открывается ✔️

        # ㉧ LOCATORS
        courses_header_locator = page.get_by_role(role='heading', name='Courses')
        folder_icon_locator = page.get_by_test_id('courses-list-empty-view-icon')
        no_result_locator = page.get_by_role(role='heading', name='There is no results')
        description_locator = page.get_by_test_id('courses-list-empty-view-description-text')

        # ✔︎ EXPECTATIONS
        expect(page, '❌ Wrong page URL!').to_have_url(courses_url)
        expect(courses_header_locator, '❌ Wrong page header text!').to_have_text('Courses')
        expect(folder_icon_locator,'❌ Folder icon - invisible!').to_be_visible()
        expect(no_result_locator, '❌ Wrong text!').to_have_text('There is no results')
        expect(description_locator, '❌ Wrong description').to_have_text('Results from the load test pipeline will be displayed here')


        # ⏳
        page.wait_for_timeout(1000)
#=======================================================================================================================
