"""
Sidebar Component [Button]
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from components.navigation.sidebar_list_component import SidebarListComponent

#=======================================================================================================================
class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ----------------------------------------------- ⿷ COMPONENTS ------------------------------------------------
        self.dashboard = SidebarListComponent(page=page, identifier='dashboard')
        self.courses = SidebarListComponent(page=page, identifier='courses')
        self.logout = SidebarListComponent(page=page, identifier='logout')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_dashboard(self):
        self.dashboard.click_btn()

    def click_course(self):
        self.courses.click_btn()

    def click_logout(self):
        self.logout.click_btn()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_sidebar(self):
        """
        Check <Sidebar>

        - ✔ Dashboard Button - visible | Icon - visible | Title - visible | Text - correct
        - ✔ Courses Button - visible | Icon - visible | Title - visible | Text - correct
        - ✔ Logout Button - visible | Icon - visible | Title - visible | Text - correct
        """
        self.dashboard.check_btn('Dashboard')
        self.courses.check_btn('Courses')
        self.logout.check_btn('Logout')


#=======================================================================================================================
