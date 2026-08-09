"""
Sidebar List Component
"""
"""
<Button>
  - [Icon]
  - [Title]
  - [Title text]
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
class SidebarListComponent(BaseComponent):
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
    def click_btn(self):
        """
        Click <Sidebar List component [Button]>

        - ✔ Button - click
        """
        self.btn.click()

    # ------------------------------------------------ ✔️EXPECTATIONS --------------------------------------------------
    # ──────────────────────────────────┐
    def check_btn(self, title: str):
        """
        Check <Sidebar List component [Button]>

        - ✔ Button - visible
        - ✔ Button Icon - visible
        - ✔ Button Title - visible | Text - correct
        """
        self.check_btn_visible()
        self.check_btn_icon_visible()
        self.check_btn_title_visible()
        self.check_btn_title_text(title)
    # ──────────────────────────────────┘
    def check_btn_visible(self):
        """
        Check <Sidebar List component [Button]> - visible

        - ✔ Button - visible
        """
        error = '❌ Check <Sidebar List component [Button]> - invisible!'
        expect(self.btn, error).to_be_visible()

    def check_btn_icon_visible(self):
        """
        Check <Sidebar List component [Button Icon]> - visible

        - ✔ Icon - visible
        """
        error = '❌ Check <Sidebar List component [Button Icon]> - invisible!'
        expect(self.btn_icon, error).to_be_visible()

    def check_btn_title_visible(self):
        """
        Check <Sidebar List component [Button Title]> - visible

        - ✔ Title - visible
        """
        error = '❌ Check <Sidebar List component [Button Title]> - invisible!'
        expect(self.btn_title, error).to_be_visible()

    def check_btn_title_text(self, title: str):
        """
        Check <Sidebar List component [Button Title text]> - correct

        - ✔ Text - correct

        :param title: Title
        """
        error = '❌ Check <Sidebar List component [Button Title text]> - incorrect!'
        expect(self.btn_title, error).to_have_text(title)


#=======================================================================================================================
