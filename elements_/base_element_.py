"""
BASE element
(⚠️Page factory)
"""
from playwright.sync_api import Page, Locator, expect
from pathlib import Path

#=======================================================================================================================
"""
⚠️ Page factory️ приведен для примера. 
Зависимые файлы проекта помечены как <*_>.

НЕ ПРИВЕТСТВУЮ использование Page factory️ в связке Python + Playwright.
- локаторы Playwright уже работают лениво — элементы ищутся непосредственно перед выполнением действия
- дополнительная фабрика создаёт лишний уровень абстракции
- усложняются чтение кода, отладка и поддержка тестов
- скрывается стандартное и понятное поведение Locator
- все превращается в "синтетику"
"""
#=======================================================================================================================
class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    # -------------------------------------------------- Directories ---------------------------------------------------
    PROJECT = Path(__file__).parent.parent      # 🗂️Project ROOT/
    TESTDATA = PROJECT/'testdata'               # └─ 📁testdata/
    FILES = TESTDATA/'files'                    #    └─ 📁files/

    # --------------------------------------------------- ㉧ LOCATORS --------------------------------------------------
    # [Locator]
    def get_locator(self, nth_index: int = 0, **kwargs) -> Locator:                # принимает именованные параметры для подстановки в шаблон
        """
        ⚙ Build Locator from the self.locator template

        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        :return: Locator by .get_by_test_id
        """
        locator = self.locator.format(**kwargs)                              # подставляет значения в шаблон локатора
        locator_get_by_test_id = self.page.get_by_test_id(locator).nth(nth_index)  # создаёт локатор по data-testid c ntx-index
        return locator_get_by_test_id

    # ---------------------------------------------------- ▶ ACTIONS ---------------------------------------------------
    # [Click]
    def click(self, nth_index: int = 0, **kwargs):               # принимает именованные параметры для подстановки в шаблон
        """
        ▶ Click element

        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index, **kwargs)     # инициализация локатора
        locator.click()                                    # Playwright action

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Visible]
    def check_visible(self, nth_index: int = 0, **kwargs):       # принимает именованные параметры для подстановки в шаблон
        """
        ✔ Check element is visible

        :param nth_index: nth-index
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index, **kwargs)     # инициализация локатора
        error = '❌Element - invisible!'
        expect(locator, error).to_be_visible()             # Playwright expect

    # [Text]
    def check_text(self, element_text: str, nth_index: int = 0, **kwargs):  # принимает текст и именованные параметры для подстановки в шаблон
        """
        ✔ Check element text

        :param nth_index: nth-index
        :param element_text: Expected element text
        :param kwargs: Additional named parameters for create locator
        """
        locator = self.get_locator(nth_index, **kwargs)                # инициализация локатора
        error = '❌Element - incorrect text!'
        expect(locator, error).to_have_text(element_text)             # Playwright expect


#=======================================================================================================================
