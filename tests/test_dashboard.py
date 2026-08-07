"""
Test Dashboard
"""

import pytest
from pages.dashboard_page import DashboardPage

#=======================================================================================================================
@pytest.mark.dashboard
@pytest.mark.registration
def test_dashboard(dashboard_page: DashboardPage):

    # ⿹ Open page
    dashboard_page.visit(dashboard_page.URL)

    # ✔️EXPECTATIONS
    dashboard_page.navbar.check_navbar('Username')
    dashboard_page.check_toolbar()
    dashboard_page.check_all_widgets()


    # ⏳(optional)
    dashboard_page.wait()
#=======================================================================================================================
