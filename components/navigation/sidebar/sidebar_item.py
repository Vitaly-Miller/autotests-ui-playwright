"""
Sidebar item (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page
from elements.button import Button
from elements.icon import Icon
from elements.text import Text

#=======================================================================================================================
class SidebarItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        """
        Sidebar item (component)

        - Button
        - Icon
        - Title

        :param page: Page
        :param identifier: Unique part of locator [dashboard, courses, logout]
        """
        super().__init__(page)

        self.identifier = identifier
        self.path = f'Sidebar > {self.identifier.capitalize()}-item'


    # ----------------------------------------- ㉧ LOCATORS (dynamic) -----------------------------------------------
    def btn_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-drawer-list-item-button')

    def icon_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-drawer-list-item-icon')

    def title_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-drawer-list-item-title-text')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def btn(self) -> Button:
        return Button(self.btn_locator(), self.path, f'{self.identifier.capitalize()}-button')

    def icon(self) -> Icon:
        return Icon(self.icon_locator(), self.path, f'{self.identifier.capitalize()}-icon')

    def title(self) -> Text:
        return Text(self.title_locator(), self.path, f'{self.identifier.capitalize()}-title')


    # -------------------------------------------------- ▶ ACTIONS -----------------------------------------------------
    # Click [Button]
    def click_btn(self):
        """
        ▶ Click [Item-button]

        .
        """
        self.btn().click()

    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # [Item]
    # ─────────────────────────────┐
    @allure.step('✔ Check [Item]')
    def check(self, title: str):
        """
        ✔ Check [Item]

        - ✔ Button
        - ✔ Icon
        - ✔ Title

        :param title: Title
        """
        self.check_btn()
        self.check_icon()
        self.check_title(title)
    # ─────────────────────────────┘

    # [Button]
    @allure.step('✔ Check [Button]')
    def check_btn(self):
        """
        ✔ Check [Button]

        - ✔ Button - visible
        """
        self.btn().check_visible()

    # [Icon]
    @allure.step('✔ Check [Icon]')
    def check_icon(self):
        """
        ✔ Check [Icon]

        - ✔ Icon - visible
        """
        self.icon().check_visible()

    # [Title]
    @allure.step('✔ Check [Title]')
    def check_title(self, title: str):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param title: Title
        """
        self.title().check_visible()
        self.title().check_text(title)


#=======================================================================================================================
