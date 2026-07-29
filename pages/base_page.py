"""
BASE PAGE
"""
from playwright.sync_api import Page

#=======================================================================================================================
class BasePage:                                            # Родительский класс
    def __init__(self, page: Page):                        # Конструктор класса, принимающий Page
        self.page = page

        #----------------------------------------------- 𝌆  BASE DATA -------------------------------------------------------

        self.registration_page_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'

    #---------------------------------------------- Базовые методы класса ----------------------------------------------
    # ⿹ Open page
    def visit(self, url: str):                             # Принимает URL-адрес страницы
        self.page.goto(url, wait_until='networkidle')  # Открыть страницу, Ожидание сети

    # Reload page
    def reload(self):
        self.page.reload(wait_until='networkidle')         # Reload courant page, Ожидание сети



#=======================================================================================================================
