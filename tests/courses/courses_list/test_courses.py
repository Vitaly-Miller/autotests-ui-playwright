"""
Test Courses
"""

import pytest
from pages.courses.courses_list.courses_list_page import CoursesListPage

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        # 𝌆 TEST DATA
        username = 'username'

        # ⿹ Open page
        courses_list_page.visit(courses_list_page.URL)

        # ✔️EXPECTATIONS
        courses_list_page.navbar.check_navbar(username)
        courses_list_page.sidebar.check_sidebar()
        courses_list_page.toolbar.check_toolbar()
        courses_list_page.check_empty_view()

        # ╴╴╴╴╴╴╴╴╴╴ ⏳╴╴╴╴╴╴╴╴╴╴╴┐
        courses_list_page.wait()
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘


#=======================================================================================================================
