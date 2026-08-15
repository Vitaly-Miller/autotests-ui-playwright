"""
Empty view (component)
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
Elements:
- Icon
- Title
- Description
"""
class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        """
        :param page: Page
        :param identifier: Unique part of locator (courses-list | create-course-preview | create-course-exercises)
        """
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.identifier = identifier.capitalize()   # for logging

        # ---------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Empty view]
    # ──────────────────────────────────────────────────────┐
    def check_empty_view(self, title: str, description: str):
        """
        ✔ Check <Empty view>

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text

        :param title: Title text
        :param description: Description text
        """
        self.check_icon_visible()
        self.check_title(title)
        self.check_description(description)
    # ──────────────────────────────────────────────────────┘

    # Empty view [Icon]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_icon(self):
        """
        ✔ Check [Icon]

        - ✔ Icon - visible
        """
        self.check_icon_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_icon_visible(self):
        """
        ✔ Check [Icon] visible

        .
        """
        error = f'❌ {self.identifier} > Empty view > [Icon] - invisible!'
        expect(self.icon, error).to_be_visible()


    # Empty view [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self, title: str):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Text - correct

        :param title: Title
        """
        self.check_title_visible()
        self.check_title_text(title)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self):
        """
        ✔ Check [Title] visible

        .
        """
        error = f'❌ {self.identifier} > Empty view > [Title] - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title text
        """
        error = f'❌ {self.identifier} > Empty view > [Title] - incorrect text!'
        expect(self.title, error).to_have_text(title)


    # Empty view [Description]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_description(self, description: str):
        """
        ✔ Check [Description]

        - ✔ Description - visible
        - ✔ Text - correct

        :param description: Description text
        """
        self.check_description_visible()
        self.check_description_text(description)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_description_visible(self):
        """
        ✔ Check [Description] visible

        .
        """
        error = f'❌ {self.identifier} > Empty view > [Description] - invisible!'
        expect(self.description, error).to_be_visible()

    def check_description_text(self, description: str):
        """
        ✔ Check [Description] text

        :param description: Description
        """
        error = f'❌ {self.identifier} > Empty view > [Description] - incorrect text!'
        expect(self.description, error).to_have_text(description)

#=======================================================================================================================
