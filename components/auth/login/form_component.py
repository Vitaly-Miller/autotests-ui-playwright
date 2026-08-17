"""
Login page > [Form] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


#=======================================================================================================================
"""
[Form]:
- Email
- Password
"""
class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.EMAIL_FIELD_NAME = 'Email'
        self.PASSWORD_FIELD_NAME = 'Password'

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.email_field = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_field = page.get_by_test_id('login-form-password-input').locator('input')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Login form]
    # ─────────────────────────────────────────────────┐
    def fill_login_form(
            self,
            email: str | None = None,
            password: str | None = None
    ):
        """
        ▶ Fill [Login form] fields

        - ▶ Email field - fill
        - ▶ Password field - fill

        :param email: Email (optional)
        :param password: Password (optional)
        """
        self.fill_email_field(email)
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
    def check_form(
            self,
            email: str | None = None,
            password: str | None = None
    ):
        """
        ✔ Check [Form]

        If is passed:
        -------------
        - ✔ Email field - filled correctly
        - ✔ Password field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Email field - visible | - name
        - ✔ Password field - visible | - names

        :param email: Email (optional)
        :param password: Password (optional)
        """
        self.check_email_field(email)
        self.check_password_field(password)
    # ──────────────────────────────────────┘

    # [Email field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_email_field(self, email: str | None = None):
        """
        ✔ Check [Email field]

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct

        :param email: Email (optional)
        """
        if email is not None:
            self.check_email_field_filled_correctly(email)
        else:
            self.check_email_field_visible()
            self.check_email_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_email_field_visible(self):
        """
        ✔ Check [Email field] visible

        .
        """
        error = f'❌ Login page > Form > [Email field] - invisible!'
        expect(self.email_field, error).to_be_visible()

    def check_email_field_name(self):
        """
        ✔ Check [Email field] name

        .
        """
        error = f'❌ Login page > Form > [Email field] - incorrect name!'
        expect(self.email_field, error).to_have_accessible_name(self.EMAIL_FIELD_NAME)

    def check_email_field_filled_correctly(self, email: str):
        """
        ✔ Check [Email field] filled correctly

        :param email: Email
        """
        error = f'❌ Login page > Form > [Email field] - filled incorrectly!'
        expect(self.email_field, error).to_have_value(email)


    #  [Password field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_password_field(self, password: str | None = None):
        """
        ✔ Check [Password field]>

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        ----------------
        - ✔ Field - visible
        - ✔ Field name - correct

        :param password: Password (optional)
        """
        if password is not None:
            self.check_password_field_filled_correctly(password)
        else:
            self.check_password_field_visible()
            self.check_password_field_name()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_password_field_visible(self):
        """
        ✔ Check [Password field] visible

        .
        """
        error = f'❌ Login page > Form > [Password field] - invisible!'
        expect(self.password_field, error).to_be_visible()

    def check_password_field_name(self):
        """
        ✔ Check [Password field] name

        .
        """
        error = f'❌ Login page > Form > [Password field] - incorrect name!'
        expect(self.password_field, error).to_have_accessible_name(self.PASSWORD_FIELD_NAME)

    def check_password_field_filled_correctly(self, password: str):
        """
        ✔ Check [Password field] filled correctly

        :param password: Password
        """
        error = f'❌ Login page > Form > [Password field] - filled incorrectly!'
        expect(self.password_field, error).to_have_value(password)


#=======================================================================================================================
