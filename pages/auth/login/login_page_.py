"""
Login page
(⚠️Page factory)
"""



from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.auth.login.form_component import LoginFormComponent
from elements_.button_ import Button
from elements_.link_ import Link
from elements_.text_ import Text

#=======================================================================================================================
class LoginPage(BasePage):              # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        # [Title]

        self.TITLE_TEXT = 'UI Course'
        # [Login button]
        self.LOGIN_BTN_TEXT = 'Login'
        # [Registration link]
        self.REGISTRATION_LINK_TEXT = 'Registration'
        self.REGISTRATION_LINK_URL = '#/auth/registration'
        # [Alerts]
        self.ALERT_TEXT = 'Wrong email or password'

        # ----------------------------------------------- ⿳ COMPONENTS ------------------------------------------------
        # <Form>
        self.form = LoginFormComponent(page)

        # ----------------------------------------- ㉧ LOCATORS (⚠️Page factory) ---------------------------------------
        # [Title]
        self.title_locator = Text(page, 'authentication-ui-course-title-text', 'Title')
        # [Login button]
        self.login_btn_locator = Button(page, 'login-page-login-button', 'Login')
        # [Registration link]
        self.registration_link_locator = Link(page, 'login-page-registration-link', 'Registration')
        # [Alert]
        self.wrong_email_or_password_alert_locator = Text(page,'login-page-wrong-email-or-password-alert', 'Wrong email or password')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Login button]
    def click_login_btn(self):
        """
        ▶ Click [Login button]

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_login_btn(enabled=True)
        self.login_btn_locator.click()

    # [Registration link]
    def click_registration_link(self):
        """
        ▶ Click [Registration link]

        - ✔ Link - visible | - text | - URL
        - ▶ Link - click
        """
        self.check_registration_link()
        self.registration_link_locator.click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Page]
    # ────────────────────────────────┐
    def check(self):
        """
        ✔ Check [Login page] elements

        - ✔ Title - visible | - text
        - ✔ Login Form (unfilled)
        - ✔ Login button - disabled
        - ✔ Registration link - visible | - text | - URL
        """
        self.check_title()
        self.form.check_login_form()
        self.check_login_btn()
        self.check_registration_link()
    # ────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.check_title_visible()
        self.check_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self):
        """
        ✔ Check visible [Title]

        .
        """
        error = f'❌ Login page > [Title] - invisible!'
        expect(self.title_locator, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check text of [Title]

        .
        """
        error = f'❌ Login page > [Title] - incorrect text!'
        expect(self.title_locator, error).to_have_text(self.TITLE_TEXT)


    # [Login button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_login_btn(self, enabled: bool = False):
        """
        ✔ Check [Login button]

        - ✔ Button - enabled / disabled
        - ✔ Button - text

        :param enabled: True/False
        """
        if enabled:
            self.check_login_btn_enabled()
        else:
            self.check_login_btn_disabled()
        self.check_login_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_login_btn_enabled(self):
        """
        ✔ Check enabled [Login button]

        (If the Login form is completed successfully)
        """
        error = f'❌ Login page > [Login button] - disabled!'
        expect(self.login_btn_locator, error).to_be_enabled()

    def check_login_btn_disabled(self):
        """
        ✔ Check disabled [Login button]

        (If the Login form is NOT completed successfully)
        """
        error = f'❌ Login page > [Login button] - enabled!'
        expect(self.login_btn_locator, error).to_be_disabled()

    def check_login_btn_text(self):
        """
        ✔ Check text of [Login button]

        .
        """
        error = f'❌ Login page > [Login button] - incorrect text!'
        expect(self.login_btn_locator, error).to_have_text(self.LOGIN_BTN_TEXT)


    # [Registration link]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_registration_link(self):
        """
        ✔ Check <Registration link

        - ✔ Link - visible
        - ✔ Link - text
        - ✔ Link URL - correct
        """
        self.check_registration_link_visible()
        self.check_registration_link_text()
        self.check_registration_link_url()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_registration_link_visible(self):
        """
        ✔ Check visible [Registration link]

        .
        """
        error = f'❌ Login page > [Registration link] - invisible!'
        expect(self.registration_link_locator, error).to_be_visible()

    def check_registration_link_text(self):
        """
        ✔ Check text of [Registration link]

        .
        """
        error = f'❌ Login page > [Registration link] - incorrect text!'
        expect(self.registration_link_locator, error).to_have_text(self.REGISTRATION_LINK_TEXT)

    def check_registration_link_url(self):
        """
        ✔ Check [Registration link] URL

        .
        """
        error = f'❌ Login page > [Registration link] - incorrect URL!'
        expect(self.registration_link_locator, error).to_have_attribute('href', self.REGISTRATION_LINK_URL)


    # [Alert]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert_locator.check_visible()
        self.wrong_email_or_password_alert_locator.check_text(self.ALERT_TEXT)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘



#=======================================================================================================================
