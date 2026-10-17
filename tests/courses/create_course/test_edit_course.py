"""
Edit course
"""
import allure
import pytest
from allure_commons.types import Severity

from pages.courses.courses_list.courses_list_page import CoursesListPage
from pages.courses.create_course.create_course_page import CreateCoursePage
from tools.allure.annotations import Epic, Feature, Story, Tag

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.files
@pytest.mark.regression
@allure.severity(Severity.CRITICAL)
@allure.tag(Tag.COURSES, Tag.UPDATE, Tag.FILES, Tag.REGRESSION)
@allure.epic(Epic.COURSES)
@allure.feature(Feature.COURSES)
@allure.story(Story.UPDATE)
class TestEditCourse:
    @allure.title('Edit course')
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴ ◁ PRE-CONDITION (Create course)  ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
        # ⏎ INPUT TEST DATA (wrong input)
        title = 'eltit esruoc tset yM'
        estimated_time = 'emit detamitse esruoc tset yM'
        description = 'noitpircsed esruoc tset yM'
        max_score = '100'
        min_score = '10'

        # ⿹ Open page
        create_course_page.open(create_course_page.URL)

        # ▶ ACTIONS (Create course)
        create_course_page.image_upload_widget.upload_image('image_1.jpg')
        create_course_page.form.fill(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score
        )
        create_course_page.toolbar.click_create_course_btn()

        # ✔️EXPECTATIONS (After Course creation)
        courses_list_page.check_current_url(courses_list_page.URL)
        courses_list_page.course_card.check(
            title=title,
            estimated_time=estimated_time,
            max_score=max_score,
            min_score=min_score
        )
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

        # ⏎ NEW INPUT TEST DATA (Reverse + Upper case)
        new_title = title.upper()[::-1]
        new_estimated_time = estimated_time.upper()[::-1]
        new_description = description.upper()[::-1]
        new_max_score = str(int(max_score) + 400)
        new_min_score = str(int(min_score) + 40)

        # ▶ ACTIONS (Edit course)
        courses_list_page.course_card.click_menu_btn()
        courses_list_page.course_card.menu.click_edit_btn()
        create_course_page.image_upload_widget.upload_image('image_2.jpg')
        create_course_page.form.fill(
            title=new_title,
            estimated_time=new_estimated_time,
            description=new_description,
            max_score=new_max_score,
            min_score=new_min_score
        )
        create_course_page.toolbar.click_create_course_btn()

        # ✔️EXPECTATIONS
        courses_list_page.check_current_url(courses_list_page.URL)
        courses_list_page.course_card.check(
            title=new_title,
            estimated_time=new_estimated_time,
            max_score=new_max_score,
            min_score=new_min_score
        )


#=======================================================================================================================
