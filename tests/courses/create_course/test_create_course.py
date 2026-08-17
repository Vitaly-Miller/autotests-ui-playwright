"""
Test Create course
"""

import pytest
from pages.courses.courses_list.courses_list_page import CoursesListPage
from pages.courses.create_course.create_course_page import CreateCoursePage

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.create_course
@pytest.mark.files
@pytest.mark.regression
class TestCreateCourse:
    def test_create_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        # ⏎ INPUT TEST DATA
        course_title = 'Playwright'
        course_estimated_time = '2 weeks'
        course_description = 'Page Object Model'
        course_max_score = '100'
        course_min_score = '10'

        # ⿹ Open page
        create_course_page.visit(create_course_page.URL)

        # ▶ ACTIONS (Create course)
        create_course_page.image_upload_widget.upload_image('image_1.jpg')  # Загрузка картинки курса
        create_course_page.form.fill_form(                                  # Заполнение полей формы <Create Course>
            title=course_title,
            estimated_time=course_estimated_time,
            description=course_description,
            max_score=course_max_score,
            min_score=course_min_score
        )
        create_course_page.toolbar.click_create_course_btn()                # Нажатие на кнопку <Create course button>

        # ✔️EXPECTATIONS (After Course creation)
        courses_list_page.check_current_url(courses_list_page.URL)          # Проверка успешного редиректа на страницу - Courses list page
        courses_list_page.course_card.check_course_card(                    # Данные в карточке курса соответствуют заполненным полям формы
            nth_index=0,                                                    # nth-index
            title=course_title,
            estimated_time=course_estimated_time,
            max_score=course_max_score,
            min_score=course_min_score
        )


#=======================================================================================================================
