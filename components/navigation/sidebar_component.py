"""
Sidebar (component)
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar_item_component import SidebarItemComponent

#=======================================================================================================================
"""
Elements:
- Dashboard button (component)
- Courses button (component)
- Logout button (component)
"""
class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ----------------------------------------------- 𝌆 DATA -------------------------------------------------------
        # Identifiers
        self.DASHBOARD_IDENTIFIER = 'dashboard'
        self.COURSES_IDENTIFIER = 'courses'
        self.LOGOUT_IDENTIFIER = 'logout'

        # Titles
        self.DASHBOARD_TITLE = 'Dashboard'
        self.COURSES_TITLE = 'Courses'
        self.LOGOUT_TITLE = 'Logout'

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
        self.dashboard_btn = SidebarItemComponent(page=page, identifier=self.DASHBOARD_IDENTIFIER)
        self.courses_btn = SidebarItemComponent(page=page, identifier=self.COURSES_IDENTIFIER)
        self.logout_btn = SidebarItemComponent(page=page, identifier=self.LOGOUT_IDENTIFIER)

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_dashboard_btn(self):
        """
        ▶ Click <Sidebar [Dashboard button]>

        - Button - ✔ visible -> ▶ click
        """
        self.dashboard_btn.click_btn()

    def click_courses_btn(self):
        """
        ▶ Click <Sidebar [Courses button]>

        - Button - ✔ visible -> ▶ click
        """
        self.courses_btn.click_btn()

    def click_logout_btn(self):
        """
        ▶ Click <Sidebar [Logout button]>

        - Button - ✔ visible -> ▶ click
        """
        self.logout_btn.click_btn()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_sidebar(self):
        """
        ✔ Check [Sidebar]

        - ✔ Dashboard button - visible | Icon - visible | Title - visible | - text
        - ✔ Courses button - visible | Icon - visible | Title - visible | - text
        - ✔ Logout button - visible | Icon - visible | Title - visible | - text
        """
        self.dashboard_btn.check_component(self.DASHBOARD_TITLE)
        self.courses_btn.check_component(self.COURSES_TITLE)
        self.logout_btn.check_component(self.LOGOUT_TITLE)


#=======================================================================================================================
