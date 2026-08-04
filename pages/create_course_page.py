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

        # Preview Empty View
        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        # Preview View - Image
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        # Upload image View
        self.upload_image_view_icon = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.upload_image_view_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_view_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')

        # Upload image View - Buttons
        self.upload_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_image_view_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')  # hidden input for upload image
        self.remove_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

        # Course Form
        self.course_form_title_field = page.get_by_role(role='textbox', name='Title')
        self.course_form_estimated_time_field = page.get_by_role(role='textbox', name='Estimated time')
        self.course_form_description_field = page.get_by_role(role='textbox', name='Description')
        self.course_form_max_score_field = page.get_by_role(role='spinbutton', name='Max score')
        self.course_form_min_score_field = page.get_by_role(role='spinbutton', name='Min score')


        # Create exercise
        self.create_exercise_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.create_exercise_btn = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        # Create exercise - Empty view
        self.create_exercise_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.create_exercise_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.create_exercise_empty_view_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')


    # ---------------------------------------------- ㉧ LOCATORS {dynamic} ----------------------------------------------
    # Exercise
    def exercise_title(self, index: int = 0) -> Locator:
        """
        By element <data_testid> index

        :param index: Element <data_testid> index if more than one Exercise (Default = 0, if single)
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

    def click_remove_image_btn(self):
        """
        Click <Remove image> button of the Create course page

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button text - correct
        - ▶ Button - Click
        :return:
        """
        self.check_remove_image_view_btn()
        self.remove_image_btn.click()

    def upload_image(self, file: str):
        """
        Upload image

        - ▶ Upload file

        :param file: File path
        """
        self.upload_image_view_input.set_input_files(file)
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
    # - Toolbar - Title
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

    # - Toolbar - Create Course button
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


    # Preview View:
    # ─────────────────────────────────────────────────────────┐
    def check_preview_view(self):
        """
        Check <Remove View> of the Create course page

        If Image UPLOADED:
        -----------------
        - ✔ Image - visible

        If Image DID NOT upload:
        -----------------------
        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        if self.preview_image.is_visible():  # if image uploaded
            self.check_preview_view_image_visible()
        else:
            self.check_preview_empty_view_icon_visible()
            self.check_preview_empty_view_title_visible()
            self.check_preview_empty_view_title_text()
            self.check_preview_empty_view_description_visible()
            self.check_preview_empty_view_description_text()
    # ─────────────────────────────────────────────────────────┘
    # - Preview Empty View - Icon
    def check_preview_empty_view_icon_visible(self):
        """
        Check <Preview Empty View - Icon> of the Create course page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Preview Empty View - Icon> of the Create course page - invisible!'
        expect(self.preview_empty_view_icon, error).to_be_visible()

    # - Preview Empty View - Title
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

    # - Preview Empty View - Description
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

    # - Preview View - Image
    def check_preview_view_image_visible(self):
        """
        Check <Preview View - Image> of the Create course page - visible

        - ✔ Image - visible
        """
        error = '❌ <Preview View - Image> of the Create course page - invisible!'
        expect(self.preview_image, error).to_be_visible()


    # Upload image View:
    # ────────────────────────────────────────────────────┐
    def check_upload_image_empty_view(self):
        """
        Check <Upload image View> of the Create course page

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        - ✔ <Upload Button> - visible | - enabled | - text
        - ✔ <Remove Button> - invisible (if image DID NOT upload)
        - ✔ <Remove Button> - visible | - enabled | - text (if image UPLOADED)
        """
        self.check_upload_image_view_icon_visible()
        self.check_upload_image_view_title_visible()
        self.check_upload_image_view_title_text()
        self.check_upload_image_view_description_visible()
        self.check_upload_image_view_description_text()
        self.check_upload_image_view_btn()    # suite
        self.check_remove_image_view_btn()    # if-suite
    # ────────────────────────────────────────────────────┘
    # - Upload image View - Icon
    def check_upload_image_view_icon_visible(self):
        """
        Check <Upload image View - Icon> of the Create course page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Upload image View - Icon> of the Create course page - invisible!'
        expect(self.upload_image_view_icon, error).to_be_visible()

    # - Upload image View - Title
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

    # - Upload image View - Description
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


    # - Upload image View - <Upload image> Button
    # ────────────────────────────────────────────────────┐
    def check_upload_image_view_btn(self):
        """
        Check <Upload image> button of the Create course page

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Text - correct
        """
        self.check_upload_image_view_btn_visible()
        self.check_upload_image_view_btn_enable()
        self.check_upload_image_view_btn_text()
    # ────────────────────────────────────────────────────┘
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


    # - Upload image View - <Remove image> Button (if image uploaded)
    # ────────────────────────────────────────────────────┐
    def check_remove_image_view_btn(self):
        """
        Check <Remove image> button of the Create course page

        If Image UPLOADED:
        -----------------
        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button text - correct

        If Image DID NOT upload:
        -----------------------
        - ✔ Button - invisible
        """
        if self.preview_image.is_visible():  # if image uploaded
            self.check_remove_image_view_btn_visible()
            self.check_remove_image_view_btn_enable()
            self.check_remove_image_view_btn_text()
        else:    # if image did not upload
            self.check_remove_image_view_btn_invisible()
    # ────────────────────────────────────────────────────┘
    def check_remove_image_view_btn_visible(self):
        """
        Check <Remove image View - Button> of the Create course page - visible

        (For case - If image UPLOADED)

        - ✔ Button - visible

        """
        error = '❌ <Remove image View - Button> of the Create course page - invisible!'
        expect(self.remove_image_btn, error).to_be_visible()

    def check_remove_image_view_btn_invisible(self):
        """
        Check <Remove image View - Button> of the Create course page - invisible

        (For case - if image DID NOT upload)

        - ✔ Button - invisible

        """
        error = '❌ <Remove image View - Button> of the Create course page - visible!'
        expect(self.remove_image_btn, error).not_to_be_visible()

    def check_remove_image_view_btn_enable(self):
        """
        Check <Remove image View - Button> of the Create course page - enabled

        - ✔ Button - enabled

        """
        error = '❌ <Remove image View - Button> of the Create course page - disabled!'
        expect(self.remove_image_btn, error).to_be_enabled()

    def check_remove_image_view_btn_text(self, text: str = 'Remove image'):
        """
        Check <Remove image View - Button> text of the Create course page - correct

        - ✔ Text - correct
        """
        error = '❌ <Remove image View - Button> text of the Create course page - incorrect!'
        expect(self.remove_image_btn, error).to_have_text(text)


    # Course Form:
    # ────────────────────────────────────────────────────┐
    def check_course_form(
            self,
            title,
            estimated_time,
            description,
            max_score,
            min_score
    ):
        """
        Check <Course form> of the Create course page

        - ✔ Form fields - visible
        - ✔ Form fields - correct
        - ✔ Form field placeholders - correct (except Max/Min score)
        - ✔ Form fields - filled correctly

        :param title: Title
        :param estimated_time: Estimated Time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        self.check_course_form_title(title)
        self.check_course_form_estimated_time(estimated_time)
        self.check_course_form_description(description)
        self.check_course_form_max_score(max_score)
        self.check_course_form_min_score(min_score)
    # ────────────────────────────────────────────────────┘

    # Course Form - Title field
    # ─────────────────────────────────────────────────────────────────────┐
    def check_course_form_title(self, title: str | None = None):
        """
        Check <Course form - Title field> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct
        - ✔ Field - filled correctly (if text is passed)

        :param title: Title (optional)
        """
        self.check_course_form_title_field_visible()
        self.check_course_form_title_field_name()
        self.check_course_form_title_field_placeholder()
        if title:   # (if text is passed)
            self.check_course_form_title_field_filled_correctly(title)
    # ─────────────────────────────────────────────────────────────────────┘
    def check_course_form_title_field_visible(self):
        """
        Check <Course form - Title field> of the Create course page - visible!

        - ✔ Title field - visible
        """
        error = '❌ <Course form Title field> of the Create course page - invisible!'
        expect(self.course_form_title_field, error).to_be_visible()

    def check_course_form_title_field_name(self, field_name: str = 'Title'):
        """
        Check <Course form - Title field> name of the Create course page - correct!

        - ✔ Title name - correct

        :param field_name: Field name
        """
        error = '❌ <Course form Title field> name of the Create course page - incorrect!'
        expect(self.course_form_title_field, error).to_have_accessible_name(field_name)

    def check_course_form_title_field_placeholder(self, placeholder: str = 'New course'):
        """
        Check <Course form - Title field Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct

        :param placeholder: Placeholder
        """
        error = '❌ <Course form Title field> of the Create course page - incorrect!'
        expect(self.course_form_title_field, error).to_have_attribute('placeholder', placeholder)

    def check_course_form_title_field_filled_correctly(self, title: str):
        """
        Check <Course form - Title field> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param title: Title
        """
        error = '❌ <Course form Title field> of the Create course page - filled incorrectly!'
        expect(self.course_form_title_field, error).to_have_value(title)


    # Course Form - Estimated time field
    # ──────────────────────────────────────────────────────────────────────────────────┐
    def check_course_form_estimated_time(self, estimated_time: str | None = None):
        """
        Check <Course form - Estimated time field> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct
        - ✔ Field - filled correctly (if text is passed)

        :param estimated_time: Estimated time (optional)
        """
        self.check_course_form_estimated_time_field_visible()
        self.check_course_form_estimated_time_field_name()
        self.check_course_form_estimated_time_field_placeholder()
        if estimated_time:   # If filled
            self.check_course_form_estimated_time_field_filled_correctly(estimated_time)
    # ──────────────────────────────────────────────────────────────────────────────────┘
    def check_course_form_estimated_time_field_visible(self):
        """
        Check <Course form - Estimated time field> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course form Estimated time field> of the Create course page - invisible!'
        expect(self.course_form_estimated_time_field, error).to_be_visible()

    def check_course_form_estimated_time_field_name(self, field_name: str = 'Estimated time'):
        """
        Check <Course form - Estimated time field> name of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course form Estimated time field> name of the Create course page - incorrect!'
        expect(self.course_form_estimated_time_field, error).to_have_accessible_name(field_name)

    def check_course_form_estimated_time_field_placeholder(self, placeholder: str = '1h 20m'):
        """
        Check <Course form - Estimated time field Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct

        :param placeholder: Placeholder
        """
        error = '❌ <Course form Estimated time field> of the Create course page - incorrect!'
        expect(self.course_form_estimated_time_field, error).to_have_attribute('placeholder', placeholder)

    def check_course_form_estimated_time_field_filled_correctly(self, estimated_time: str):
        """
        Check <Course form - Estimated time field> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param estimated_time: Estimated time
        """
        error = '❌ <Course form Estimated time field> of the Create course page - filled incorrectly!'
        expect(self.course_form_estimated_time_field, error).to_have_value(estimated_time)


    # Course Form - Description field
    # ────────────────────────────────────────────────────────────────────────────┐
    def check_course_form_description(self, description: str | None = None):
        """
        Check <Course form - Description field> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct
        - ✔ Field - filled correctly (if text is passed)

        :param description: Description (optional)
        """
        self.check_course_form_description_field_visible()
        self.check_course_form_description_field_name()
        self.check_course_form_description_field_placeholder()
        if description:   # If filled
            self.check_course_form_description_field_filled_correctly(description)
    # ────────────────────────────────────────────────────────────────────────────┘
    def check_course_form_description_field_visible(self):
        """
        Check <Course form - Description field> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course form Description field> of the Create course page - invisible!'
        expect(self.course_form_description_field, error).to_be_visible()

    def check_course_form_description_field_name(self, field_name: str = 'Description'):
        """
        Check <Course form - Description field> name of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course form Description field> name of the Create course page - incorrect!'
        expect(self.course_form_description_field, error).to_have_accessible_name(field_name)

    def check_course_form_description_field_placeholder(self, placeholder: str = 'Add description for course'):
        """
        Check <Course form - Description field Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct

        :param placeholder: Placeholder
        """
        error = '❌ <Course form Description field> of the Create course page - incorrect!'
        expect(self.course_form_description_field, error).to_have_attribute('placeholder', placeholder)

    def check_course_form_description_field_filled_correctly(self, description: str):
        """
        Check <Course form - Description field> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param description: Description
        """
        error = '❌ <Course form Description field> of the Create course page - filled incorrectly!'
        expect(self.course_form_description_field, error).to_have_value(description)


    # Course Form - Max score field
    # ───────────────────────────────────────────────────────────────┐
    def check_course_form_max_score(self, max_score: str = '0'):
        """
        Check <Course form - Max score field> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly

        :param max_score: Max score (optional)
        """
        self.check_course_form_max_score_field_visible()
        self.check_course_form_max_score_field_name()
        self.check_course_form_max_score_field_filled_correctly(max_score)
    # ───────────────────────────────────────────────────────────────┘
    def check_course_form_max_score_field_visible(self):
        """
        Check <Course form - Max score field> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course form Max score field> of the Create course page - invisible!'
        expect(self.course_form_max_score_field, error).to_be_visible()

    def check_course_form_max_score_field_name(self, field_name: str = 'Max score'):
        """
        Check <Course form - Max score field> name of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course form Max score field> name of the Create course page - incorrect!'
        expect(self.course_form_max_score_field, error).to_have_accessible_name(field_name)

    def check_course_form_max_score_field_filled_correctly(self, max_score: str = '0'):
        """
        Check <Course form - Max score field> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param max_score: Max score
        """
        error = '❌ <Course form Max score field> of the Create course page - filled incorrectly!'
        expect(self.course_form_max_score_field, error).to_have_value(max_score)


    # Course Form - Min score field
    # ───────────────────────────────────────────────────────────────────────────┐
    def check_course_form_min_score(self, min_score: str = '0'):
        """
        Check <Course form - Min score field> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly

        :param min_score: Min score
        """
        self.check_course_form_min_score_field_visible()
        self.check_course_form_min_score_field_name()
        self.check_course_form_min_score_field_filled_correctly(min_score)
    # ───────────────────────────────────────────────────────────────────────────┘
    def check_course_form_min_score_field_visible(self):
        """
        Check <Course form - Min score field> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course form Min score field> of the Create course page - invisible!'
        expect(self.course_form_min_score_field, error).to_be_visible()

    def check_course_form_min_score_field_name(self, field_name: str = 'Min score'):
        """
        Check <Course form - Min score field> name of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course form Min score field> name of the Create course page - incorrect!'
        expect(self.course_form_min_score_field, error).to_have_accessible_name(field_name)

    def check_course_form_min_score_field_filled_correctly(self, min_score: str = '0'):
        """
        Check <Course form - Min score field> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param min_score: Min score
        """
        error = '❌ <Course form Min score field> of the Create course page - filled incorrectly!'
        expect(self.course_form_min_score_field, error).to_have_value(min_score)
