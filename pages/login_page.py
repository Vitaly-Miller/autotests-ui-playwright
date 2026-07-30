"""
Login page
"""
from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

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


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def fill_login_form(self, email: str, password: str):
        """
        ▶ Actions:
        ----------
        - Fill Login form

        ✔ Expectations:
        ---------------
        - Email field filled
        - Password field filled

        :param email: Email
        :param password: Password
        """
        self.email_field.fill(email)
        self.password_field.fill(password)
        error_email = '❌ Email field did not fill!'
        error_password = '❌ Password field did not fill!'
        expect(self.email_field, error_email).to_have_value(email)
        expect(self.password_field, error_password).to_have_value(password)


    def click_login_btn(self):
        """
        ▶ Actions:
        ----------
        - Click Login-button

        ✔ Expectations:
        ---------------
        - Login-button is enabled
        """
        expect(self.login_btn, '❌ Login button is disabled!').to_be_enabled()
        self.login_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_header_text(self):
        """
        Check Header on the Login page

        - Header is visible
        - Header text is correct
        """
        error_visible = '❌ Header on the Login page is invisible!'
        error_text = '❌ Header text on the Login page is incorrect!'
        expect(self.header, error_visible).to_be_visible()
        expect(self.header, error_text).to_have_text(self.header_text)


    def check_wrong_email_or_password_alert(self):
        """
        Check <Wrong Email or Password> alert

        - Alert is visible
        - Alert text is correct
        """
        error_visible = '❌ Alert did not appear!'
        error_text = '❌ Incorrect alert text!'
        expect(self.wrong_email_password_alert, error_visible).to_be_visible()
        expect(self.wrong_email_password_alert, error_text).to_have_text(self.wrong_email_password_alert_text)


    def check_registration_link(self, link_url=None):
        """
        Check <Registration> link on the Login page

        - Link is enable
        - Link redirect URL is correct
        """
        error_enabled = '❌ <Registration> link on the Login page is disabled!'
        expect(self.registration_link, error_enabled).to_be_enabled()
        # ⚠️Сейчас для проверки требуется клик по ссылке. Но лучше не кликать, а проверить атрибут <href>
        # ⚠️Раскомментировать ⬇︎⬇︎⬇︎ после перехода на BASE_URL + endpoint (а то в DOM только endpoint - href="#/auth/registration")
        # registration_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        # link_url = link_url if link_url else registration_page_url      # Если <link_url> не передан
        # error_url = '❌ <Registration> link on the Login page is disabled!'
        # expect(self.registration_link, error_url).to_have_attribute('href', link_url)
#=======================================================================================================================
