"""
Registration page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class RegistrationPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ┌╴ 𝌆 DATA:
        # ├ Page
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        # ├ Toolbar
        self.toolbar_title_text = 'UI Course'

        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_role(role='heading', name='UI Course')
        # ├ Form fields
        self.email_field = page.get_by_role(role='textbox', name='Email')
        self.username_field = page.get_by_role(role='textbox', name='Username')
        self.password_field = page.get_by_role(role='textbox', name='Password')
        # ├ Buttons/Links
        self.registration_btn = page.get_by_role(role='button', name='Registration')
        self.login_link = page.get_by_role(role='link', name='Login')


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
    def check_toolbar_title(self):
        """
        Check Toolbar title on the Registration page

        - Title is visible
        - Title text is correct

        """
        error_visible = '❌ Toolbar title is invisible on the Registration page!'
        error_text = '❌ Toolbar title text on the Registration page is incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text(self.toolbar_title_text)


    def check_login_link(self, redirect_endpoint: str | None = None):
        """
        Check <Login link> on the Registration page

        :param redirect_endpoint: Redirection page endpoint (from DOM)

        - Link is enable
        - Link endpoint is correct
        """
        login_page_endpoint = '#/auth/login'
        redirect_endpoint = redirect_endpoint if redirect_endpoint else login_page_endpoint # Если <link_url> не передан
        error_enabled = '❌ <Login> link on the Registration page is disabled!'
        error_endpoint = '❌ <Login> link on the Registration page has incorrect endpoint!'
        expect(self.login_link, error_enabled).to_be_enabled()
        expect(self.login_link, error_endpoint).to_have_attribute('href', redirect_endpoint)


    def check_new_page_url_after_successful_registration(self, new_page_url: str | None = None):
        """
        Check new page URL after successful registration

        :param new_page_url: New page URL

        """
        dashboard_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        new_page_url = new_page_url if new_page_url else dashboard_page_url  # Если <new_page_url> не передан
        error_url = '❌ New page URL after successful registration is incorrect!'
        expect(self.page, error_url).to_have_url(new_page_url)

#=======================================================================================================================
