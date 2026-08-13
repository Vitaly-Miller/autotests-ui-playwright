"""
Test Dashboard
"""

import pytest
from pages.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard(dashboard_page: DashboardPage):

    # 𝌆 TEST DATA
    username = 'username'

    # ⿹ Open page
    dashboard_page.visit(dashboard_page.URL)

    # ✔️EXPECTATIONS
    dashboard_page.navbar.check_navbar()
    dashboard_page.sidebar.check_sidebar()
    dashboard_page.check_toolbar()
    dashboard_page.check_all_widgets()


    # ⏳(optional)
    dashboard_page.wait()
#=======================================================================================================================
