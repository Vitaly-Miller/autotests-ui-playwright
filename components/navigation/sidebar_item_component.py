"""
Sidebar list (component)
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
Elements:
- Button
- Icon
- Title
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
        self.icon = page.get_by_test_id(f'{identifier}-drawer-list-item-icon')
        self.title = page.get_by_test_id(f'{identifier}-drawer-list-item-title-text')

    # -------------------------------------------------- ▶ ACTIONS -----------------------------------------------------
    def click_btn(self):
        """
        ▶ Click Sidebar item [Button]

        - ✔ Button - visible
        - ▶ Button - click
        """
        self.check_btn_visible()
        self.btn.click()

    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # ────────────────────────────────────┐
    def check_item(self, title: str):
        """
        ✔ Check [Sidebar item]

        - ✔ Item - visible
        - ✔ Icon - visible
        - ✔ Title - visible | - text

        :param title: Item title
        """
        self.check_btn_visible()
        self.check_icon_visible()
        self.check_title_visible()
        self.check_title_text(title)
    # ────────────────────────────────────┘
    def check_btn_visible(self):
        """
        ✔ Check [Button] visible

        .
        """
        error = f'❌ Sidebar item -> [Button] - invisible!'
        expect(self.btn, error).to_be_visible()

    def check_icon_visible(self):
        """
        ✔ Check [Icon]> visible

        .
        """
        error = f'❌ Sidebar item -> [Icon] - invisible!'
        expect(self.icon, error).to_be_visible()

    def check_title_visible(self):
        """
        ✔ Check [Title] visible

        .
        """
        error = f'❌ Sidebar item -> [Title] - invisible!'
        expect(self.title, error).to_be_visible()

    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title
        """
        error = f'❌ Sidebar item -> [Title] - text incorrect!'
        expect(self.title, error).to_have_text(title)


#=======================================================================================================================
