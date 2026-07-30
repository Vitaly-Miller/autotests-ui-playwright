"""
Registration page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, Locator, expect

#=======================================================================================================================
class RegistrationPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # 𝌆 DATA:
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
        self.header_text = 'UI Course'

        # ㉧ LOCATORS (static):
        self.header = page.get_by_role(role='heading', name='UI Course')
        self.email_field = page.get_by_role(role='textbox', name='Email')
        self.username_field = page.get_by_role(role='textbox', name='Username')
        self.password_field = page.get_by_role(role='textbox', name='Password')
        self.registration_btn = page.get_by_role(role='button', name='Registration')
        self.login_link = page.get_by_role(role='link', name='Login')

    # ㉧ LOCATORS {dynamic}:


    # ▶ ACTIONS:
    def fill_registration_form(self, email: str, username: str, password: str):                 # Принимает Email, Username и Password
        self.email_field.fill(email)                                                            # Заполняет Email-поле
        self.username_field.fill(username)                                                      # Заполняет Username-поле
        self.password_field.fill(password)                                                      # Заполняет Password-поле
        expect(self.email_field, '❌ Email field did not fill!').to_have_value(email)           # - поле имеет значение из параметра <email>
        expect(self.username_field, '❌ Username field did not fill!').to_have_value(username)  # - поле имеет значение из параметра <username>
        expect(self.password_field, '❌ Password field did not fill!').to_have_value(password)  # - поле имеет значение из параметра <password>


    def click_registration_btn(self):
        expect(self.registration_btn, '❌ Registration button is disabled!').to_be_enabled()    # Проверка активного состояния кнопки
        self.registration_btn.click()                                                           # Клик по кнопке


    # ✔️EXPECTATIONS:
    def check_header_text(self):
        """
        Check Header text on the Registration page

        .
        """
        error = '❌ Header text on the Registration page is incorrect!'
        expect(self.header, error).to_have_text(self.header_text)


    def check_login_link(self, link_url=None):
        """
        Check <Login> link on the Registration page

        - Link is enable
        - Link redirect URL is correct
        .
        """
        error_link_disabled = '❌ <Login> link on the Registration page is disabled!'
        expect(self.login_link, error_link_disabled).to_be_enabled()
        # ⚠️Сейчас для проверки требуется клик по ссылке. Но лучше не кликать, а проверить атрибут <href>
        # ⚠️Раскомментировать ⬇︎⬇︎⬇︎ после перехода на BASE_URL + endpoint (а то в DOM только endpoint - href="#/auth/login")
        # login_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        # link_url = link_url if link_url else login_page_url                      # Если <link_url> не передан
        # error_link_url = '❌ <Login> link on the Registration page has incorrect URL'
        # expect(self.login_link, error_link_url).to_have_attribute('href', link_url)


    def check_redirect_page_url_after_successful_registration(self, redirect_url=None):
        """
        Check redirect URL after successful registration

        :param redirect_url: New page URL

        """
        dashboard_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
        redirect_url = redirect_url if redirect_url else dashboard_page_url      # Если <redirect_url> не передан
        error = '❌ Incorrect redirection URL after successful registration!'
        expect(self.page, error).to_have_url(redirect_url)

#=======================================================================================================================
