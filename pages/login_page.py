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
        # [Title]
        self.TITLE_TEXT = 'UI Course'
        # [Login button]
        self.LOGIN_BTN_TEXT = 'Login'
        # [Registration link]
        self.REGISTRATION_LINK_TEXT = 'Registration'
        self.REGISTRATION_LINK_URL = '#/auth/registration'
        # [Alerts]
        self.ALERT_TEXT = 'Wrong email or password'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        # <Form>
        self.form = LoginFormComponent(page)

        # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------
        # [Title]
        self.title = page.get_by_test_id('authentication-ui-course-title-text')
        # [Login button]
        self.login_btn = page.get_by_test_id('login-page-login-button')
        # [Registration link]
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        # [Alert]
        self.wrong_email_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Login button]
    def click_login_btn(self):
        """
        ▶ Click [Login button]

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_login_btn(enable=True)
        self.login_btn.click()

    # [Registration link]
    def click_registration_link(self):
        """
        ▶ Click [Registration link]

        - ✔ Link - visible | - text | - URL
        - ▶ Link - click
        """
        self.check_registration_link()
        self.registration_link.click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Page]
    # ────────────────────────────────┐
    def check_page(self):
        """
        ✔ Check [Login page] elements

        - ✔ Title - visible | - text
        - ✔ Login Form (unfilled)
        - ✔ Login button - disabled
        - ✔ Registration link - visible | - text | - URL
        """
        self.check_title()
        self.form.check_form()
        self.check_login_btn()
        self.check_registration_link()
    # ────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        self.check_title_visible()
        self.check_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self):
        """
        ✔ Check [Title] visible

        .
        """
        error = f'❌ Login page > [Title] - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'❌ Login page > [Title] - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # [Login button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_login_btn(self, enable: bool = False):
        """
        ✔ Check [Login button]

        - ✔ Button - enabled / disabled
        - ✔ Button text - correct

        :param enable: True/False
        """
        if enable:
            self.check_login_btn_enable()
        else:
            self.check_login_btn_disabled()
        self.check_login_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_login_btn_enable(self):
        """
        ✔ Check [Login button] enabled

        (If the Login form is completed successfully)
        """
        error = f'❌ Login page > [Login button] - disabled!'
        expect(self.login_btn, error).to_be_enabled()

    def check_login_btn_disabled(self):
        """
        ✔ Check [Login button] disabled

        (If the Login form is NOT completed successfully)
        """
        error = f'❌ Login page > [Login button] - enabled!'
        expect(self.login_btn, error).to_be_disabled()

    def check_login_btn_text(self):
        """
        ✔ Check [Login button] text

        .
        """
        error = f'❌ Login page > [Login button] - incorrect text!'
        expect(self.login_btn, error).to_have_text(self.LOGIN_BTN_TEXT)


    # [Registration link]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_registration_link(self):
        """
        ✔ Check <Registration link

        - ✔ Link - visible
        - ✔ Link text - correct
        - ✔ Link URL - correct
        """
        self.check_registration_link_visible()
        self.check_registration_link_text()
        self.check_registration_link_url()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_registration_link_visible(self):
        """
        ✔ Check [Registration link] visible

        .
        """
        error = f'❌ Login page > [Registration link] - invisible!'
        expect(self.registration_link, error).to_be_visible()

    def check_registration_link_text(self):
        """
        ✔ Check [Registration link] text

        .
        """
        error = f'❌ Login page > [Registration link] - incorrect text!'
        expect(self.registration_link, error).to_have_text(self.REGISTRATION_LINK_TEXT)

    def check_registration_link_url(self):
        """
        ✔ Check [Registration link] URL

        .
        """
        error = f'❌ Login page > [Registration link] - incorrect URL!'
        expect(self.registration_link, error).to_have_attribute('href', self.REGISTRATION_LINK_URL)


    # [Alert]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def wrong_email_or_password_alert(self):
        """
        ✔ Check [Wrong Email or Password alert]

        - ✔ Alert - visible
        - ✔ Alert text - correct
        """
        self.check_wrong_email_or_password_alert_visible()
        self.check_wrong_email_or_password_alert_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_wrong_email_or_password_alert_visible(self):
        """
        ✔ Check [Wrong Email or Password alert] visible

        .
        """
        error = f'❌ Login page > [Wrong Email or Password alert] - invisible!'
        expect(self.wrong_email_password_alert, error).to_be_visible()

    def check_wrong_email_or_password_alert_text(self):
        """
        ✔ Check [Wrong Email or Password alert] text

        .
        """
        error = f'❌ Login page > [Wrong Email or Password alert] - incorrect text!'
        expect(self.wrong_email_password_alert, error).to_have_text(self.ALERT_TEXT)



#=======================================================================================================================
