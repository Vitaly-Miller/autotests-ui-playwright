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

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.form_component = '❌ Registration page > Form'
        self.email_field_element = f'{self.form_component} > [Email field]'
        self.username_field_element = f'{self.form_component} > [Username field]'
        self.password_field_element = f'{self.form_component} > [Password field]'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.email_field = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_field = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_field = page.get_by_test_id('registration-form-password-input').locator('input')

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
        self.email_field.fill(email)
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
        self.username_field.fill(username)
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
        self.password_field.fill(password)
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
        - ✔ Password field - visible | - names

        :param email: Email (optional)
        :param username: Username (optional)
        :param password: Password (optional)
        """
        with allure.step(
                '✔ Check [Registration form] field values'
                if all(param is not None for param in (email, username, password))
                else '✔ Check [Registration form] UI'
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
            with allure.step('✔ Check [Email field] value'):
                self.check_email_field_value(email)
        else:
            with allure.step('✔ Check [Email field] UI'):
                self.check_email_field_visible()
                self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Email field] is visible')
    def check_email_field_visible(self):
        """
        ✔ Check [Email field]  is visible

        .
        """
        error = f'{self.email_field_element} - invisible!'
        expect(self.email_field, error).to_be_visible()

    @allure.step('✔ Check [Email field] name')
    def check_email_field_name(self):
        """
        ✔ Check [Email field] name

        .
        """
        error = f'{self.email_field_element} - incorrect name!'
        expect(self.email_field, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    @allure.step('✔ Check [Email field] value')
    def check_email_field_value(self, email: str):
        """
        ✔ Check [Email field] value

        :param email: Email
        """
        error = f'{self.email_field_element} - incorrect value!'
        expect(self.email_field, error).to_have_value(email)


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
            with allure.step('✔ Check [Username field] value'):
                self.check_username_field_value(username)
        else:
            with allure.step('✔ Check [Username field] UI'):
                self.check_username_field_visible()
                self.check_username_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Username field] is visible')
    def check_username_field_visible(self):
        """
        ✔ Check [Username field]  is visible

        .
        """
        error = f'{self.username_field_element} - invisible!'
        expect(self.username_field, error).to_be_visible()

    @allure.step('✔ Check [Username field] name')
    def check_username_field_name(self):
        """
        ✔ Check [Username field] name

        .
        """
        error = f'{self.username_field_element} - incorrect name!'
        expect(self.username_field, error).to_have_accessible_name(self.USERNAME_FIELD_NAME)

    @allure.step('✔ Check [Username field] value')
    def check_username_field_value(self, username: str):
        """
        ✔ Check [Username field] value

        :param username: Username
        """
        error = f'{self.username_field_element} - incorrect value!'
        expect(self.username_field, error).to_have_value(username)


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
            with allure.step('✔ Check [Password field] value'):
                self.check_password_field_value(password)
        else:
            with allure.step('✔ Check [Password field] UI'):
                self.check_password_field_visible()
                self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Password field] is visible')
    def check_password_field_visible(self):
        """
        ✔ Check [Password field]  is visible

        .
        """
        error = f'{self.password_field_element} - invisible!'
        expect(self.password_field, error).to_be_visible()

    @allure.step('✔ Check [Password field] name')
    def check_password_field_name(self):
        """
        ✔ Check [Password field] name

        .
        """
        error = f'{self.password_field_element} - incorrect name!'
        expect(self.password_field, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    @allure.step('✔ Check [Password field] value')
    def check_password_field_value(self, password: str):
        """
        ✔ Check [Password field] value

        :param password: Password
        """
        error = f'{self.password_field_element} - incorrect value!'
        expect(self.password_field, error).to_have_value(password)


#=======================================================================================================================
