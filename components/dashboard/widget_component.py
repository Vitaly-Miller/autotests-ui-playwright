"""
Dashboard page > [Widget]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page
from elements.image import Image
from elements.text import Text

#=======================================================================================================================
class DashboardWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        """
        [Widget] component

        - Title  [students | activities | courses | scores ]
        - Chart  [   bar   |    line    |   pie   | scatter]
        :param page: Page
        :param identifier: Unique part of locator [students | activities | courses | scores ]
        :param chart_type: Unique part of locator [   bar   |     line   |   pie   | scatter]
        """
        super().__init__(page)
        self.identifier = identifier
        self.chart_type = chart_type
        self.path = f'Dashboard page > {self.identifier.capitalize()}-widget'


    # ------------------------------------------------ ㉧ LOCATORS -------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-widget-title-text')

    def chart_locator(self) -> Locator:
        return self.page.get_by_test_id(f'{self.identifier}-{self.chart_type}-chart')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.path, 'Title')

    def chart(self) -> Image:
        return Image(self.chart_locator(), self.path, f'{self.chart_type.capitalize()}-chart')


    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Widget]
    # ────────────────────────────────────────┐
    @allure.step('✔ Check [Widget]')
    def check(self, title: str):
        """
        ✔ Check [Widget]

        - ✔ Title - visible | - text
        - ✔ Chart - visible

        :param title: Title
        """
        self.check_title(title)
        self.check_chart()
    # ────────────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_title(self, title: str):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param title: Title
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

        :param title: Title
        """
        self.title().check_text(title)


    # [Chart]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Chart]')
    def check_chart(self):
        """
        ✔ Check [Chart]

        - ✔ Chart - visible
        """
        self.check_chart_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_chart_visible(self):
        """
        ✔ Check [Chart] is visible

        .
        """
        self.chart().check_visible()

#=======================================================================================================================
