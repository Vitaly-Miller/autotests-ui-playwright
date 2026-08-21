"""
Registration page
"""

from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.auth.registration.form_component import RegistrationFormComponent

#=======================================================================================================================
class RegistrationPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        # [Title]
        self.TITLE_TEXT = 'UI Course'
        # [Registration button]
        self.REGISTRATION_BTN_TEXT = 'Registration'
        # [Login link]
        self.LOGIN_LINK_TEXT = 'Login'
        self.LOGIN_LINK_URL = '#/auth/login'

        # ----------------------------------------------- ⿳ COMPONENTS ------------------------------------------------
        # <Registration form>
        self.form = RegistrationFormComponent(page)

        # -----------------------------------------------╴ ㉧ LOCATORS -------------------------------------------------
        # [Title]
        self.title = page.get_by_test_id('authentication-ui-course-title-text')
        # [Registration button]
        self.registration_btn = page.get_by_test_id('registration-page-registration-button')
        # [Login link]
        self.login_link = page.get_by_test_id('registration-page-login-link')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Registration button]
    def click_registration_btn(self):
        """
        ▶ Click <Registration> button

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_registration_btn(enable=True)
        self.registration_btn.click()

    # [Login link]
    def click_login_link(self):
        """
        ▶ Click <Login link>

        - ✔ Link - visible | - text | URL - correct
        - ▶ Link - click
        """
        self.check_login_link()
        self.login_link.click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Page]
    # ──────────────────────────────────────┐
    def check(self):
        """
        ✔ Check [Registration page] elements

        - ✔ Title - visible | - text
        - ✔ Registration form (unfilled)
        - ✔ Registration button - disabled
        - ✔ Login link - visible | - text | - URL
        """
        self.check_title()
        self.form.check_registration_form()
        self.check_registration_btn()
        self.check_login_link()
    # ──────────────────────────────────────┘

    # [Title]
    # # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
        error = f'❌ Registration page > [Title] - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'❌ Registration page > [Title] - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # [Registration button]
    # # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_registration_btn(self, enable: bool = False):
        """
        ✔ Check [Registration button]

        - ✔ Button - enabled / disabled
        - ✔ Button text - correct

        :param enable: True / False
        """
        if enable:
            self.check_registration_btn_enable()
        else:
            self.check_registration_btn_disable()
        self.check_registration_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_registration_btn_enable(self):
        """
        ✔ Check [Registration button] enabled

        (If the Registration form is completed successfully)
        """
        error = f'❌ Registration page > [Registration button] - disabled!'
        expect(self.registration_btn, error).to_be_enabled()

    def check_registration_btn_disable(self):
        """
        ✔ Check [Registration button] disabled

        (If the Registration form is NOT completed successfully)
        """
        error = f'❌ Registration page > [Registration button] - enabled!'
        expect(self.registration_btn, error).to_be_disabled()

    def check_registration_btn_text(self):
        """
        ✔ Check [Registration button] text

        .
        """
        error = f'❌ Registration page > [Registration button] - incorrect text!'
        expect(self.registration_btn, error).to_have_text(self.REGISTRATION_BTN_TEXT)


    # [Login link]
    # # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_login_link(self):
        """
        ✔ Check [Login link]

        - ✔ Link - visible
        - ✔ Link text - correct
        - ✔ Link URL - correct
        """
        self.check_login_link_visible()
        self.check_login_link_text()
        self.check_login_link_url()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_login_link_visible(self):
        """
        ✔ Check [Login link] visible

        .
        """
        error = f'❌ Registration page > [Login link] - invisible!'
        expect(self.login_link, error).to_be_visible()

    def check_login_link_text(self):
        """
        ✔ Check [Login link] text

        .
        """
        error = f'❌ Registration page > [Login link] - incorrect text!'
        expect(self.login_link, error).to_have_text(self.LOGIN_LINK_TEXT)

    def check_login_link_url(self):
        """
        ✔ Check [Login link] URL

        .
        """
        error = f'❌ Registration page > [Login link] - incorrect URL!'
        expect(self.login_link, error).to_have_attribute('href', self.LOGIN_LINK_URL)


    def check_login_link_redirect(self):
        """
        ✔ Check [Login link] redirect to Login page

        .
        """
        login_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        self.check_current_url(login_page_url)

#=======================================================================================================================
