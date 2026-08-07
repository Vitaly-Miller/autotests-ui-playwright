"""
Sidebar Component
"""
"""
- <Dashboard Button>
- <Courses Button>
- <Logout Button>
"""

from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar_list_component import SidebarListComponent

#=======================================================================================================================
class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ----------------------------------------------- ⿷ COMPONENTS ------------------------------------------------
        self.dashboard_btn = SidebarListComponent(page=page, identifier='dashboard')
        self.courses_btn = SidebarListComponent(page=page, identifier='courses')
        self.logout_btn = SidebarListComponent(page=page, identifier='logout')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_dashboard_btn(self):
        self.dashboard_btn.click_btn()

    def click_course_btn(self):
        self.courses_btn.click_btn()

    def click_logout_btn(self):
        self.logout_btn.click_btn()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    def check_sidebar(self):
        """
        Check <Sidebar>

        - ✔ <Dashboard Button> - visible | Icon - visible | Title - visible | Text - correct
        - ✔ <Courses Button> - visible | Icon - visible | Title - visible | Text - correct
        - ✔ <Logout Button> - visible | Icon - visible | Title - visible | Text - correct
        """
        self.dashboard_btn.check_btn('Dashboard')
        self.courses_btn.check_btn('Courses')
        self.logout_btn.check_btn('Logout')


#=======================================================================================================================
