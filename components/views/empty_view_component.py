"""
Empty view
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.icon import Icon
from elements.text import Text

#=======================================================================================================================
"""
[Empty view]:
- Icon
- Title
- Description
"""
class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, path: str):
        """
        :param page: Page
        :param identifier: Unique part of locator (courses-list | create-course-preview | create-course-exercises)
        :param path: Component navigate-path
        """
        super().__init__(page)

        # 𝌆 DATA (dynamic)
        self.identifier = identifier.capitalize().replace('-', ' ')    # for logging

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.icon_locator = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title_locator = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description_locator = page.get_by_test_id(f'{identifier}-empty-view-description-text')

        # ---------------------------------------------- ◈ ELEMENTS ----------------------------------------------------
        self.path = f'{path} > {self.identifier} > Empty view'
        self.icon = Icon(self.icon_locator, self.path, 'Icon')
        self.title = Text(self.title_locator, self.path, 'Title')
        self.description = Text(self.description_locator, self.path, 'Description')

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
        self.icon.check_visible()


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
        self.title.check_visible()

    # Text
    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title text
        """
        self.title.check_text(title)


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
        self.description.check_visible()

    # Text
    def check_description_text(self, description: str):
        """
        ✔ Check [Description] text

        :param description: Description text
        """
        self.description.check_text(description)

#=======================================================================================================================
