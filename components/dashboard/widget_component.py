"""
Dashboard page > [Widget] (component)
"""
import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
[Widget]:
- Title  (students | activities | courses | scores )
- Chart  (   bar   |    line    |   pie   | scatter)
"""

class DashboardWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        """
        :param page: Page
        :param identifier: Unique part of locator (students | activities | courses | scores )
        :param chart_type: Unique part of locator (   bar   |     line   |   pie   | scatter)
        """
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # Element names (for logging)
        self.widget_name = identifier.capitalize()
        self.chart_name = chart_type.capitalize()

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.widget_component = f'❌ Dashboard page > {self.widget_name}-widget'
        self.title_element = f'{self.widget_component} > [Title]'
        self.chart_element = f'{self.widget_component} > [{self.chart_name}-chart]'

        # ------------------------------------------------ ㉧ LOCATORS -------------------------------------------------
        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    # -------------------------------------------------- ✔️EXPECTATIONS ------------------------------------------------
    # [Widget]
    # ─────────────────────────────────┐
    def check_widget(self, title: str):
        """
        ✔ Check [Widget]

        - ✔ Title - visible | - text
        - ✔ Chart - visible
        """
        with allure.step(f'✔ Check [{self.widget_name}-widget]'):
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
        """
        self.check_title_visible()
        self.check_title_text(title)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Title] is visible')
    def check_title_visible(self):
        """
        ✔ Check [Title] is visible

        .
        """
        error = f'{self.title_element} - invisible!'
        expect(self.title, error).to_be_visible()

    @allure.step('✔ Check [Title] text')
    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title
        """
        error = f'{self.title_element} - incorrect text!'
        expect(self.title, error).to_have_text(title)


    # [Chart]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_chart(self):
        """
        ✔ Check [Chart]

        - ✔ Chart - visible
        """
        with allure.step(f'✔ Check [{self.chart_name}-chart]'):
            self.check_chart_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_chart_visible(self):
        """
        ✔ Check [Chart] is visible

        .
        """
        with allure.step(f'✔ Check [{self.chart_name}-chart] is visible'):
            error = f'{self.chart_element} - invisible!'
            expect(self.chart, error).to_be_visible()


#=======================================================================================================================
