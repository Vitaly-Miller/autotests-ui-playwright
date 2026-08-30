"""
Registration page > [Form] (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
Fields:
- Email
- Username
- Password
"""
class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # Fields names
        self.EMAIL_FIELD_NAME = 'Email'
        self.USERNAME_FIELD_NAME = 'Username'
        self.PASSWORD_FIELD_NAME = 'Password'

        # ------------------------------------ Elements (path & name) (for debug) --------------------------------------
        self.form_component = '❌ Registration page > Form'
        self.email_field_element = f'{self.form_component} > [Email field]'
        self.username_field_element = f'{self.form_component} > [Username field]'
        self.password_field_element = f'{self.form_component} > [Password field]'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.email_field_locator = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_field_locator = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_field_locator = page.get_by_test_id('registration-form-password-input').locator('input')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Registration form]
    # ────────────────────────────────────────┐
    @allure.step('▶ Fill [Registration form]')
    def fill(
            self,
            email: str,
            username: str,
            password: str
    ):
        """
        ▶ Fill [Registration form]

        - Email field - ▶ fill | ✔ value
        - Username field - ▶ fill | ✔ value
        - Password field - ▶ fill | ✔ value

        :param email: Email
        :param username: Username
        :param password: Password
        """
        self.fill_email_field(email)
        self.fill_username_field(username)
        self.fill_password_field(password)
    # ────────────────────────────────────────┘
    # Fill [Email field]
    @allure.step('▶ Fill [Email field]')
    def fill_email_field(self, email: str):
        """
        ▶ Fill [Email field]

        - ▶ Field - fill
        - ✔ Field - value

        :param email: Email
        """
        self.email_field_locator.fill(email)
        self.check_email_field_value(email)

    # Fill [Username field]
    @allure.step('▶ Fill [Username field]')
    def fill_username_field(self, username: str):
        """
        ▶ Fill [Username field]

        - ▶ Field - fill
        - ✔ Field - value

        :param username: Username
        """
        self.username_field_locator.fill(username)
        self.check_username_field_value(username)

    # Fill [Password field]
    @allure.step('▶ Fill [Password field]')
    def fill_password_field(self, password: str):
        """
        ▶ Fill [Password field]

        - ▶ Field - fill
        - ✔ Field - value

        :param password: Password
        """
        self.password_field_locator.fill(password)
        self.check_password_field_value(password)
    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Form]
    # ─────────────────────────────────────────┐
    def check_registration_form(
            self,
            email: str | None = None,
            username: str | None = None,
            password: str | None = None
    ):
        """
        ✔ Check [Registration form]

        If is passed:
        -------------
        - ✔ Email field - value
        - ✔ Username field - value
        - ✔ Password field - value

        If is NOT passed:
        ----------------
        - ✔ Email field - visible | - name
        - ✔ Username field - visible | - name
        - ✔ Password field - visible | - name

        :param email: Email (optional)
        :param username: Username (optional)
        :param password: Password (optional)
        """
        with allure.step(
                '✔ Check values of [Registration form] fields'
                if all(param is not None for param in (email, username, password))
                else '✔ Check UI of [Registration form]'
        ):
            self.check_email_field(email)
            self.check_username_field(username)
            self.check_password_field(password)
    # ─────────────────────────────────────────┘

    # [Email field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_email_field(self, email: str | None = None):
        """
        ✔ Check [Email field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name

        :param email: Email (optional)
        """
        if email is not None:
            with allure.step('✔ Check value of [Email field]'):
                self.check_email_field_value(email)
        else:
            with allure.step('✔ Check UI of [Email field]'):
                self.check_email_field_visible()
                self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Email field]')
    def check_email_field_visible(self):
        """
        ✔ Check visible [Email field]

        .
        """
        error = f'{self.email_field_element} - invisible!'
        expect(self.email_field_locator, error).to_be_visible()

    @allure.step('✔ Check name of [Email field]')
    def check_email_field_name(self):
        """
        ✔ Check name of [Email field]

        .
        """
        error = f'{self.email_field_element} - incorrect name!'
        expect(self.email_field_locator, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    @allure.step('✔ Check value of [Email field]')
    def check_email_field_value(self, email: str):
        """
        ✔ Check value of [Email field]

        :param email: Email
        """
        error = f'{self.email_field_element} - incorrect value!'
        expect(self.email_field_locator, error).to_have_value(email)


    #  [Username field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_username_field(self, username: str | None = None):
        """
        ✔ Check [Username field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name

        :param username: Username (optional)
        """
        if username is not None:
            with allure.step('✔ Check value of [Username field]'):
                self.check_username_field_value(username)
        else:
            with allure.step('✔ Check UI of [Username field]'):
                self.check_username_field_visible()
                self.check_username_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Username field]')
    def check_username_field_visible(self):
        """
        ✔ Check visible [Username field]

        .
        """
        error = f'{self.username_field_element} - invisible!'
        expect(self.username_field_locator, error).to_be_visible()

    @allure.step('✔ Check name of [Username field]')
    def check_username_field_name(self):
        """
        ✔ Check name of [Username field]

        .
        """
        error = f'{self.username_field_element} - incorrect name!'
        expect(self.username_field_locator, error).to_have_accessible_name(self.USERNAME_FIELD_NAME)

    @allure.step('✔ Check value of [Username field]')
    def check_username_field_value(self, username: str):
        """
        ✔ Check value of [Username field]

        :param username: Username
        """
        error = f'{self.username_field_element} - incorrect value!'
        expect(self.username_field_locator, error).to_have_value(username)


    #  [Password field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_password_field(self, password: str | None = None):
        """
        ✔ Check [Password field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field - name

        :param password: Password (optional)
        """
        if password is not None:
            with allure.step('✔ Check value of [Password field]'):
                self.check_password_field_value(password)
        else:
            with allure.step('✔ Check UI of [Password field]'):
                self.check_password_field_visible()
                self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Password field]')
    def check_password_field_visible(self):
        """
        ✔ Check visible [Password field]

        .
        """
        error = f'{self.password_field_element} - invisible!'
        expect(self.password_field_locator, error).to_be_visible()

    @allure.step('✔ Check name of [Password field]')
    def check_password_field_name(self):
        """
        ✔ Check name of [Password field]

        .
        """
        error = f'{self.password_field_element} - incorrect name!'
        expect(self.password_field_locator, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    @allure.step('✔ Check value of [Password field]')
    def check_password_field_value(self, password: str):
        """
        ✔ Check value of [Password field]

        :param password: Password
        """
        error = f'{self.password_field_element} - incorrect value!'
        expect(self.password_field_locator, error).to_have_value(password)


#=======================================================================================================================
