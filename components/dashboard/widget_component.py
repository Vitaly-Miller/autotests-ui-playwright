"""
Dashboard page > [Widget] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
[Widget]:
- Title (students | activities | courses | scores)
- Chart (bar | line | pie | scatter)
"""

class DashboardWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        """
        :param page: Page
        :param identifier: Unique part of locator (students | activities | courses | scores)
        :param chart_type: Unique part of locator (bar | line | pie | scatter)
        """
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # Element names (for logging)
        self.widget_name = identifier.capitalize()
        self.chart_name = chart_type.capitalize()

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
        self.check_title(title)
        self.check_chart()
    # ─────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self, title: str):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Text - correct
        """
        self.check_title_visible()
        self.check_title_text(title)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self):
        """
        ✔ Check [Title] visible

        .
        """
        error = f'❌ Dashboard page > {self.widget_name}-widget > [Title] - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title
        """
        error = f'❌ Dashboard page > {self.widget_name}-widget > [Title] - incorrect text!'
        expect(self.title, error).to_have_text(title)


    # [Chart]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_chart(self):
        """
        ✔ Check [Chart]

        - ✔ Chart - visible
        """
        self.check_chart_visible()
    # ╴╴╴╴╴╴╴╴╴╴-╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_chart_visible(self):
        """
        ✔ Check [Chart] visible

        .
        """
        error = f'❌ Dashboard page > {self.widget_name}-widget > [{self.chart_name}-chart] - invisible!'
        expect(self.chart, error).to_be_visible()


#=======================================================================================================================
