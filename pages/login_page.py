"""
Login page
"""

from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.login.form_component import LoginFormComponent

#=======================================================================================================================
class LoginPage(BasePage):              # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.TITLE_TEXT = 'UI Course'
        self.LOGIN_BTN_TEXT = 'Login'
        self.REGISTRATION_LINK_TEXT = 'Registration'
        self.REGISTRATION_LINK_URL = '#/auth/registration'
        self.ALERT_TEXT = 'Wrong email or password'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        self.login_form = LoginFormComponent(page)

        # ------------------------------------------ ㉧ LOCATORS (static) -----------------------------------------------
        # Title
        self.title = page.get_by_test_id('authentication-ui-course-title-text')

        # Buttons/Links
        self.login_btn = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')

        # Alerts
        self.wrong_email_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_login_btn(self):
        """
        ▶ Click <Login button> of the Login page

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_login_btn()
        self.login_btn.click()


    def click_registration_link(self):
        """
        ▶ Click <Registration link> of the Login page

        - ✔ Link - visible | - text | URL - correct
        - ▶ Link - click
        """
        self.check_registration_link()
        self.registration_link.click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Page
    # ───────────────────────────────────┐
    def check_page(self):
        """
        ✔ Check ALL Elements of the Login page

        - ✔ Title
        - ✔ Login Form (unfilled)
        - ✔ Login button - disabled
        - ✔ Registration link
        """
        self.check_title()
        self.login_form.check_form()
        self.check_login_btn(enable=False)
        self.check_registration_link()
    # ────────────────────────────────────┘

    # Title
    # ─────────────────────────────┐
    def check_title(self):
        """
        ✔ Check <Title> of the Registration page

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        self.check_title_visible()
        self.check_title_text()
    # ─────────────────────────────┘
    def check_title_visible(self):
        """
        ✔ Check <Title> of the Login page - visible

        - ✔ Title - visible
        """
        error = f'❌ <Title> of the Login page - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check <Title text> of the Login page - correct

        - ✔ Text - correct
        """
        error = f'❌ <Title text> of the Login page - incorrect!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


  # Login button:
    # ─────────────────────────────────────────────┐
    def check_login_btn(self, enable: bool = True):
        """
        ✔ Check <Login button> of the Login page

        - ✔ Button - enabled / disabled
        - ✔ Button text - correct
        """
        if enable:
            self.check_login_btn_enable()
        else:
            self.check_login_btn_disabled()
        self.check_login_btn_text()
    # ─────────────────────────────────────────────┘
    def check_login_btn_enable(self):
        """
        ✔ Check <Login button> of the Login page - enabled

        - ✔ Button - enabled
        """
        error = f'❌ <Login button> of the Login page - disabled!'
        expect(self.login_btn, error).to_be_enabled()

    def check_login_btn_disabled(self):
        """
        ✔ Check <Login button> of the Login page - disabled

        (Until the Login form is completed successfully)

        - ✔ Button - disabled
        """
        error = f'❌ <Login button> of the Login page - enabled!'
        expect(self.login_btn, error).to_be_disabled()

    def check_login_btn_text(self):
        """
        ✔ Check <Login button text> of the Login page - correct

        - ✔ Text - correct
        """
        error = f'❌ <Login button text> of the Login page - incorrect!'
        expect(self.login_btn, error).to_have_text(self.LOGIN_BTN_TEXT)


    # Registration Link:
    # ────────────────────────────────────────┐
    def check_registration_link(self):
        """
        ✔ Check <Registration link> of the Login page

        - ✔ Link - visible
        - ✔ Link text - correct
        - ✔ Link URL - correct
        """
        self.check_registration_link_visible()
        self.check_registration_link_text()
        self.check_registration_link_url()
    # ────────────────────────────────────────┘
    def check_registration_link_visible(self):
        """
        ✔ Check <Registration link> of the Login page - visible

        - ✔ Link - visible
        """
        error = f'❌ <Registration link> of the Login page - invisible!'
        expect(self.registration_link, error).to_be_visible()

    def check_registration_link_text(self):
        """
        ✔ Check <Registration link text> of the Login page - correct

        - ✔ Text - correct
        """
        error = f'❌ <Registration link text> of the Login page - incorrect!'
        expect(self.registration_link, error).to_have_text(self.REGISTRATION_LINK_TEXT)

    def check_registration_link_url(self):
        """
        ✔ Check <Registration link [URL]> on the Login page - correct

        - ✔ URL - correct
        """
        error = f'❌ <Registration link [URL]> of the Login page - incorrect!'
        expect(self.registration_link, error).to_have_attribute('href', self.REGISTRATION_LINK_URL)


    # Alert:
    # ────────────────────────────────────────────────────┐
    def wrong_email_or_password_alert(self):
        """
        ✔ Check <Wrong Email or Password> alert of the Login page

        - ✔ Alert - visible
        - ✔ Alert text - correct
        """
        self.check_wrong_email_or_password_alert_visible()
        self.check_wrong_email_or_password_alert_text()
    # ────────────────────────────────────────────────────┘
    def check_wrong_email_or_password_alert_visible(self):
        """
        ✔ Check <Wrong Email or Password alert> - visible

        - ✔ Alert - visible
        """
        error = f'❌ <Wrong Email or Password alert> - invisible!'
        expect(self.wrong_email_password_alert, error).to_be_visible()

    def check_wrong_email_or_password_alert_text(self):
        """
        ✔ Check <Wrong Email or Password alert> text - correct

        - ✔ Text - correct
        """
        error = f'❌ <Wrong Email or Password alert text> - incorrect!'
        expect(self.wrong_email_password_alert, error).to_have_text(self.ALERT_TEXT)



#=======================================================================================================================
