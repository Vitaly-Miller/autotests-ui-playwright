"""
Empty view
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page
from elements.icon import Icon
from elements.text import Text

#=======================================================================================================================
class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, path: str, identifier: str):
        """
        [Empty view] component

        - Icon
        - Title
        - Description

        :param page: Page
        :param identifier: Unique part of locator ['courses-list', 'create-course-preview', 'create-course-exercises']
        :param path: Component navigate-path
        """
        super().__init__(page)

        self.identifier = identifier
        self.path = f'{path} > {self.identifier.capitalize().replace('-', ' ')} > Empty view'


    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def icon_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-empty-view-icon')

    def title_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-empty-view-title-text')

    def description_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-empty-view-description-text')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def icon(self) -> Icon:
        return Icon(self.icon_locator(), self.path, 'Icon')

    def title(self) -> Text:
        return Text(self.title_locator(), self.path, 'Title')

    def description(self) -> Text:
        return Text(self.description_locator(), self.path, 'Description')


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Empty view]
    # ─────────────────────────────────────┐
    @allure.step('✔ Check [Empty view]')
    def check(self, title: str, description: str):
        """
        ✔ Check [Empty view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text

        :param title: Title text
        :param description: Description text
        """
        self.check_icon()
        self.check_title(title)
        self.check_description(description)
    # ─────────────────────────────────────┘

    # [Icon]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Icon]')
    def check_icon(self):
        """
        ✔ Check [Icon]

        - ✔ Icon - visible
        """
        self.check_icon_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_icon_visible(self):
        """
        ✔ Check [Icon] is visible

        .
        """
        self.icon().check_visible()


    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_title(self, title: str):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param title: Title text
        """
        self.check_title_visible()
        self.check_title_text(title)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_title_visible(self):
        """
        ✔ Check [Title] is visible

        .
        """
        self.title().check_visible()

    # Text
    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title text
        """
        self.title().check_text(title)


    # [Description]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Description]')
    def check_description(self, description: str):
        """
        ✔ Check [Description]

        - ✔ Description - visible
        - ✔ Description - text

        :param description: Description text
        """
        self.check_description_visible()
        self.check_description_text(description)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_description_visible(self):
        """
        ✔ Check [Description] is visible

        .
        """
        self.description().check_visible()

    # Text
    def check_description_text(self, description: str):
        """
        ✔ Check [Description] text

        :param description: Description text
        """
        self.description().check_text(description)

#=======================================================================================================================
