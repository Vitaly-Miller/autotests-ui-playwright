"""
Sidebar
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.navigation.sidebar.sidebar_item_component import SidebarItemComponent

#=======================================================================================================================
class SidebarComponent(BaseComponent):
    """
    [Sidebar] component

    - Dashboard item
    - Courses item
    - Logout item
    """
    def __init__(self, page: Page):
        super().__init__(page)
        # ⿳ COMPONENTS
        self.dashboard_item = SidebarItemComponent(page=page, identifier='dashboard')
        self.courses_item = SidebarItemComponent(page=page, identifier='courses')
        self.logout_item = SidebarItemComponent(page=page, identifier='logout')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Dashboard]
    def click_dashboard(self):
        """
        ▶ Click [Dashboard]

        .
        """
        self.dashboard_item.click_btn()

    # Click [Courses]
    def click_courses(self):
        """
        ▶ Click [Courses]

        .
        """
        self.courses_item.click_btn()

    # Click [Logout]
    def click_logout(self):
        """
        ▶ Click [Logout]

        .
        """
        self.logout_item.click_btn()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Sidebar]
    # ────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Sidebar]')
    def check(self):
        """
        ✔ Check [Sidebar]

        - ✔ Dashboard item - visible | Icon - visible | Title - visible | - text
        - ✔ Courses item - visible | Icon - visible | Title - visible | - text
        - ✔ Logout item - visible | Icon - visible | Title - visible | - text
        """
        self.dashboard_item.check(title='Dashboard')
        self.courses_item.check(title='Courses')
        self.logout_item.check(title='Logout')
    # ────────────────────────────────────────────────────────────┘

#=======================================================================================================================
