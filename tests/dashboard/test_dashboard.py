"""
Test Dashboard
"""

import pytest
from pages.dashboard.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard(self, dashboard_page: DashboardPage):
        # 𝌆 TEST DATA
        username = 'username'

        # ⿹ Open page
        dashboard_page.visit(dashboard_page.URL)

        # ✔️EXPECTATIONS
        dashboard_page.check_page(username)  # <— 30 внутренних проверок

#=======================================================================================================================
