"""
Edit course
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
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴ Precondition (Create course)  ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
        # ⏎ INPUT TEST DATA
        title = 'eltit esruoc tset yM'
        estimated_time = 'emit detamitse esruoc tset yM'
        description = 'noitpircsed esruoc tset yM'
        max_score = '100'
        min_score = '10'

        # ⿹ Open page
        create_course_page.visit(create_course_page.URL)

        # ▶ ACTIONS (Create course)
        create_course_page.image_upload_widget.upload_image('image_1.jpg')  # Загрузка картинки курса
        create_course_page.form.fill_course_form(                           # Заполнение полей формы <Create Course>
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score
        )
        create_course_page.toolbar.click_create_course_btn()                # Нажатие на кнопку <Create course button>

        # ✔️EXPECTATIONS (After Course creation)
        courses_list_page.check_current_url(courses_list_page.URL)          # Проверка успешного редиректа на страницу - Courses list page
        courses_list_page.course_card.check_course_card(                    # Данные в карточке курса соответствуют заполненным полям формы
            title=title,
            estimated_time=estimated_time,
            max_score=max_score,
            min_score=min_score
        )
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
        # ⏎ NEW INPUT TEST DATA (🤦🏻‍♂️просто решил побаловаться с методами)
        new_title = title.upper()[::-1]
        new_estimated_time = estimated_time.upper()[::-1]
        new_description = description.upper()[::-1]
        new_max_score = str(int(max_score) + 400)
        new_min_score = str(int(min_score) + 40)

        # ▶ ACTIONS (Edit course)
        courses_list_page.course_card.click_menu_btn()                     # Нажатие на кнопку <Menu>
        courses_list_page.course_card.menu.click_edit_btn()                # Нажатие на кнопку <Edit course>
        create_course_page.image_upload_widget.upload_image('image_2.jpg') # Загрузка новой картинки курса
        create_course_page.form.fill_course_form(                          # Заполнение полей формы новыми данными
            title=new_title,
            estimated_time=new_estimated_time,
            description=new_description,
            max_score=new_max_score,
            min_score=new_min_score
        )
        create_course_page.toolbar.click_create_course_btn()               # Нажатие на кнопку <Create course button>

        # ✔️EXPECTATIONS
        courses_list_page.check_current_url(courses_list_page.URL)         # Проверка успешного редиректа на страницу - Courses list page
        courses_list_page.course_card.check_course_card(                   # Данные в карточке курса соответствуют заполненным полям формы
            title=new_title,
            estimated_time=new_estimated_time,
            max_score=new_max_score,
            min_score=new_min_score
        )



#=======================================================================================================================
