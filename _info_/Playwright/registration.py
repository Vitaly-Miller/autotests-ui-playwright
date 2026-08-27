"""
Playwright Registration
"""
from playwright.sync_api import sync_playwright, expect

#=======================================================================================================================
registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
dashboard_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'

# Создаем объект playwright через контекст менеджер <with> - для авто-закрытия браузера по окончании
with sync_playwright() as playwright:                        # Создаем объект playwright = sync_playwright() (инициализация)
    browser = playwright.chromium.launch(headless=False)     # Создаем объект браузера chromium (с отображением)
    page = browser.new_page()                                # Создаем объект страницы page

    # ⿹ Open page
    page.goto(registration_url)

    # ㉧ LOCATORS
    email_field_locator = page.get_by_role('textbox', name='Email')
    username_field_locator = page.get_by_role('textbox', name='Username')
    password_field_locator = page.get_by_role('textbox', name='Password')
    registration_btn_locator = page.get_by_role("button", name='Registration')
    dashboard_header_locator = page.get_by_role('heading', name='Dashboard')
    navbar_header_locator = page.get_by_test_id('navigation-navbar-app-title-text')
    navbar_welcome_title_locator = page.get_by_test_id('navigation-navbar-welcome-title-text')


    # ✔️EXPECTATIONS (before filling out)
    expect(registration_btn_locator).to_be_disabled()           # v.1 - Button is disabled    (by default)
    expect(registration_btn_locator).not_to_be_enabled()        # v.2 - Button is NOT enabled (by default)                       <— ⚠️ анти-паттерн (двойное отрицание)

    # ▶ ACTIONS (filling out)
    email_field_locator.fill('user.name@gmail.com')
    username_field_locator.fill('username')
    password_field_locator.fill('password')

    # ✔️EXPECTATIONS (after filling out)
    expect(registration_btn_locator).to_be_enabled()            # v.1 - Button is enabled      (after filling out)
    expect(registration_btn_locator).not_to_be_disabled()       # v.2 - Button is NOT disabled (after filling out)               <— ⚠️ анти-паттерн (двойное отрицание)


    # ▶ ACTIONS (after filling out)
    registration_btn_locator.click()                                     # Click Registration button

    # ✔️EXPECTATIONS (after click registration button)
    expect(page).to_have_url(dashboard_url)                      # ✔ Check Page URL
    expect(navbar_header_locator).to_have_text('UI Course')              # ✔ Check Navbar header text
    expect(navbar_welcome_title_locator).to_contain_text('Welcome,')     # ✔ Check Navbar welcome text contains "Welcome,"
    expect(dashboard_header_locator).to_have_text('Dashboard')           # ✔ Check Dashboard header text

    # ⏳(optional)
    page.wait_for_timeout(1000)
#=======================================================================================================================
