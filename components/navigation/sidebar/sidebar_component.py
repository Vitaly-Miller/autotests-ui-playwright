"""
Sidebar (component)
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar.sidebar_item_component import SidebarItemComponent

#=======================================================================================================================
"""
Elements:
- Dashboard item
- Courses item
- Logout item
"""
class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ----------------------------------------------- 𝌆 DATA -------------------------------------------------------
        # <Item [Identifiers]>
        self.DASHBOARD_IDENTIFIER = 'dashboard'
        self.COURSES_IDENTIFIER = 'courses'
        self.LOGOUT_IDENTIFIER = 'logout'

        # <Item [Titles]>
        self.DASHBOARD_TITLE = 'Dashboard'
        self.COURSES_TITLE = 'Courses'
        self.LOGOUT_TITLE = 'Logout'

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
        self.dashboard_item = SidebarItemComponent(page=page, identifier=self.DASHBOARD_IDENTIFIER)
        self.courses_item = SidebarItemComponent(page=page, identifier=self.COURSES_IDENTIFIER)
        self.logout_item = SidebarItemComponent(page=page, identifier=self.LOGOUT_IDENTIFIER)

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_dashboard_item(self):
        """
        ▶ Click [Dashboard item]

        - Button - ✔ visible -> ▶ click
        """
        self.dashboard_item.click_btn()

    def click_courses_item(self):
        """
        ▶ Click [Courses item]

        - Button - ✔ visible -> ▶ click
        """
        self.courses_item.click_btn()

    def click_logout_item(self):
        """
        ▶ Click [Logout item]

        - Button - ✔ visible -> ▶ click
        """
        self.logout_item.click_btn()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Sidebar]
    # ────────────────────────────────────────────────────────────┐
    def check_sidebar(self):
        """
        ✔ Check [Sidebar]

        - ✔ Dashboard item - visible | Icon - visible | Title - visible | - text
        - ✔ Courses item - visible | Icon - visible | Title - visible | - text
        - ✔ Logout item - visible | Icon - visible | Title - visible | - text
        """
        self.dashboard_item.check_item(title=self.DASHBOARD_TITLE)
        self.courses_item.check_item(title=self.COURSES_TITLE)
        self.logout_item.check_item(title=self.LOGOUT_TITLE)
    # ────────────────────────────────────────────────────────────┘


#=======================================================================================================================
