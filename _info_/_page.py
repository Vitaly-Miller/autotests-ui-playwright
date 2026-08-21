"""
<New> page
https://website.com/=NEW_PAGE=
"""
from playwright.sync_api import Page

#=======================================================================================================================
class BasePage:
    def __init__(self, page: Page):                    # Конструктор класса, принимающий Page
        self.page = page

    def open(self, url: str):
        ...


    # -------------------------------------------------- 𝌆 DATA --------------------------------------------------------
    ENDPOINT = ''
    TITLE_TEXT = ''
    HEADER_TEXT = ''

    # ----------------------------------------------- 🅔 ERROR data ----------------------------------------------------


    # ------------------------------------------------ ㉧ LOCATORS ------------------------------------------------------
    # ---- Buttons ----
    @property
    def xxx_btn(self):
        return self.page.locator('')

    # ---- Fields ----

    # ---- Errors ----


    #================================================== ✨HELPERS ======================================================
    # Open <New> page
    def open(self):
        return self.open_page(self.ENDPOINT)            # -→ <New> page                                                  https://website.com/=NEW_PAGE=
