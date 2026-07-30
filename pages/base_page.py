"""
BASE PAGE
"""
from playwright.sync_api import Page

#=======================================================================================================================
class BasePage:                                 # Родительский класс
    def __init__(self, page: Page):             # Конструктор класса, принимающий page
        self.page = page

        # 𝌆 BASE DATA:


    # BASE METHODS:
    def visit(self, url: str):
        """
        ⿹ Open page

        :param url: URL
        """
        self.page.goto(url=url)


    def reload(self):
        """
        ↺ Reload courant page

        .
        """
        self.page.reload()

#=======================================================================================================================
