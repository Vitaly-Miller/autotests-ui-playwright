"""
Login page
"""
from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage
from playwright.sync_api import Page, Locator, expect

#=======================================================================================================================
class LoginPage(BasePage):              # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        #𝌆 DATA:
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        self.header_text = 'UI Course'
        self.wrong_email_password_alert_text = 'Wrong email or password'

        # ㉧ LOCATORS (static):
        self.header = page.get_by_role(role='heading', name='UI Course')
        self.email_field = page.get_by_label('Email')
        self.password_field = page.get_by_label('Password')
        self.login_btn = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_role(role='link', name='Registration')
        self.wrong_email_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')


    # ㉧ LOCATORS {dynamic}:


    # ▶ ACTIONS:
    def fill_login_form(self, email: str, password: str):                                      # Принимает Email и Password
        self.email_field.fill(email)                                                           # Заполняет Email-поле
        self.password_field.fill(password)                                                     # Заполняет Password-поле
        expect(self.email_field, '❌ Email field did not fill!').to_have_value(email)          # Проверка - поле имеет значение из параметра <email>
        expect(self.password_field,'❌ Password field did not fill!').to_have_value(password)  # Проверка - поле имеет значение из параметра <password>


    def click_login_btn(self):
        expect(self.login_btn, '❌ Login button is disabled!').to_be_enabled()   # Проверка активного состояния кнопки
        self.login_btn.click()                                                   # Клик по кнопке



    # ✔️EXPECTATIONS:
    def check_header_text(self):
        """
        Check Header text on the Login page

        .
        """
        error = '❌ Header text on the Login page is incorrect!'
        expect(self.header, error).to_have_text(self.header_text)


    def check_wrong_email_or_password_alert(self):
        """
        Check Wrong Email or Password alert

        - Alert is visible
        - Alert text is correct
        """
        expect(self.wrong_email_password_alert, '❌ Alert did not appear!').to_be_visible()
        expect(self.wrong_email_password_alert, '❌ Incorrect alert text!').to_have_text(self.wrong_email_password_alert_text)


    def check_registration_link(self, link_url=None):
        """
        Check <Registration> link on the Login page

        - Link is enable
        - Link redirect URL is correct
        """
        error_link_disabled = '❌ <Registration> link on the Login page is disabled!'
        expect(self.registration_link, error_link_disabled).to_be_enabled()
        # ⚠️Сейчас для проверки требуется клик по ссылке. Но лучше не кликать, а проверить атрибут <href>
        # ⚠️Раскомментировать ⬇︎⬇︎⬇︎ после перехода на BASE_URL + endpoint (а то в DOM только endpoint - href="#/auth/registration")
        # registration_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        # link_url = link_url if link_url else registration_page_url      # Если <link_url> не передан
        # error_link_url = '❌ <Registration> link on the Login page is disabled!'
        # expect(self.registration_link, error_link_url).to_have_attribute('href', link_url)
#=======================================================================================================================
