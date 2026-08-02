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
        # ├ Page URL
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'


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
        - ▶ <Email> field - fill
        - ▶ <Username> field - fill
        - ▶ <Password> field - fill
        - ✔ Check <Registration form> fields filled correctly (func)

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.email_field.fill(email)
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.check_registration_form_fields_filled(email=email, username=username, password=password)


    def click_registration_btn(self):
        """
        - ✔ <Registration> Button - enabled
        - ▶ <Registration> Button - Click
        """
        expect(self.registration_btn).to_be_enabled()
        self.registration_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Form fields:
    def check_registration_form_fields_filled(self, email: str, username: str, password: str):
        """
        Check <Registration form> fields filled correctly

        - ✔ <Email> field - filled correctly
        - ✔ <Username> field - filled correctly
        - ✔ <Password> field - filled correctly

        :param email: Email
        :param username: Username
        :param password: Password
        """
        error_email = '❌ <Email> field did not fill correctly!'
        error_username = '❌ <Username> field did not fill correctly!'
        error_password = '❌ <Password> field did not fill correctly!'
        expect(self.email_field, error_email).to_have_value(email)
        expect(self.username_field, error_username).to_have_value(username)
        expect(self.password_field, error_password).to_have_value(password)


    # Toolbar:
    def check_toolbar_title(self):
        """
        Check <Toolbar title> of the Registration page

        - ✔ Title - visible
        - ✔ Title text - correct

        """
        error_visible = '❌ <Toolbar title> of the Registration page - invisible!'
        error_text = '❌ <Toolbar title> text of the Registration page - incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text('UI Course')


    # Buttons/Links:
    def check_registration_btn(self):
        """
        Check <Registration button> of the Registration page

        - ✔ Button - enabled
        - ✔ Button text - correct
        """
        error_enabled = '❌ <Registration> button of the Registration page - disabled!'
        error_text = '❌ <Registration> button text of the Registration page - incorrect!'
        expect(self.registration_btn, error_enabled).to_be_enabled()
        expect(self.registration_btn, error_text).to_have_text('Registration')


    def check_login_link(self, redirect_endpoint: str | None = None):
        """
        Check <Login> link of the Registration page

        :param redirect_endpoint: Redirection page endpoint

        - ✔ Link - enable
        - ✔ Link endpoint - correct
        """
        login_page_endpoint = '#/auth/login'
        redirect_endpoint = redirect_endpoint if redirect_endpoint else login_page_endpoint # Если <link_url> не передан
        error_enabled = '❌ <Login> link of the Registration page - disabled!'
        error_endpoint = '❌ <Login> link of the Registration page has incorrect endpoint!'
        expect(self.login_link, error_enabled).to_be_enabled()
        expect(self.login_link, error_endpoint).to_have_attribute('href', redirect_endpoint)


    def check_new_page_url_after_successful_registration(self, new_page_url: str | None = None):
        """
        Check <New page> URL after successful registration

        - ✔ URL - correct

        :param new_page_url: New page URL
        """
        dashboard_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        new_page_url = new_page_url if new_page_url else dashboard_page_url  # Если <new_page_url> не передан
        error_url = '❌ <New page> URL after successful registration - incorrect!'
        expect(self.page, error_url).to_have_url(new_page_url)

#=======================================================================================================================
