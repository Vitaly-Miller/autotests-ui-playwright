"""
Test Create Course (60 checks)
"""

import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage

#=======================================================================================================================
@pytest.mark.courses
@pytest.mark.files
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):

    # ⏎ INPUT DATA
    username = 'username'
    course_title = 'Playwright'
    course_estimated_time = '2 weeks'
    course_description = 'Page Object Model'
    course_max_score = '100'
    course_min_score = '10'


    # ⿹ Open page
    create_course_page.visit(create_course_page.URL)

    # ✔️EXPECTATIONS (before image uploading)
    create_course_page.check_toolbar_and_navbar_sidebar(username)  # Проверка блоков <Toolbar> + <Navbar> + <Sidebar>
    create_course_page.check_preview_view()                        # Проверка блока <Preview View> (КАРТИНКА НЕ ЗАГРУЖЕНА)
    create_course_page.check_upload_image_view()                   # Проверка блока <Upload image View> (КАРТИНКА НЕ ЗАГРУЖЕНА)
    create_course_page.check_course_form()                         # Проверка блока <Course form> (ПОЛЯ НЕ ЗАПОЛНЕНЫ)
    create_course_page.check_exercises_toolbar()                   # Проверка блока <Exercises [Toolbar]>
    create_course_page.check_exercises_empty_view()                # Проверка блока <Exercises [Empty view]>

    # ▶ ACTIONS (image upload)
    create_course_page.upload_image('image_1.jpg')                 # Загрузка изображения

    # ✔️EXPECTATIONS (after image uploading)
    create_course_page.check_preview_view()                        # Проверка блока <Preview View> (КАРТИНКА ЗАГРУЖЕНА)

    # ▶ ACTIONS (Create course)
    create_course_page.fill_create_course_form(                    # Заполнение полей формы <Create Course>
        title=course_title,
        estimated_time=course_estimated_time,
        description=course_description,
        max_score=course_max_score,
        min_score=course_min_score
    )
    create_course_page.click_create_course_btn()                   # Нажатие на кнопку <Create course Button>

    # ✔️EXPECTATIONS (after Course creation)
    courses_list_page.check_current_url(courses_list_page.URL)    # Проверка успешного редиректа на страницу - Courses List Page
    courses_list_page.check_course_card(                          # Данные в карточке курса соответствуют заполненным полям формы
        index=0,                                                  # Element DOM-index of <Course Card>
        title=course_title,
        estimated_time=course_estimated_time,
        max_score=course_max_score,
        min_score=course_min_score
    )

    # ⏳(optional)
    create_course_page.wait()
#=======================================================================================================================
