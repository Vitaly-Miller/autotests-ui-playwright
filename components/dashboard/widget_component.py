"""
Dashboard page > [Widget]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.image import Image
from elements.text import Text
from typing import Literal

#=======================================================================================================================
"""
[Widget]:
- Title  (students | activities | courses | scores )
- Chart  (   bar   |    line    |   pie   | scatter)
"""
class DashboardWidgetComponent(BaseComponent):
    Identifier = Literal['students', 'activities', 'courses', 'scores'] # Type of accepted identifiers
    ChartType = Literal['bar', 'line', 'pie', 'scatter']                # Type of accepted chart types

    def __init__(self, page: Page, identifier: Identifier, chart_type: ChartType):
        """
        :param page: Page
        :param identifier: Unique part of locator (students | activities | courses | scores )
        :param chart_type: Unique part of locator (   bar   |     line   |   pie   | scatter)
        """
        super().__init__(page)

        # 𝌆 DATA (dynamic)
        self.widget_name = identifier.capitalize()   # for logging
        self.chart_name = chart_type.capitalize()    # for logging

        # ------------------------------------------------ ㉧ LOCATORS -------------------------------------------------
        self.title_locator = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart_locator = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

        # ---------------------------------------------- ◈ ELEMENTS ----------------------------------------------------
        self.path = f'Dashboard page > {self.widget_name}-widget'
        self.title = Text(self.title_locator, self.path, 'Title')
        self.chart = Image(self.chart_locator, self.path, f'{self.chart_name}-chart')

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Widget]
    # ─────────────────────────────────┐
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
    # ─────────────────────────────────┘

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
        self.title.check_visible()

    # Text
    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title
        """
        self.title.check_text(title)


    # [Chart]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Chart]')
    def check_chart(self):
        """
        ✔ Check [Chart]

        - ✔ Chart - visible
        """
        self.check_chart_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_chart_visible(self):
        """
        ✔ Check [Chart] is visible

        .
        """
        self.chart.check_visible()

#=======================================================================================================================
