"""
Login page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, Locator, expect

#=======================================================================================================================
class LoginPage(BasePage):              # Класс LoginPage (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        #--------------------------------------------- ㉧ LOCATORS (static) ---------------------------------------------
        self.email_field = page.get_by_label('Email')
        self.password_field = page.get_by_label('Password')
        self.login_btn = page.get_by_test_id('login-page-login-button')
        self.register_link = page.get_by_role(role='link', name='Registration')
        self.wrong_email_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    #---------------------------------------------- ㉧ LOCATORS (dynamic) -----------------------------------------------
    # def user(self, name) -> Locator:
    #     return self.page.get_by_label(f'User-{name}')

    #------------------------------------------------ ▶ ACTIONS --------------------------------------------------------
    # Заполнение Login-формы
    def fill_login_form(self, email: str, password: str):                  # Принимает Email и Password
        self.email_field.fill(email)                                       # Заполняет Email-поле
        expect(self.email_field,                                           # Проверка заполнения Email-поля:
               '❌ Email field did not fill!').to_have_value(email)        # - поле имеет значение из параметра <email>
        self.password_field.fill(password)                                 # Заполняет Password-поле
        expect(self.password_field,                                        # Проверка заполнения Password-поля:
               '❌ Password field did not fill!').to_have_value(password)  # - поле имеет значение из параметра <password>


    # Click <Login> button
    def click_login_btn(self):
        expect(self.login_btn,
               '❌ Login button is disabled!').to_be_enabled()       # Проверка активности кнопки <Login>
        self.login_btn.click()                                       # Клик по кнопке <Login>


    # Click <Registration> link
    def click_registration_link(self):
        self.register_link.click()                                   # Клик по <Registration> link

    #------------------------------------------------ ✔️EXPECTATIONS ---------------------------------------------------
    # Wrong Email or Password alert
    def check_wrong_email_password_alert(self):
        expect(self.wrong_email_password_alert,
               '❌ Alert did not appear!').to_be_visible()                               # Проверка видимости сообщения об ошибке
        expect(self.wrong_email_password_alert,
               '❌ Wrong alert message text!').to_have_text('Wrong email or password')   # Проверка текста сообщения об ошибке


#=======================================================================================================================
