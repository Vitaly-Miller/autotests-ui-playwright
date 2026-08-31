"""
Registration page
"""
import allure
from elements.button import Button
from elements.link import Link
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Locator, Page
from components.auth.registration.form_component import RegistrationFormComponent

#=======================================================================================================================
"""
[Registration page]:
- Title
- Registration form (component)
- Registration button
- Login link
"""
class RegistrationPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
    path = 'Registration page'

    # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
    TITLE_TEXT = 'UI Course'
    REGISTRATION_BTN_TEXT = 'Registration'
    LOGIN_LINK_TEXT = 'Login'
    LOGIN_LINK_HREF = '#/auth/login'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ----------------------------------------------- ⿳ COMPONENTS ------------------------------------------------
        self.form = RegistrationFormComponent(page)

    # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('authentication-ui-course-title-text')

    def registration_btn_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-page-registration-button')

    def login_link_locator(self) -> Locator:
        return self.page.get_by_test_id('registration-page-login-link')

    # ------------------------------------------------- ◈ ELEMENTS -------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.path, 'Title')

    def registration_btn(self) -> Button:
        return Button(self.registration_btn_locator(), self.path, 'Registration button')

    def login_link(self) -> Link:
        return Link(self.login_link_locator(), self.path, 'Login link')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Registration button]
    def click_registration_btn(self):
        """
        ▶ Click [Registration button]

        .
        """
        self.registration_btn().click()

    # Click [Login link]
    def click_login_link(self):
        """
        ▶ Click [Login link]

        .
        """
        self.login_link().click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Registration page]
    # ──────────────────────────────────┐
    @allure.step('✔ Check [Registration page]')
    def check(
            self,
            email: str | None = None,
            username: str | None = None,
            password: str | None = None,
            is_registration_button_enabled: bool = False
    ):
        """
        ✔ Check [Registration page]

        - ✔ Title - visible | - text
        - ✔ Registration form - UI / values
        - ✔ Registration button - disabled / enabled
        - ✔ Login link - visible | - text | - URL

        :param email: Email (optional)
        :param username: Username (optional)
        :param password: Password (optional)
        :param is_registration_button_enabled: False/True
        """
        self.check_title()
        self.form.check(email=email, username=username, password=password)
        self.check_registration_btn(enabled=is_registration_button_enabled)
        self.check_login_link()
    # ──────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.check_title_visible()
        self.check_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_title_visible(self):
        """
        ✔ Check [Title] is visible

        .
        """
        self.title().check_visible()

    # Text
    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        self.title().check_text(text=self.TITLE_TEXT)


    # [Registration button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Registration button]')
    def check_registration_btn(self, enabled: bool = False):
        """
        ✔ Check [Registration button]

        - ✔ Button - visible
        - ✔ Button - enabled / disabled
        - ✔ Button - text

        :param enabled: True/False
        """
        self.check_registration_btn_visible()
        if enabled:
            self.check_registration_btn_enabled()
        else:
            self.check_registration_btn_disabled()
        self.check_registration_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_registration_btn_visible(self):
        """
        ✔ Check [Registration button] is visible

        .
        """
        self.registration_btn().check_visible()

    # Enabled
    def check_registration_btn_enabled(self):
        """
        ✔ Check [Registration button] is enabled

        (If the Registration form is completed successfully)
        """
        self.registration_btn().check_enabled()

    # Disabled
    def check_registration_btn_disabled(self):
        """
        ✔ Check [Registration button] disabled

        (If the Registration form is NOT completed successfully)
        """
        self.registration_btn().check_disabled()

    # Text
    def check_registration_btn_text(self):
        """
        ✔ Check [Registration button] text

        .
        """
        self.registration_btn().check_text(text=self.REGISTRATION_BTN_TEXT)


    # [Login link]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Login link]')
    def check_login_link(self):
        """
        ✔ Check [Login link]

        - ✔ Link - visible
        - ✔ Link - text
        - ✔ Link - URL
        """
        self.check_login_link_visible()
        self.check_login_link_text()
        self.check_login_link_href()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_login_link_visible(self):
        """
        ✔ Check [Login link] is visible

        .
        """
        self.login_link().check_visible()

    # Text
    def check_login_link_text(self):
        """
        ✔ Check [Login link] text

        .
        """
        self.login_link().check_text(text=self.LOGIN_LINK_TEXT)

    # href
    def check_login_link_href(self):
        """
        ✔ Check [Login link] "href" url-attribute

        .
        """
        self.login_link().check_href(href=self.LOGIN_LINK_HREF)

    # Redirect
    @allure.step('✔ Check [Login link] redirect to Login page')
    def check_login_link_redirect(self):
        """
        ✔ Check [Login link] redirect to Login page

        .
        """
        login_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        self.check_current_url(login_page_url)

#=======================================================================================================================
