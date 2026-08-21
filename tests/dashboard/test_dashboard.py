"""
Test Dashboard
"""

import pytest
import allure
from tools.allure.annotations import Epic, Feature, Story, Tag
from pages.dashboard.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(Tag.DASHBOARD, Tag.REGRESSION, Tag.UI)
@allure.epic(Epic.DASHBOARD)
@allure.story(Story.DASHBOARD)
@allure.feature(Feature.DASHBOARD)
class TestDashboard:
    @allure.title('Check Dashboard page components UI')
    def test_dashboard(self, dashboard_page: DashboardPage):
        # 𝌆 TEST DATA
        username = 'username'

        # ⿹ Open page
        dashboard_page.open(dashboard_page.URL)

        # ✔️EXPECTATIONS
        dashboard_page.check(username)  # <— 30 внутренних проверок

#=======================================================================================================================
