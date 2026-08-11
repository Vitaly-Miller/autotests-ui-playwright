"""
Empty View Component
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
        - courses-list
        - create-course-preview
        - create-course-exercises

        :param page: Page
        :param identifier: Unique component locator identifier
        """
        super().__init__(page)

        # ---------------------------------------- ㉧ LOCATORS (semi-dynamic) -------------------------------------------
        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ══════════════════════════════════════════════════════╗
    def check_component(self, title: str, description: str):
        """
        Check <Empty View> component

        - ✔ Icon - visible
        - ✔ Title - visible | Text - correct
        - ✔ Description - visible | Text - correct

        :param title: Title text
        :param description: Description text
        """
        self.check_icon_visible()
        self.check_title(title)
        self.check_description(description)
    # ══════════════════════════════════════════════════════╝

    # Icon
    def check_icon_visible(self):
        """
        Check [Icon] of the <Empty View> component - visible

        - ✔ Icon - visible
        """
        error = f'❌ [Icon] of the <Empty View> component - invisible!'
        expect(self.icon, error).to_be_visible()

    # Title
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self, title: str):
        """
        Check [Title] of the <Empty View> component

        - ✔ Title - visible
        - ✔ Text - correct

        :param title: Title text
        """
        self.check_title_visible()
        self.check_title_text(title)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self):
        """
        Check [Title] of the <Empty View> component - visible

        - ✔ Title - visible
        """
        error = f'❌ [Title] of the <Empty View> component - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self, title: str):
        """
        Check [Title text] of the <Empty View> component - correct

        - ✔ Text - correct

        :param title: Title text
        """
        error = f'❌ [Title text] of the <Empty View> component> - incorrect!'
        expect(self.title, error).to_have_text(title)

    # Description
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_description(self, description: str):
        """
        Check [Description] of the <Empty View> component

        - ✔ Description - visible
        - ✔ Text - correct

        :param description: Description text
        """
        self.check_description_visible()
        self.check_description_text(description)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_description_visible(self):
        """
        Check [Description] of the <Empty View> component - visible

        - ✔ Description - visible
        """
        error = f'❌ [Description] of the <Empty View> component - invisible!'
        expect(self.description, error).to_be_visible()

    def check_description_text(self, description: str):
        """
        Check [Description text] of the <Empty View> component - correct

        - ✔ Text - correct

        :param description: Description text
        """
        error = f'❌ [Description text] of the <Empty View> component - incorrect!'
        expect(self.description, error).to_have_text(description)

#=======================================================================================================================
