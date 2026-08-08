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
    email_field = page.get_by_role('textbox', name='Email')
    username_field = page.get_by_role('textbox', name='Username')
    password_field = page.get_by_role('textbox', name='Password')
    registration_btn = page.get_by_role("button", name='Registration')
    dashboard_header = page.get_by_role('heading', name='Dashboard')
    navbar_header = page.get_by_test_id('navigation-navbar-app-title-text')
    navbar_welcome_title = page.get_by_test_id('navigation-navbar-welcome-title-text')


    # ✔️EXPECTATIONS (before filling out)
    expect(registration_btn).to_be_disabled()           # v.1 - Button is disabled    (by default)
    expect(registration_btn).not_to_be_enabled()        # v.2 - Button is NOT enabled (by default)                       <— ⚠️ анти-паттерн (двойное отрицание)

    # ▶ ACTIONS (filling out)
    email_field.fill('user.name@gmail.com')
    username_field.fill('username')
    password_field.fill('password')

    # ✔️EXPECTATIONS (after filling out)
    expect(registration_btn).to_be_enabled()            # v.1 - Button is enabled      (after filling out)
    expect(registration_btn).not_to_be_disabled()       # v.2 - Button is NOT disabled (after filling out)               <— ⚠️ анти-паттерн (двойное отрицание)


    # ▶ ACTIONS (after filling out)
    registration_btn.click()                                     # Click Registration button

    # ✔️EXPECTATIONS (after click registration button)
    expect(page).to_have_url(dashboard_url)                      # Check Page URL
    expect(navbar_header).to_have_text('UI Course')              # Check Navbar header text
    expect(navbar_welcome_title).to_contain_text('Welcome,')     # Check Navbar welcome text contains "Welcome,"
    expect(dashboard_header).to_have_text('Dashboard')           # Check Dashboard header text

    # ⏳(optional)
    page.wait_for_timeout(1000)
#=======================================================================================================================
