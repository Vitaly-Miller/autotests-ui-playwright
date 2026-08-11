"""
Sidebar Component
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar_item_component import SidebarItemComponent

#=======================================================================================================================
"""
Elements:
- Dashboard Item (component)
- Courses Item (component)
- Logout Item (component)
"""
class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # Identifiers
        self.DASHBOARD_IDENTIFIER = 'dashboard'
        self.COURSES_IDENTIFIER = 'courses'
        self.LOGOUT_IDENTIFIER = 'logout'

        # Titles
        self.DASHBOARD_TITLE = 'Dashboard'
        self.COURSES_TITLE = 'Courses'
        self.LOGOUT_TITLE = 'Logout'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        self.dashboard_item = SidebarItemComponent(page=page, identifier=self.DASHBOARD_IDENTIFIER)
        self.courses_item = SidebarItemComponent(page=page, identifier=self.COURSES_IDENTIFIER)
        self.logout_item = SidebarItemComponent(page=page, identifier=self.LOGOUT_IDENTIFIER)

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_dashboard_item(self):
        """
        Click <Sidebar [Dashboard Item]>

        - Item - ✔ visible | ▶ click
        """
        self.dashboard_item.click_item()

    def click_courses_item(self):
        """
        Click <Sidebar [Courses Item]>

        - Item - ✔ visible | ▶ click
        """
        self.courses_item.click_item()

    def click_logout_item(self):
        """
        Click <Sidebar [Logout Item]>

        - Item - ✔ visible | ▶ click
        """
        self.logout_item.click_item()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_component(self):
        """
        Check <Sidebar> component

        - ✔ Dashboard Item - visible | Icon - visible | Title - visible | Text - correct
        - ✔ Courses Item - visible | Icon - visible | Title - visible | Text - correct
        - ✔ Logout Item - visible | Icon - visible | Title - visible | Text - correct
        """
        self.dashboard_item.check_component(self.DASHBOARD_TITLE)
        self.courses_item.check_component(self.COURSES_TITLE)
        self.logout_item.check_component(self.LOGOUT_TITLE)


#=======================================================================================================================
