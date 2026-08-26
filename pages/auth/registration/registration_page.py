"""
Registration page
"""
import allure

from pages.base_page import BasePage
from playwright.sync_api import Page, expect
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

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.TITLE_TEXT = 'UI Course'
        self.REGISTRATION_BTN_TEXT = 'Registration'
        self.LOGIN_LINK_TEXT = 'Login'
        self.LOGIN_LINK_URL = '#/auth/login'

        # ----------------------------------------------- ⿳ COMPONENTS ------------------------------------------------
        self.form = RegistrationFormComponent(page)

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.registration_page_component = '❌ Registration page'
        self.title_element = f'{self.registration_page_component} > [Title]'
        self.registration_btn_element = f'{self.registration_page_component} > [Registration button]'
        self.login_link_element = f'{self.registration_page_component} > [Login link]'

        # ------------------------------------------------ ㉧ LOCATORS --------------------------------------------------
        self.title = page.get_by_test_id('authentication-ui-course-title-text')
        self.registration_btn = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Registration button]
    @allure.step('▶ Click [Registration button]')
    def click_registration_btn(self):
        """
        ▶ Click [Registration button]

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_registration_btn(enable=True)
        self.registration_btn.click()

    # Click [Login link]
    @allure.step('▶ Click [Login link]')
    def click_login_link(self):
        """
        ▶ Click [Login link]

        - ✔ Link - visible | - text | - URL
        - ▶ Link - click
        """
        self.check_login_link()
        self.login_link.click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Registration page]
    # ──────────────────────────────────┐
    @allure.step('✔ Check [Registration page]')
    def check(
            self,
            email: str | None = None,
            username: str | None = None,
            password: str | None = None,
            is_registration_button_enable: bool = False
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
        :param is_registration_button_enable: False/True
        """
        self.check_title()
        self.form.check_registration_form(email=email, username=username, password=password)
        self.check_registration_btn(enable=is_registration_button_enable)
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
    @allure.step('✔ Check visible [Title]')
    def check_title_visible(self):
        """
        ✔ Check visible [Title]

        .
        """
        error = f'{self.title_element} - invisible!'
        expect(self.title, error).to_be_visible()

    @allure.step('✔ Check text of [Title]')
    def check_title_text(self):
        """
        ✔ Check text of [Title]

        .
        """
        error = f'{self.title_element} - incorrect text!'
        expect(self.title, error).to_have_text(self.TITLE_TEXT)


    # [Registration button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Registration button]')
    def check_registration_btn(self, enable: bool = False):
        """
        ✔ Check [Registration button]

        - ✔ Button - visible
        - ✔ Button - enabled / disabled
        - ✔ Button - text

        :param enable: True/False
        """
        self.check_registration_btn_visible()
        if enable:
            self.check_registration_btn_enable()
        else:
            self.check_registration_btn_disable()
        self.check_registration_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Registration button]')
    def check_registration_btn_visible(self):
        """
        ✔ Check visible [Registration button]

        .
        """
        error = f'{self.registration_btn_element} - invisible!'
        expect(self.registration_btn, error).to_be_visible()

    @allure.step('✔ Check enabled [Registration button]')
    def check_registration_btn_enable(self):
        """
        ✔ Check enabled [Registration button]

        (If the Registration form is completed successfully)
        """
        error = f'{self.registration_btn_element} - disabled!'
        expect(self.registration_btn, error).to_be_enabled()

    @allure.step('✔ Check [Registration button] is disable')
    def check_registration_btn_disable(self):
        """
        ✔ Check disabled [Registration button]

        (If the Registration form is NOT completed successfully)
        """
        error = f'{self.registration_btn_element} - enabled!'
        expect(self.registration_btn, error).to_be_disabled()

    @allure.step('✔ Check text of [Registration button]')
    def check_registration_btn_text(self):
        """
        ✔ Check text of [Registration button]

        .
        """
        error = f'{self.registration_btn_element} - incorrect text!'
        expect(self.registration_btn, error).to_have_text(self.REGISTRATION_BTN_TEXT)


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
        self.check_login_link_url()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Login link]')
    def check_login_link_visible(self):
        """
        ✔ Check visible [Login link]

        .
        """
        error = f'{self.login_link_element} - invisible!'
        expect(self.login_link, error).to_be_visible()

    @allure.step('✔ Check text of [Login link]')
    def check_login_link_text(self):
        """
        ✔ Check text of [Login link]

        .
        """
        error = f'{self.login_link_element} - incorrect text!'
        expect(self.login_link, error).to_have_text(self.LOGIN_LINK_TEXT)

    @allure.step('✔ Check [Login link] URL')
    def check_login_link_url(self):
        """
        ✔ Check [Login link] URL

        .
        """
        error = f'{self.login_link_element} - incorrect URL!'
        expect(self.login_link, error).to_have_attribute('href', self.LOGIN_LINK_URL)

    @allure.step('✔ Check [Login link] redirect to Login page')
    def check_login_link_redirect(self):
        """
        ✔ Check [Login link] redirect to Login page

        .
        """
        login_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        self.check_current_url(login_page_url)



#=======================================================================================================================
