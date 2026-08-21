"""
Test Courses
"""

import pytest
import allure
from allure_commons.types import Severity
from tools.allure.annotations import Epic, Feature, Story, Tag
from pages.courses.courses_list.courses_list_page import CoursesListPage

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.ui
@allure.severity(Severity.NORMAL)
@allure.tag(Tag.COURSES, Tag.REGRESSION, Tag.UI)
@allure.epic(Epic.COURSES)
@allure.feature(Feature.COURSES)
@allure.story(Story.UI)
class TestCourses:
    @allure.title('Check empty courses list UI')
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        # 𝌆 TEST DATA
        username = 'username'

        # ⿹ Open page
        courses_list_page.open(courses_list_page.URL)

        # ✔️EXPECTATIONS
        courses_list_page.navbar.check(username)
        courses_list_page.sidebar.check()
        courses_list_page.toolbar.check()
        courses_list_page.check_empty_view()

        # ╴╴╴╴╴╴╴╴╴╴ ⏳╴╴╴╴╴╴╴╴╴╴╴┐
        # courses_list_page.wait()
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘


#=======================================================================================================================
