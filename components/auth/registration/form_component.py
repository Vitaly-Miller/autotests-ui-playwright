"""
Registration page > [Form] (component)
"""
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
        self.EMAIL_FIELD_NAME = 'Email'
        self.USERNAME_FIELD_NAME = 'Username'
        self.PASSWORD_FIELD_NAME = 'Password'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.email_field = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_field = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_field = page.get_by_test_id('registration-form-password-input').locator('input')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Registration form]
    # ─────────────────────────────────────────────────┐
    def fill(
            self,
            email: str | None = None,
            username: str | None = None,
            password: str | None = None
    ):
        """
        ▶ Fill [Registration form] fields

        - ▶ Email field - fill
        - ▶ Username field - fill
        - ▶ Password field - fill

        :param email: Email (optional)
        :param username: Username (optional)
        :param password: Password (optional)
        """
        self.fill_email_field(email)
        self.fill_username_field(username)
        self.fill_password_field(password)
    # ─────────────────────────────────────────────────┘
    # Fill [Email field]
    def fill_email_field(self, email: str | None = None):
        """
        ▶ Fill [Email field]

        :param email: Email (optional)
        """
        if email is not None:
            self.email_field.fill(email)

    # Fill [Username field]
    def fill_username_field(self, username: str | None = None):
        """
        ▶ Fill [Username field]

        :param username: Username (optional)
        """
        if username is not None:
            self.username_field.fill(username)

    # Fill [Password field]
    def fill_password_field(self, password: str | None = None):
        """
        ▶ Fill [Password field]

        :param password: Password (optional)
        """
        if password is not None:
            self.password_field.fill(password)
    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Form]
    # ──────────────────────────────────────┐
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
        self.check_email_field(email)
        self.check_username_field(username)
        self.check_password_field(password)
    # ──────────────────────────────────────┘

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
            self.check_email_field_value(email)
        else:
            self.check_email_field_visible()
            self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_email_field_visible(self):
        """
        ✔ Check [Email field] visible

        .
        """
        error = f'❌ Registration page > Form > [Email field] - invisible!'
        expect(self.email_field, error).to_be_visible()

    def check_email_field_name(self):
        """
        ✔ Check [Email field] name

        .
        """
        error = f'❌ Registration page > Form > [Email field] - incorrect name!'
        expect(self.email_field, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    def check_email_field_value(self, email: str):
        """
        ✔ Check [Email field] value

        :param email: Email
        """
        error = f'❌ Registration page > Form > [Email field] - incorrect value!'
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
            self.check_username_field_value(username)
        else:
            self.check_username_field_visible()
            self.check_username_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_username_field_visible(self):
        """
        ✔ Check [Username field] visible

        .
        """
        error = f'❌ Registration page > Form > [Username field] - invisible!'
        expect(self.username_field, error).to_be_visible()

    def check_username_field_name(self):
        """
        ✔ Check [Username field] name

        .
        """
        error = f'❌ Registration page > Form > [Username field] - incorrect name!'
        expect(self.username_field, error).to_have_accessible_name(self.USERNAME_FIELD_NAME)

    def check_username_field_value(self, username: str):
        """
        ✔ Check [Username field] value

        :param username: Username
        """
        error = f'❌ Registration page > Form > [Username field] - incorrect value!'
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
            self.check_password_field_value(password)
        else:
            self.check_password_field_visible()
            self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_password_field_visible(self):
        """
        ✔ Check [Password field] visible

        .
        """
        error = f'❌ Registration page > Form > [Password field] - invisible!'
        expect(self.password_field, error).to_be_visible()

    def check_password_field_name(self):
        """
        ✔ Check [Password field] name

        .
        """
        error = f'❌ Registration page > Form > [Password field] - incorrect name!'
        expect(self.password_field, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    def check_password_field_value(self, password: str):
        """
        ✔ Check [Password field] value

        :param password: Password
        """
        error = f'❌ Registration page > Form > [Password field] - incorrect value!'
        expect(self.password_field, error).to_have_value(password)


#=======================================================================================================================
