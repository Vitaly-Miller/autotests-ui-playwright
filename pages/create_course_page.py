"""
Create Course page
"""
from pages.base_page import BasePage
from playwright.sync_api import Locator, Page, expect

#=======================================================================================================================
class CreateCoursePage(BasePage):        # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'

    def __init__(self, page: Page):      # Конструктор класса, принимающий Page
        super().__init__(page)           # Передаёт page в конструктор BasePage

        # ------------------------------------------- ㉧ LOCATORS (static) ----------------------------------------------
        # Toolbar
        self.toolbar_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('create-course-toolbar-create-course-button')

        # Preview - Empty View
        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        # Preview - Image View
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        # Upload image View
        self.upload_image_view_icon = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.upload_image_view_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_view_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')

        # Upload image View - Buttons
        self.upload_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_image_view_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')  # hidden input for upload image
        self.remove_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

        # Form
        self.title_field = page.get_by_role(role='textbox', name='Title')
        self.estimated_time_field = page.get_by_role(role='textbox', name='Estimated time')
        self.description_field = page.get_by_role(role='textbox', name='Description')
        self.max_score_field = page.get_by_role(role='spinbutton', name='Max score')
        self.minx_score_field = page.get_by_role(role='spinbutton', name='Min score')


        # Create exercise
        self.create_exercise_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_btn = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        # Create exercise - Empty view
        self.create_exercise_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.create_exercise_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.create_exercise_empty_view_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')
        self.exercise_title = page.get_by_test_id(f'create-course-exercise-0-box-toolbar-subtitle-text')  # ⚠️ Используй динамический локатор с индексом!


    # ---------------------------------------------- ㉧ LOCATORS {dynamic} ----------------------------------------------
    # Exercises
    def exercise_title(self, index: int = 0) -> Locator:
        """
        By element <data_testid> index

        :param index: Element <data_testid> index if more than one Exercise (Default = 0 if single)
        :return: Locator
        """
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_create_course_btn(self):
        """
        Click <Create course> button of the Create course page

        - ✔ Button - visible
        - ✔ Button - enabled
        - ▶ Button - Click
        """
        self.check_create_course_btn_visible()
        self.check_create_course_btn_enabled()
        self.create_course_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar:
    # ─────────────────────────────────────────┐
    def check_toolbar(self):
        """
        Check <Toolbar> of the Create course page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ <Create Course button> - visible
        - ✔ <Create Course button> - enable
        """
        self.check_toolbar_title_visible()
        self.check_toolbar_title_text()
        self.check_create_course_btn_visible()
        self.check_create_course_btn_enabled()
    # ─────────────────────────────────────────┘

    # Toolbar - Title
    def check_toolbar_title_visible(self):
        """
        Check <Toolbar - Title> of the Create course page - visible

        - ✔ Title - visible
        """
        error = '❌ <Toolbar - Title> of the Create course page - invisible!'
        expect(self.toolbar_title, error).to_be_visible()

    def check_toolbar_title_text(self, text: str = 'Create course'):
        """
        Check <Toolbar - Title> text of the Create course page

        - ✔ Title text - correct

        :param text: "Create course" (default)

        """
        error = '❌ <Toolbar - Title> text of the Create course page - incorrect!'
        expect(self.toolbar_title, error).to_have_text(text)


    # Toolbar - Create Course button
    def check_create_course_btn_visible(self):
        """
        Check <Toolbar - Create Course button> of the Create course page - visible

        - ✔ Button - visible
        """
        error = '❌ <Toolbar - Create Course button> of the Create course page - invisible!'
        expect(self.create_course_btn, error).to_be_visible()

    def check_create_course_btn_enabled(self):
        """
        Check <Toolbar - Create Course button> of the Create course page - enabled

        - ✔ Button - enabled
        """
        error = '❌ <Toolbar - Create Course button> of the Create course page - disabled!'
        expect(self.create_course_btn, error).to_be_enabled()

    def check_create_course_btn_disabled(self):
        """
        Check <Toolbar - Create Course button> of the Create course page - disabled

        - ✔ Button - disabled
        """
        error = '❌ <Toolbar - Create Course button> of the Create course page - enabled!'
        expect(self.create_course_btn, error).to_be_disabled()



    # Preview -  Empty View:
    # ────────────────────────────────────────────────────┐
    def check_preview_empty_view(self):
        self.check_preview_empty_view_icon()
        self.check_preview_empty_view_title_visible()
        self.check_preview_empty_view_title_text()
        self.check_preview_empty_view_description_visible()
        self.check_preview_empty_view_description_text()
    # ────────────────────────────────────────────────────┘

    # Preview Empty View - Icon
    def check_preview_empty_view_icon(self):
        """
        Check <Preview Empty View - Icon> of the Create course page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Preview Empty View - Icon> of the Create course page - invisible!'
        expect(self.preview_empty_view_icon, error).to_be_visible()


    # Preview Empty View - Title
    def check_preview_empty_view_title_visible(self):
        """
        Check <Preview Empty View - Title> of the Create course page - visible

        - ✔ Title - visible

        """
        error = '❌ <Preview Empty View - Title> of the Create course page - invisible!'
        expect(self.preview_empty_view_title, error).to_be_visible()

    def check_preview_empty_view_title_text(self, title: str = 'No image selected'):
        """
        Check <Preview Empty View - Title> text of the Create course page - correct

        - ✔ Text - correct
        """
        error = '❌ <Preview Empty View - Title> text of the Create course page - incorrect!'
        expect(self.preview_empty_view_title, error).to_have_text(title)


    # Preview Empty View - Description
    def check_preview_empty_view_description_visible(self):
        """
        Check <Preview Empty View - Description> of the Create course page - visible

        - ✔ Description - visible
        """
        error = '❌ <Preview Empty View - Description> of the Create course page - invisible!'
        expect(self.preview_empty_view_description, error).to_be_visible()

    def check_preview_empty_view_description_text(self, text: str = 'Preview of selected image will be displayed here'):
        """
        Check <Preview Empty View - Description> text of the Create course - correct

        - ✔ Text - correct
        """
        error = '❌ <Preview Empty View - Description> text of the Create course page - incorrect!'
        expect(self.preview_empty_view_description, error).to_have_text(text)


    # Preview - Image View:
    # ────────────────────────────────────────────────────┐

    # ────────────────────────────────────────────────────┘


    # Upload image View:
    # ────────────────────────────────────────────────────┐
    def check_upload_image_view(self):
        """
        Check <Upload image View> of the Create course page

        - ✔ Icon - visible
        - ✔ Title - visible | Text - correct
        - ✔ Description - visible | Text - correct
        - ✔ <Upload Button> - visible | - enabled | Text - correct
        """
        self.check_upload_image_view_icon_visible()
        self.check_upload_image_view_title_visible()
        self.check_upload_image_view_title_text()
        self.check_upload_image_view_description_visible()
        self.check_upload_image_view_description_text()
        self.check_upload_image_view_btn_visible()
        self.check_upload_image_view_btn_enable()
        self.check_upload_image_view_btn_text()
    # ────────────────────────────────────────────────────┘
    # Upload image View - Icon
    def check_upload_image_view_icon_visible(self):
        """
        Check <Upload image View - Icon> of the Create course page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Upload image View - Icon> of the Create course page - invisible!'
        expect(self.upload_image_view_icon, error).to_be_visible()


    # Upload image View - Title
    def check_upload_image_view_title_visible(self):
        """
        Check <Upload image View - Title> of the Create course page - visible

        - ✔ Title - visible

        """
        error = '❌ <Upload image View - Title> of the Create course page - invisible!'
        expect(self.upload_image_view_title, error).to_be_visible()

    def check_upload_image_view_title_text(self, title: str = 'Tap on "Upload image" button to select file'):
        """
        Check <Upload image View - Title> text of the Create course page - correct

        - ✔ Text - correct
        """
        error = '❌ <Upload image View - Title> text of the Create course page - incorrect!'
        expect(self.upload_image_view_title, error).to_have_text(title)


    # Upload image View - Description
    def check_upload_image_view_description_visible(self):
        """
        Check <Upload image View - Description> of the Create course page - visible

        - ✔ Description - visible

        """
        error = '❌ <Upload image View - Description> of the Create course page - invisible!'
        expect(self.upload_image_view_description, error).to_be_visible()

    def check_upload_image_view_description_text(self, title: str = 'Recommended file size 540X300'):
        """
        Check <Upload image View - Description> text of the Create course page - correct

        - ✔ Text - correct
        """
        error = '❌ <Upload image View - Description> text of the Create course page - incorrect!'
        expect(self.upload_image_view_description, error).to_have_text(title)


    # Upload image View - <Upload image> Button
    def check_upload_image_view_btn_visible(self):
        """
        Check <Upload image View - Button> of the Create course page - visible

        - ✔ Button - visible

        """
        error = '❌ <Upload image View - Button> of the Create course page - invisible!'
        expect(self.upload_image_btn, error).to_be_visible()

    def check_upload_image_view_btn_enable(self):
        """
        Check <Upload image View - Button> of the Create course page - enabled

        - ✔ Button - enabled

        """
        error = '❌ <Upload image View - Button> of the Create course page - disabled!'
        expect(self.upload_image_btn, error).to_be_enabled()

    def check_upload_image_view_btn_text(self, title: str = 'Upload image'):
        """
        Check <Upload image View - Button> text of the Create course page - correct

        - ✔ Text - correct
        """
        error = '❌ <Upload image View - Button> text of the Create course page - incorrect!'
        expect(self.upload_image_btn, error).to_have_text(title)

    # Upload image View - <Remove image> Button
