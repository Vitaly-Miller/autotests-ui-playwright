"""
Registration page
"""

from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.registration.form_component import RegistrationFormComponent

#=======================================================================================================================
class RegistrationPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.TITLE_TEXT = 'UI Course'

        self.REGISTRATION_BTN_TEXT = 'Registration'
        self.LOGIN_LINK_TEXT = 'Login'
        self.LOGIN_LINK_URL = '#/auth/login'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        self.registration_form = RegistrationFormComponent(page)

        # -----------------------------------------------╴ ㉧ LOCATORS -------------------------------------------------
        # Title
        self.title = page.get_by_test_id('authentication-ui-course-title-text')

        # Buttons/Links
        self.registration_btn = page.get_by_role(role='button', name='Registration')
        self.login_link = page.get_by_role(role='link', name='Login')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------


    def click_registration_btn(self):
        """
        ▶ Click <Registration> button of the Registration page

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_registration_btn()
        self.registration_btn.click()


    def click_login_link(self):
        """
        ▶ Click <Login link> of the Registration page

        - ✔ Link - visible | - text | URL - correct
        - ▶ Link - click
        """
        self.check_login_link()
        self.login_link.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ALL Elements
    # ───────────────────────────────────────────┐
    def check_all_elements(self):
        """
        ✔ Check ALL Elements of the Registration page

        - ✔ Title
        - ✔ Registration Form (unfilled)
        - ✔ Registration button - disabled
        - ✔ Login link
        """
        self.check_title()
        self.registration_form.check_form()
        self.check_registration_btn(enable=False)
        self.check_login_link()
    # ───────────────────────────────────────────┘

    # Title
    # ──────────────────────────────┐
    def check_title(self):
        """
        ✔ Check <Title> of the Registration page

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        self.check_title_visible()
        self.check_title_text()
    # ──────────────────────────────┘
    def check_title_visible(self):
        """
        ✔ Check <Title> of the Registration page - visible

        - ✔ Title - visible
        """
        error = f'❌ <Title> of the Registration page - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self):
        """
        ✔ Check <Title text> of the Registration page - correct!

        - ✔ Text - correct
        """
        error = f'❌ <Title text> of the Registration page - incorrect!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # Registration button:
    # ────────────────────────────────────────────────────┐
    def check_registration_btn(self, enable: bool = True):
        """
        ✔ Check <Registration button> of the Registration page

        - ✔ Button - enabled / disabled
        - ✔ Button text - correct
        """
        if enable:
            self.check_registration_btn_enable()
        else:
            self.check_registration_btn_disable()
        self.check_registration_btn_text()
    # ────────────────────────────────────────────────────┘
    def check_registration_btn_enable(self):
        """
        ✔ Check <Registration button> of the Registration page - enabled!

        - ✔ Button - enabled
        """
        error = f'❌ <Registration button> of the Registration page - disabled!'
        expect(self.registration_btn, error).to_be_enabled()

    def check_registration_btn_disable(self):
        """
        ✔ Check <Registration button> of the Registration page - disabled!

        (Until the Registration form is completed successfully)

        - ✔ Button - disabled
        """
        error = f'❌ <Registration button> of the Registration page - enabled!'
        expect(self.registration_btn, error).to_be_disabled()

    def check_registration_btn_text(self):
        """
        ✔ Check <Registration button text> of the Registration page - correct

        - ✔ Button text - correct
        """
        error = f'❌ <Registration button text> of the Registration page - incorrect!'
        expect(self.registration_btn, error).to_have_text(self.REGISTRATION_BTN_TEXT)


    # Login Link:
    # ───────────────────────────────────┐
    def check_login_link(self):
        """
        ✔ Check <Login> link of the Registration page

        - ✔ Link - visible
        - ✔ Link text - correct
        - ✔ Link URL - correct
        """
        self.check_login_link_visible()
        self.check_login_link_text()
        self.check_login_link_url()
    # ───────────────────────────────────┘
    def check_login_link_visible(self):
        """
        ✔ Check <Login link> of the Registration page - visible

        - ✔ Link - visible
        """
        error = f'❌ <Login link> of the Registration page - invisible!'
        expect(self.login_link, error).to_be_visible()

    def check_login_link_text(self):
        """
        ✔ Check <Login link text> of the Registration page - correct

        - ✔ Link text - correct
        """
        error = f'❌ <Login link text> of the Registration page - incorrect!'
        expect(self.login_link, error).to_have_text(self.LOGIN_LINK_TEXT)

    def check_login_link_url(self):
        """
        ✔ Check <Login link> URL on the Registration page - correct

        - ✔ Link URL - correct
        """
        error = f'❌ <Login link> URL of the Registration page - incorrect!'
        expect(self.login_link, error).to_have_attribute('href', self.LOGIN_LINK_URL)

#=======================================================================================================================
