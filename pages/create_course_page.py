"""
Create Course page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class CreateCoursePage(BasePage):        # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):      # Конструктор класса, принимающий Page
        super().__init__(page)           # Передаёт page в конструктор BasePage

        # ┌╴ 𝌆 DATA:
        # ├ Page URL
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'


        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('create-course-toolbar-create-course-button')
        # ├ Preview (left block)
        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')
        # ├ Upload image (right block)
        self.upload_image_icon = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.upload_image_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.upload_image_button = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_image_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')  # hidden input for upload image
        self.remove_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')
        # ├ Create course (Form)
        self.title_field = page.get_by_role(role='textbox', name='Title')
        self.estimated_time_field = page.get_by_role(role='textbox', name='Estimated time')
        self.description_field = page.get_by_role(role="textbox", name="Description")
        self.max_score_field = page.get_by_role(role='spinbutton', name="Max score")
        self.minx_score_field = page.get_by_role(role='spinbutton', name="Min score")
        # ├ Create exercise (Toolbar)
        self.create_exercise_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_btn = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')
        # ├ Create exercise (Empty view)
        self.create_exercise_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.create_exercise_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.create_exercise_empty_view_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------




    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    #
