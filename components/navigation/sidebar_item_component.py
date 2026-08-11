"""
Sidebar List Component
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
Item elements:
- Icon
- Title
- Title text
"""
class SidebarItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        """
        - dashboard
        - courses
        - logout

        :param page: Page
        :param identifier: Unique component locator identifier
        """
        super().__init__(page)

        # -------------------------------------- ㉧ LOCATORS (semi-dynamic) ---------------------------------------------
        self.btn = page.get_by_test_id(f'{identifier}-drawer-list-item-button')
        self.btn_icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.btn_title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')

    # -------------------------------------------------- ▶ ACTIONS -----------------------------------------------------
    def click_item(self):
        """
        Click <Sidebar Item>

        - ✔ Item - visible
        - ▶ Item - click
        """
        self.check_item_visible()
        self.btn.click()

    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # ────────────────────────────────────┐
    def check_component(self, title: str):
        """
        Check ALL elements of the <Sidebar Item> component

        - ✔ Item - visible
        - ✔ Icon - visible
        - ✔ Title - visible | Text - correct

        :param title: Item title
        """
        self.check_item_visible()
        self.check_icon_visible()
        self.check_title_visible()
        self.check_title_text(title)
    # ────────────────────────────────────┘
    def check_item_visible(self):
        """
        Check <Sidebar Item> - visible

        - ✔ Button - visible
        """
        error = f'❌ Check <Sidebar Item> - invisible!'
        expect(self.btn, error).to_be_visible()

    def check_icon_visible(self):
        """
        Check <Sidebar Item [Icon]> - visible

        - ✔ Icon - visible
        """
        error = f'❌ Check <Sidebar Item [Icon]> - invisible!'
        expect(self.btn_icon, error).to_be_visible()

    def check_title_visible(self):
        """
        Check <Sidebar Item [Title]> - visible

        - ✔ Title - visible
        """
        error = f'❌ Check <Sidebar Item [Title]> - invisible!'
        expect(self.btn_title, error).to_be_visible()

    def check_title_text(self, title: str):
        """
        Check <Sidebar Item [Title text]> - correct

        - ✔ Text - correct

        :param title: Title
        """
        error = f'❌ Check <Sidebar Item [Title text]> - incorrect!'
        expect(self.btn_title, error).to_have_text(title)


#=======================================================================================================================
