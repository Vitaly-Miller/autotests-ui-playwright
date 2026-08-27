"""
Login page (🔔Experimental)
"""
import allure
from pages.base_page import BasePage
from playwright.sync_api import Page
from components.auth.login.form_component import LoginFormComponent
from tools.check_element import Check

#=======================================================================================================================
"""
[Login page]:
- Title
- Login button
- Login form (component)
- Registration link
- Wrong email or password alert
"""
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

        # ----------------------------------------------- ⿳ COMPONENTS ------------------------------------------------
        self.form = LoginFormComponent(page)

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.element_path = 'Login page'
        self.title_element = 'Title'
        self.login_btn_element = 'Login button'
        self.registration_link_element = 'Registration link'
        self.wrong_email_or_password_alert_element = 'Wrong email or password alert'

        # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------
        self.title_locator = page.get_by_test_id('authentication-ui-course-title-text')
        self.login_btn_locator = page.get_by_test_id('login-page-login-button')
        self.registration_link_locator = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert_locator = page.get_by_test_id('login-page-wrong-email-or-password-alert')


    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------
    # Click [Login button]
    @allure.step('▶ Click [Login button]')
    def click_login_btn(self):
        """
        ▶ Click [Login button]

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_login_btn(enabled=True)
        self.login_btn_locator.click()

    # Click [Registration link]
    @allure.step('▶ Click [Registration link]')
    def click_registration_link(self):
        """
        ▶ Click [Registration link]

        - ✔ Link - visible | - text | - URL
        - ▶ Link - click
        """
        self.check_registration_link()
        self.registration_link_locator.click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Login page]
    # ──────────────────────────────────┐
    @allure.step('✔ Check [Login page]')
    def check(
            self,
            email: str | None = None,
            password: str | None = None,
            is_login_button_enabled: bool = False
    ):
        """
        ✔ Check [Login page]

        - ✔ Title - visible | - text
        - ✔ Login form - UI / values
        - ✔ Login button - disabled / enabled
        - ✔ Registration link - visible | - text | - URL

        :param email: Email (optional)
        :param password: Password (optional)
        :param is_login_button_enabled: False/True
        """
        self.check_title()
        self.form.check_login_form(email=email, password=password)
        self.check_login_btn(enabled=is_login_button_enabled)
        self.check_registration_link()
    # ──────────────────────────────────┘

    # [Title]
    def check_title(self):
        Check.element(
            locator=self.title_locator,
            element_path=self.element_path,
            element_name=self.title_element,
            visible=True,
            text=self.TITLE_TEXT
        )

    # [Login button]
    def check_login_btn(self, enabled: bool):
        Check.element(
            locator=self.login_btn_locator,
            element_path=self.element_path,
            element_name=self.login_btn_element,
            visible=True,
            enabled=enabled,
            text=self.LOGIN_BTN_TEXT
        )

    # [Registration link]
    def check_registration_link(self):
        Check.element(
            locator=self.registration_link_locator,
            element_path=self.element_path,
            element_name=self.registration_link_element,
            visible=True,
            text=self.REGISTRATION_LINK_TEXT,
            attribute_type='href',
            attribute_value=self.REGISTRATION_LINK_URL
        )

    # [Alert]
    def check_wrong_email_or_password_alert(self):
        Check.element(
            locator=self.wrong_email_or_password_alert_locator,
            element_path=self.element_path,
            element_name=self.wrong_email_or_password_alert_element,
            visible=True,
            text=self.ALERT_TEXT
        )

#=======================================================================================================================
