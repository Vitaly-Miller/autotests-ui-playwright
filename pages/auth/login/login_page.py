"""
Login page
"""
import allure

from config import Endpoint
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Locator, Page
from components.auth.login.form_component import LoginFormComponent
from elements.text import Text

#=======================================================================================================================
class LoginPage(BasePage):              # Дочерний класс (наследует класс BasePage)
    """
    [Login page]

    - Title
    - Login button
    - Login form (component)
    - Registration link
    - Wrong email or password alert
    """
    URL = Endpoint.LOGIN
    PATH = 'Login page'                 # for logging

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ⿳ COMPONENTS
        self.form = LoginFormComponent(page)


    # ---------------------------------------------------- ㉧ LOCATORS --------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('authentication-ui-course-title-text')

    def login_btn_locator(self) -> Locator:
        return self.page.get_by_test_id('login-page-login-button')

    def reg_link_locator(self) -> Locator:
        return self.page.get_by_test_id('login-page-registration-link')

    def alert_locator(self) -> Locator:
        return self.page.get_by_test_id('login-page-wrong-email-or-password-alert')

    # ------------------------------------------------- ◈ ELEMENTS -------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.PATH, 'Title')

    def login_btn(self) -> Button:
        return Button(self.login_btn_locator(), self.PATH, 'Login button')

    def reg_link(self) -> Link:
        return Link(self.reg_link_locator(), self.PATH, 'Registration link')

    def alert(self) -> Text:
        return Text(self.alert_locator(), self.PATH, 'Alert')

    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------
    # Click [Login button]
    def click_login_btn(self):
        """
        ▶ Click [Login button]

        .
        """
        self.login_btn().click()

    # Click [Registration link]
    def click_registration_link(self):
        """
        ▶ Click [Registration link]

        .
        """
        self.reg_link().click()

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
        - ✔ Login form - UI / values (if is passed)
        - ✔ Login button - disabled / enabled
        - ✔ Registration link - visible | - text | - URL

        :param email: Email (optional)
        :param password: Password (optional)
        :param is_login_button_enabled: False/True
        """
        self.check_title()
        self.form.check(email=email, password=password)
        self.check_login_btn(enabled=is_login_button_enabled)
        self.check_registration_link()
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
        ✔ Check [Title] visible

        .
        """
        self.title().check_visible()

    # Text
    def check_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        self.title().check_text(text='UI Course')


    # [Login button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴-╴╴╴╴╴╴┐
    @allure.step('✔ Check [Login button]')
    def check_login_btn(self, enabled: bool = False):
        """
        ✔ Check [Login button]

        - ✔ Button - visible
        - ✔ Button - enabled / disabled
        - ✔ Button - text

        :param enabled: True/False
        """
        self.check_login_btn_visible()
        if enabled:
            self.check_login_btn_enabled()
        else:
            self.check_login_btn_disabled()
        self.check_login_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_login_btn_visible(self):
        """
        ✔ Check [Login button] is visible

        .
        """
        self.login_btn().check_visible()

    # Enabled
    def check_login_btn_enabled(self):
        """
        ✔ Check [Login button] is enabled

        (If the Login form is completed successfully)
        """
        self.login_btn().check_enabled()

    # Disabled
    def check_login_btn_disabled(self):
        """
        ✔ Check [Login button] disabled

        (If the Login form is NOT completed successfully)
        """
        self.login_btn().check_disabled()

    # Text
    def check_login_btn_text(self):
        """
        ✔ Check [Login button] text

        .
        """
        self.login_btn().check_text(text='Login')


    # [Registration link]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Registration link]')
    def check_registration_link(self):
        """
        ✔ Check [Registration link]

        - ✔ Link - visible
        - ✔ Link - text
        - ✔ Link - URL
        """
        self.check_reg_link_visible()
        self.check_reg_link_text()
        self.check_reg_link_href()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_reg_link_visible(self):
        """
        ✔ Check [Registration link] is visible

        .
        """
        self.reg_link().check_visible()

    # Text
    def check_reg_link_text(self):
        """
        ✔ Check [Registration link] text

        .
        """
        self.reg_link().check_text(text='Registration')

    # href
    def check_reg_link_href(self):
        """
        ✔ Check [Registration link] "href" url-attribute

        .
        """
        from pages.auth.registration.registration_page import RegistrationPage   # import conflict
        self.reg_link().check_href(href=RegistrationPage.URL)


    # [Alert]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Alert]')
    def check_alert(self):
        """
        ✔ Check [Alert]

        - ✔ Alert - visible
        - ✔ Alert - text
        """
        self.check_alert_visible()
        self.check_alert_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_alert_visible(self):
        """
        ✔ Check [Alert] is visible

        .
        """
        self.alert().check_visible()

    # Text
    def check_alert_text(self):
        """
        ✔ Check [Alert] text

        .
        """
        self.alert().check_text(text='Wrong email or password')


#=======================================================================================================================
