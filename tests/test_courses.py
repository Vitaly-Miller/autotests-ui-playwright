"""
Test Create Course

(60 cheks)
"""


import pytest
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage




#=======================================================================================================================
@pytest.mark.registration
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):

    # ⿹ Open page
    create_course_page.visit(create_course_page.URL)

    # ✔️EXPECTATIONS (before image uploading)
    create_course_page.check_toolbar_title_text()                  # Наличие заголовка - "Create course"
    create_course_page.check_toolbar_create_course_btn_disabled()  # Кнопка "Create course" - НЕактивна
    create_course_page.check_preview_view()                        # Все элементы блока <Preview View> (КАРТИНКА НЕ ЗАГРУЖЕНА) - отображаются корректно
    create_course_page.check_upload_image_view()                   # Все элементы блока <Upload Image View> (КАРТИНКА НЕ ЗАГРУЖЕНА) -  отображаются корректно
    create_course_page.check_course_form()                         # Все поля формы создания курса - отображаются корректно
    create_course_page.check_exercises_toolbar()                   # Наличие заголовка - "Exercises" | Кнопка добавления Exercise - видима
    create_course_page.check_exercises_empty_view()                # Все элементы блока <Exercises Empty View> - отображаются корректно

    # ▶ ACTIONS (image upload)
    create_course_page.upload_image('image_1.jpg')                 # Загрузка изображения

    # ✔️EXPECTATIONS (after image uploading)
    create_course_page.check_preview_view()                        # Загруженная в <Preview View> картинка - отображается

    # ▶ ACTIONS (Create course)
    create_course_page.fill_create_course_form(                    # Заполнение полей формы <Create Course>
        title='Playwright',
        estimated_time='2 weeks',
        description='Page Object Model',
        max_score='100',
        min_score='10'
    )
    create_course_page.click_create_course_btn()                   # Нажатие на кнопку <Create course Button>

    # ✔️EXPECTATIONS (after Course creation)
    courses_list_page.check_courses_toolbar()                     # Проверка успешного редиректа на страницу - Courses List Page
    courses_list_page.check_course_card(                          # Данные в карточке курса соответствуют заполненным полям формы
        index=0,                                                  # Element DOM-index of <Course Card>
        title='Playwright',
        estimated_time='2 weeks',
        max_score='100',
        min_score='10'
    )

    # ⏳(optional)
    create_course_page.page.wait_for_timeout(2_000)
#=======================================================================================================================
