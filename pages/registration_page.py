"""
Registration page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class RegistrationPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # 𝌆 DATA:
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        self.header_text = 'UI Course'

        # ㉧ LOCATORS (static):
        self.header = page.get_by_role(role='heading', name='UI Course')
        self.email_field = page.get_by_role(role='textbox', name='Email')
        self.username_field = page.get_by_role(role='textbox', name='Username')
        self.password_field = page.get_by_role(role='textbox', name='Password')
        self.registration_btn = page.get_by_role(role='button', name='Registration')
        self.login_link = page.get_by_role(role='link', name='Login')

    # ㉧ LOCATORS {dynamic}:


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def fill_registration_form(self, email: str, username: str, password: str):
        """
        ▶ Actions:
        ----------
        - Fill Registration form

        ✔ Expectations:
        ---------------
        - Email field filled
        - Username field filled
        - Password field filled

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.email_field.fill(email)
        self.username_field.fill(username)
        self.password_field.fill(password)
        error_email = '❌ Email field did not fill!'
        error_username = '❌ Username field did not fill!'
        error_password = '❌ Password field did not fill!'
        expect(self.email_field, error_email).to_have_value(email)
        expect(self.username_field, error_username).to_have_value(username)
        expect(self.password_field, error_password).to_have_value(password)


    def click_registration_btn(self):
        """
        ▶ Actions:
        ----------
        - Click Registration-button

        ✔ Expectations:
        ---------------
        - Registration-button is enabled
        """
        error_enabled = '❌ Registration button is disabled!'
        expect(self.registration_btn, error_enabled).to_be_enabled()
        self.registration_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_header(self):
        """
        Check Header on the Registration page

        - Header is visible
        - Header text is correct

        """
        error_visible = '❌ Header is invisible on the Registration page'
        error_text = '❌ Header text on the Registration page is incorrect!'
        expect(self.header, error_visible).to_be_visible()
        expect(self.header, error_text).to_have_text(self.header_text)


    def check_login_link(self, link_url=None):
        """
        Check <Login> link on the Registration page

        - Link is enable
        - Link redirect URL is correct
        .
        """
        error_enabled = '❌ <Login> link on the Registration page is disabled!'
        expect(self.login_link, error_enabled).to_be_enabled()
        # ⚠️Сейчас для проверки требуется клик по ссылке. Но лучше не кликать, а проверить атрибут <href>
        # ⚠️Раскомментировать ⬇︎⬇︎⬇︎ после перехода на BASE_URL + endpoint (а то в DOM только endpoint - href="#/auth/login")
        # login_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        # link_url = link_url if link_url else login_page_url                      # Если <link_url> не передан
        # error_url = '❌ <Login> link on the Registration page has incorrect URL'
        # expect(self.login_link, error_url).to_have_attribute('href', link_url)


    def check_redirect_page_url_after_successful_registration(self, redirect_url=None):
        """
        Check redirect URL after successful registration

        :param redirect_url: New page URL

        """
        dashboard_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        redirect_url = redirect_url if redirect_url else dashboard_page_url      # Если <redirect_url> не передан
        error_url = '❌ Incorrect redirection URL after successful registration!'
        expect(self.page, error_url).to_have_url(redirect_url)

#=======================================================================================================================
