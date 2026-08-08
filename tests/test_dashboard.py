"""
Test Dashboard
"""

import pytest
from pages.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard(dashboard_page: DashboardPage):

    # ⿹ Open page
    dashboard_page.visit(dashboard_page.URL)

    # ✔️EXPECTATIONS
    dashboard_page.check_toolbar_and_navbar_sidebar('username')
    dashboard_page.check_all_widgets()


    # ⏳(optional)
    dashboard_page.wait()
#=======================================================================================================================
