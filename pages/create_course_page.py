"""
Create Course page
"""

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from playwright.sync_api import Locator, Page, expect

#=======================================================================================================================
class CreateCoursePage(BasePage):        # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create'

    def __init__(self, page: Page):      # Конструктор класса, принимающий Page
        super().__init__(page)           # Передаёт page в конструктор BasePage

        # ----------------------------------------------- ⿷ COMPONENTS ------------------------------------------------
        self.navbar = NavbarComponent(page) # Component - Navbar

        # ------------------------------------------- ㉧ LOCATORS (static) ----------------------------------------------
        # Toolbar
        self.toolbar_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('create-course-toolbar-create-course-button')

        # Preview - Empty View
        self.preview_empty_view_icon = page.get_by_test_id('create-course-preview-empty-view-icon')
        self.preview_empty_view_title = page.get_by_test_id('create-course-preview-empty-view-title-text')
        self.preview_empty_view_description = page.get_by_test_id('create-course-preview-empty-view-description-text')

        # Preview - Image
        self.preview_image = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        # Upload image View
        self.upload_image_view_icon = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.upload_image_view_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_view_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')

        # Upload image View - Buttons
        self.upload_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_image_view_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')  # hidden input for upload image
        self.remove_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button') # available after upload image only

        # Course Form
        self.course_form_title_field = page.get_by_role(role='textbox', name='Title')
        self.course_form_estimated_time_field = page.get_by_role(role='textbox', name='Estimated time')
        self.course_form_description_field = page.get_by_role(role='textbox', name='Description')
        self.course_form_max_score_field = page.get_by_role(role='spinbutton', name='Max score')
        self.course_form_min_score_field = page.get_by_role(role='spinbutton', name='Min score')

        # EXERCISES:
        # - Exercises Toolbar
        self.exercise_toolbar_title = page.get_by_test_id('create-course-exercises-box-toolbar-title-text')
        self.exercise_toolbar_create_exercise_btn = page.get_by_test_id('create-course-exercises-box-toolbar-create-exercise-button')

        # - Exercises - Empty view
        self.exercises_empty_view_icon = page.get_by_test_id('create-course-exercises-empty-view-icon')
        self.exercises_empty_view_title = page.get_by_test_id('create-course-exercises-empty-view-title-text')
        self.exercises_empty_view_description = page.get_by_test_id('create-course-exercises-empty-view-description-text')

        # - Exercise Form (see dynamic locators)

        # ────────── (lambda - index) - ⚠️NOT USING! - FOR EXAMPLE ONLY ──────────┐
        # - Exercise
        self._exercise_subtitle = lambda index=0: page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        self._delete_exercise_btn = lambda index=0: page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        # ────────────────────────────────────────────────────────────────────────┘


    # ---------------------------------------------- ㉤ LOCATORS {dynamic} ----------------------------------------------
    # EXERCISES: —> index: Element index
    # - Exercise
    def exercise_subtitle(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')

    def delete_exercise_btn(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')

    # - Exercise form
    def exercise_form_title_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

    def exercise_form_description_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # COURSE:
    def click_create_course_btn(self):
        """
        Click <Create course Button> of the Create course page

        - ✔ Button - visible
        - ✔ Button - enabled
        - ▶ Button - Click
        """
        self.check_toolbar_create_course_btn_visible()
        self.check_toolbar_create_course_btn_enabled()
        self.create_course_btn.click()

    def click_remove_image_btn(self):
        """
        Click <Remove image Button> of the Create course page

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button text - correct
        - ▶ Button - Click
        """
        self.check_remove_image_btn()
        self.remove_image_btn.click()

    def upload_image(self, file: str):
        """
        Upload image for Course

        - ▶ Upload file form -  PROJECT/testdata/files/

        :param file: File name
        """
        self.upload_image_view_input.set_input_files(self.FILES/file)

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        """
        Fill Create course form of the Create course page

        - ▶ Form fields - Fill
        - ✔ Form fields - filled correctly

        :param title: Title
        :param estimated_time: Estimated Time
        :param description: Description
        :param max_score: Max score
        :param min_score: Min score
        """
        # Title
        self.course_form_title_field.fill(title)
        self.check_course_form_title_field_filled_correctly(title)
        # Estimated time
        self.course_form_estimated_time_field.fill(estimated_time)
        self.check_course_form_estimated_time_field_filled_correctly(estimated_time)
        # Description
        self.course_form_description_field.fill(description)
        self.check_course_form_description_field_filled_correctly(description)
        # Max score
        self.course_form_max_score_field.fill(max_score)
        self.check_course_form_max_score_field_filled_correctly(max_score)
        # Min score
        self.course_form_min_score_field.fill(min_score)
        self.check_course_form_min_score_field_filled_correctly(min_score)



    # EXERCISES:
    def click_create_exercise_btn(self):
        """
        Click <Create exercise Button> of the Create course page

        - ✔ Button - visible
        - ▶ Button - Click
        """
        self.check_exercises_toolbar_create_exercise_btn_visible()
        self.exercise_toolbar_create_exercise_btn.click()

    def click_delete_exercise_btn(self, index: int):
        """
        Click <Delete exercise Button> of the Create course page

        - ✔ Button - visible
        - ▶ Button - Click

        :param index: Exercise index
        """
        self.check_delete_exercise_btn_visible(index)
        self.delete_exercise_btn(index).click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar:
    # ────────────────────────────────────────────────┐
    def check_toolbar(self):
        """
        Check <Courses Toolbar> of the Create course page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ <Create Course button> - visible
        - ✔ <Create Course button> - enable
        """
        self.check_toolbar_title_visible()
        self.check_toolbar_title_text()
        self.check_toolbar_create_course_btn_visible()
        self.check_toolbar_create_course_btn_enabled()
    # ────────────────────────────────────────────────┘
    # Toolbar [Title]
    def check_toolbar_title_visible(self):
        """
        Check <Toolbar [Title]> of the Create course page - visible

        - ✔ Title - visible
        """
        error = '❌ <Toolbar [Title]> of the Create course page - invisible!'
        expect(self.toolbar_title, error).to_be_visible()

    def check_toolbar_title_text(self, title: str = 'Create course'):
        """
        Check <Toolbar [Title] text> of the Create course page

        - ✔ Title text - correct

        :param title: Title text

        """
        error = '❌ <Toolbar [Title] text> of the Create course page - incorrect!'
        expect(self.toolbar_title, error).to_have_text(title)

    # Toolbar [Create Course Button]
    def check_toolbar_create_course_btn_visible(self):
        """
        Check <Toolbar [Create Course Button]> of the Create course page - visible

        - ✔ Button - visible
        """
        error = '❌ <Toolbar [Create Course Button]> of the Create course page - invisible!'
        expect(self.create_course_btn, error).to_be_visible()

    def check_toolbar_create_course_btn_enabled(self):
        """
        Check <Toolbar [Create Course Button]> of the Create course page - enabled

        - ✔ Button - enabled
        """
        error = '❌ <Toolbar [Create Course Button]> of the Create course page - disabled!'
        expect(self.create_course_btn, error).to_be_enabled()

    def check_toolbar_create_course_btn_disabled(self):
        """
        Check <Toolbar [Create Course Button]> of the Create course page - disabled

        - ✔ Button - disabled
        """
        error = '❌ <Toolbar [Create Course Button]> of the Create course page - enabled!'
        expect(self.create_course_btn, error).to_be_disabled()


    # Preview View:
    # ─────────────────────────────────────────────────────────┐
    def check_preview_view(self):
        """
        Check <Preview View> of the Create course page

        If Image UPLOADED:
        -----------------
        - ✔ Image - visible

        If Image DID NOT upload:
        -----------------------
        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        if self.preview_image.is_visible():
            self.check_preview_view_image_visible()
        else:    # If image DID NOT upload
            self.check_preview_empty_view_icon_visible()
            self.check_preview_empty_view_title_visible()
            self.check_preview_empty_view_title_text()
            self.check_preview_empty_view_description_visible()
            self.check_preview_empty_view_description_text()
    # ─────────────────────────────────────────────────────────┘

    # - Preview <Empty> View [Icon]
    def check_preview_empty_view_icon_visible(self):
        """
        Check <Preview Empty View - Icon> of the Create course page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Preview Empty View - Icon> of the Create course page - invisible!'
        expect(self.preview_empty_view_icon, error).to_be_visible()

    # - Preview <Empty> View [Title]
    def check_preview_empty_view_title_visible(self):
        """
        Check <Preview Empty View [Title]> of the Create course page - visible

        - ✔ Title - visible
        """
        error = '❌ <Preview Empty View [Title]> of the Create course page - invisible!'
        expect(self.preview_empty_view_title, error).to_be_visible()

    def check_preview_empty_view_title_text(self, title: str = 'No image selected'):
        """
        Check <Preview Empty View [Title] text> of the Create course page - correct

        - ✔ Text - correct

        :param title: Title text
        """
        error = '❌ <Preview Empty View [Title] text> of the Create course page - incorrect!'
        expect(self.preview_empty_view_title, error).to_have_text(title)

    # - Preview <Empty> View [Description]
    def check_preview_empty_view_description_visible(self):
        """
        Check <Preview Empty View [Description]> of the Create course page - visible

        - ✔ Description - visible
        """
        error = '❌ <Preview Empty View [Description]> of the Create course page - invisible!'
        expect(self.preview_empty_view_description, error).to_be_visible()

    def check_preview_empty_view_description_text(self, description: str = 'Preview of selected image will be displayed here'):
        """
        Check <Preview Empty View [Description] text> of the Create course - correct

        - ✔ Text - correct

        :param description: Description text
        """
        error = '❌ <Preview Empty View [Description] text> of the Create course page - incorrect!'
        expect(self.preview_empty_view_description, error).to_have_text(description)

    # - Preview View [Image]
    def check_preview_view_image_visible(self):
        """
        Check <Preview View [Image]> of the Create course page - visible

        - ✔ Image - visible
        """
        error = '❌ <Preview View [Image]> of the Create course page - invisible!'
        expect(self.preview_image, error).to_be_visible()


    # Upload image View:
    # ────────────────────────────────────────────────────┐
    def check_upload_image_view(self):
        """
        Check <Upload image View> of the Create course page

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        - ✔ <Upload image Button> - visible | - enabled | - text
        - ✔ <Remove image Button> - invisible  (if image DID NOT upload)
        - ✔ <Remove image Button> - visible | - enabled | - text  (if image UPLOADED)
        """
        self.check_upload_image_view_icon_visible()
        self.check_upload_image_view_title_visible()
        self.check_upload_image_view_title_text()
        self.check_upload_image_view_description_visible()
        self.check_upload_image_view_description_text()
        self.check_upload_image_btn()
        self.check_remove_image_btn()
    # ────────────────────────────────────────────────────┘

    # - Upload image View [Icon]
    def check_upload_image_view_icon_visible(self):
        """
        Check <Upload image View [Icon]> of the Create course page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Upload image View [Icon]> of the Create course page - invisible!'
        expect(self.upload_image_view_icon, error).to_be_visible()

    # - Upload image View [Title]
    def check_upload_image_view_title_visible(self):
        """
        Check <Upload image View [Title]> of the Create course page - visible

        - ✔ Title - visible
        """
        error = '❌ <Upload image View [Title]> of the Create course page - invisible!'
        expect(self.upload_image_view_title, error).to_be_visible()

    def check_upload_image_view_title_text(self, title: str = 'Tap on "Upload image" button to select file'):
        """
        Check <Upload image View [Title] text> of the Create course page - correct

        - ✔ Text - correct

        :param title: Title text
        """
        error = '❌ <Upload image View [Title] text> of the Create course page - incorrect!'
        expect(self.upload_image_view_title, error).to_have_text(title)

    # - Upload image View [Description]
    def check_upload_image_view_description_visible(self):
        """
        Check <Upload image View [Description]> of the Create course page - visible

        - ✔ Description - visible

        """
        error = '❌ <Upload image View [Description]> of the Create course page - invisible!'
        expect(self.upload_image_view_description, error).to_be_visible()

    def check_upload_image_view_description_text(self, description: str = 'Recommended file size 540X300'):
        """
        Check <Upload image View [Description] text> of the Create course page - correct

        - ✔ Text - correct

        :param description: Description text
        """
        error = '❌ <Upload image View [Description] text> of the Create course page - incorrect!'
        expect(self.upload_image_view_description, error).to_have_text(description)


    # - Upload image View [Upload image Button]
    # ────────────────────────────────────────────────────┐
    def check_upload_image_btn(self):
        """
        Check <Upload image Button> of the Create course page

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Text - correct
        """
        self.check_upload_image_btn_visible()
        self.check_upload_image_btn_enable()
        self.check_upload_image_btn_text()
    # ────────────────────────────────────────────────────┘
    def check_upload_image_btn_visible(self):
        """
        Check <Upload image Button> of the Create course page - visible

        - ✔ Button - visible

        """
        error = '❌ <Upload image Button> of the Create course page - invisible!'
        expect(self.upload_image_btn, error).to_be_visible()

    def check_upload_image_btn_enable(self):
        """
        Check <Upload image Button> of the Create course page - enabled

        - ✔ Button - enabled

        """
        error = '❌ <Upload image Button> of the Create course page - disabled!'
        expect(self.upload_image_btn, error).to_be_enabled()

    def check_upload_image_btn_text(self, text: str = 'Upload image'):
        """
        Check <Upload image Button text> of the Create course page - correct

        - ✔ Text - correct

        :param text: Button text
        """
        error = '❌ <Upload image Button text> of the Create course page - incorrect!'
        expect(self.upload_image_btn, error).to_have_text(text)


    # - Upload image View [Remove image Button] (if image uploaded)
    # ────────────────────────────────────────────────────┐
    def check_remove_image_btn(self):
        """
        Check <Remove image Button> of the Create course page

        If Image UPLOADED:
        -----------------
        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button text - correct

        If Image DID NOT upload:
        -----------------------
        - ✔ Button - invisible
        """
        if self.preview_image.is_visible():  # If image uploaded
            self.check_remove_image_btn_visible()
            self.check_remove_image_btn_enable()
            self.check_remove_image_btn_text()
        else:    # If image did not upload
            self.check_remove_image_btn_invisible()
    # ────────────────────────────────────────────────────┘
    def check_remove_image_btn_visible(self):
        """
        Check <Remove image Button> of the Create course page - visible

        (For case - If image UPLOADED)

        - ✔ Button - visible

        """
        error = '❌ <Remove image Button> of the Create course page - invisible!'
        expect(self.remove_image_btn, error).to_be_visible()

    def check_remove_image_btn_invisible(self):
        """
        Check <Remove image Button> of the Create course page - invisible

        (For case - if image DID NOT upload)

        - ✔ Button - invisible

        """
        error = '❌ <Remove image Button> of the Create course page - visible!'
        expect(self.remove_image_btn, error).not_to_be_visible()

    def check_remove_image_btn_enable(self):
        """
        Check <Remove image Button> of the Create course page - enabled

        - ✔ Button - enabled

        """
        error = '❌ <Remove image Button> of the Create course page - disabled!'
        expect(self.remove_image_btn, error).to_be_enabled()

    def check_remove_image_btn_text(self, text: str = 'Remove image'):
        """
        Check <Remove image Button text> of the Create course page - correct

        - ✔ Text - correct

        :param text: Button text
        """
        error = '❌ <Remove image Button text> of the Create course page - incorrect!'
        expect(self.remove_image_btn, error).to_have_text(text)


    # Course Form:
    # ────────────────────────────────────────────────────┐
    def check_course_form(
            self,
            title: str | None = None,
            estimated_time: str | None = None,
            description: str | None = None,
            max_score: str | None = None,
            min_score: str | None = None
    ):
        """
        Check <Course Form> of the Create course page

        - ✔ Form fields - visible
        - ✔ Form fields - correct
        - ✔ Form field Placeholders - correct (except Max/Min score fields)
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


    # - Course Form [Title field]:
    # ─────────────────────────────────────────────────────────────────────┐
    def check_course_form_title(self, title: str | None = None):
        """
        Check <Course Form [Title field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct
        - ✔ Field - filled correctly (if text is passed)

        :param title: Title (optional)
        """
        self.check_course_form_title_field_visible()
        self.check_course_form_title_field_name()
        self.check_course_form_title_field_placeholder()
        if title:   # (If text is passed)
            self.check_course_form_title_field_filled_correctly(title)
    # ─────────────────────────────────────────────────────────────────────┘
    def check_course_form_title_field_visible(self):
        """
        Check <Course Form [Title field]> of the Create course page - visible!

        - ✔ Title field - visible
        """
        error = '❌ <Course Form [Title field]> of the Create course page - invisible!'
        expect(self.course_form_title_field, error).to_be_visible()

    def check_course_form_title_field_name(self, field_name: str = 'Title'):
        """
        Check <Course Form [Title field] name> of the Create course page - correct!

        - ✔ Title name - correct

        :param field_name: Field name
        """
        error = '❌ <Course Form [Title field] name> of the Create course page - incorrect!'
        expect(self.course_form_title_field, error).to_have_accessible_name(field_name)

    def check_course_form_title_field_placeholder(self, placeholder: str = 'New course'):
        """
        Check <Course Form [Title field] Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct

        :param placeholder: Placeholder
        """
        error = '❌ <Course Form [Title field] Placeholder> of the Create course page - incorrect!'
        expect(self.course_form_title_field, error).to_have_attribute('placeholder', placeholder)

    def check_course_form_title_field_filled_correctly(self, title: str):
        """
        Check <Course Form [Title field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param title: Title
        """
        error = '❌ <Course Form [Title field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_title_field, error).to_have_value(title)


    # - Course Form [Estimated time field]:
    # ──────────────────────────────────────────────────────────────────────────────────┐
    def check_course_form_estimated_time(self, estimated_time: str | None = None):
        """
        Check <Course Form [Estimated time field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field Name - correct
        - ✔ Field Placeholder - correct
        - ✔ Field - filled correctly (if text is passed)

        :param estimated_time: Estimated time (optional)
        """
        self.check_course_form_estimated_time_field_visible()
        self.check_course_form_estimated_time_field_name()
        self.check_course_form_estimated_time_field_placeholder()
        if estimated_time:   # If is passed
            self.check_course_form_estimated_time_field_filled_correctly(estimated_time)
    # ──────────────────────────────────────────────────────────────────────────────────┘
    def check_course_form_estimated_time_field_visible(self):
        """
        Check <Course Form [Estimated time field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course Form [Estimated time field]> of the Create course page - invisible!'
        expect(self.course_form_estimated_time_field, error).to_be_visible()

    def check_course_form_estimated_time_field_name(self, field_name: str = 'Estimated time'):
        """
        Check <Course Form [Estimated time field] name> of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course Form [Estimated time field] name> of the Create course page - incorrect!'
        expect(self.course_form_estimated_time_field, error).to_have_accessible_name(field_name)

    def check_course_form_estimated_time_field_placeholder(self, placeholder: str = '1h 20m'):
        """
        Check <Course Form [Estimated time field] Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct

        :param placeholder: Placeholder
        """
        error = '❌ <Course Form [Estimated time field] Placeholder> of the Create course page - incorrect!'
        expect(self.course_form_estimated_time_field, error).to_have_attribute('placeholder', placeholder)

    def check_course_form_estimated_time_field_filled_correctly(self, estimated_time: str):
        """
        Check <Course Form [Estimated time field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param estimated_time: Estimated time
        """
        error = '❌ <Course Form [Estimated time field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_estimated_time_field, error).to_have_value(estimated_time)


    # - Course Form [Description field]:
    # ────────────────────────────────────────────────────────────────────────────┐
    def check_course_form_description(self, description: str | None = None):
        """
        Check <Course Form [Description field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field placeholder - correct
        - ✔ Field - filled correctly (if text is passed)

        :param description: Description (optional)
        """
        self.check_course_form_description_field_visible()
        self.check_course_form_description_field_name()
        self.check_course_form_description_field_placeholder()
        if description:   # If is passed
            self.check_course_form_description_field_filled_correctly(description)
    # ────────────────────────────────────────────────────────────────────────────┘
    def check_course_form_description_field_visible(self):
        """
        Check <Course Form [Description field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course Form [Description field]> of the Create course page - invisible!'
        expect(self.course_form_description_field, error).to_be_visible()

    def check_course_form_description_field_name(self, field_name: str = 'Description'):
        """
        Check <Course Form [Description field] name> of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course Form [Description field] name> of the Create course page - incorrect!'
        expect(self.course_form_description_field, error).to_have_accessible_name(field_name)

    def check_course_form_description_field_placeholder(self, placeholder: str = 'Add description for course'):
        """
        Check <Course Form [Description field] Placeholder> of the Create course page - correct!

        - ✔ Placeholder - correct

        :param placeholder: Placeholder
        """
        error = '❌ <Course Form [Description field] Placeholder> of the Create course page - incorrect!'
        expect(self.course_form_description_field, error).to_have_attribute('placeholder', placeholder)

    def check_course_form_description_field_filled_correctly(self, description: str):
        """
        Check <Course Form [Description field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param description: Description
        """
        error = '❌ <Course Form [Description field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_description_field, error).to_have_value(description)


    # - Course Form [Max score field]:
    # ─────────────────────────────────────────────────────────────────────┐
    def check_course_form_max_score(self, max_score: str | None = None):
        """
        Check <Course Form [Max score field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly

        :param max_score: Max score (optional)
        """
        self.check_course_form_max_score_field_visible()
        self.check_course_form_max_score_field_name()
        if max_score:
            self.check_course_form_max_score_field_filled_correctly(max_score)
        else:
            self.check_course_form_max_score_field_filled_correctly()
    # ─────────────────────────────────────────────────────────────────────┘
    def check_course_form_max_score_field_visible(self):
        """
        Check <Course Form [Max score field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course Form [Max score field]> of the Create course page - invisible!'
        expect(self.course_form_max_score_field, error).to_be_visible()

    def check_course_form_max_score_field_name(self, field_name: str = 'Max score'):
        """
        Check <Course Form [Max score field]> name of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course Form [Max score field]> name of the Create course page - incorrect!'
        expect(self.course_form_max_score_field, error).to_have_accessible_name(field_name)

    def check_course_form_max_score_field_filled_correctly(self, max_score: str = '0'):
        """
        Check <Course Form [Max score field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param max_score: Max score
        """
        error = '❌ <Course Form [Max score field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_max_score_field, error).to_have_value(max_score)


    # - Course Form [Min score field]:
    # ───────────────────────────────────────────────────────────────────────────┐
    def check_course_form_min_score(self, min_score: str | None = None):
        """
        Check <Course Form [Min score field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly

        :param min_score: Min score
        """
        self.check_course_form_min_score_field_visible()
        self.check_course_form_min_score_field_name()
        if min_score:   # If is passed
            self.check_course_form_min_score_field_filled_correctly(min_score)
        else:
            self.check_course_form_min_score_field_filled_correctly()
    # ───────────────────────────────────────────────────────────────────────────┘
    def check_course_form_min_score_field_visible(self):
        """
        Check <Course Form [Min score field]> of the Create course page - visible!

        - ✔ Field - visible
        """
        error = '❌ <Course Form [Min score field]> of the Create course page - invisible!'
        expect(self.course_form_min_score_field, error).to_be_visible()

    def check_course_form_min_score_field_name(self, field_name: str = 'Min score'):
        """
        Check <Course Form [Min score field]> name of the Create course page - correct!

        - ✔ Field name - correct

        :param field_name: Field name
        """
        error = '❌ <Course Form [Min score field]> name of the Create course page - incorrect!'
        expect(self.course_form_min_score_field, error).to_have_accessible_name(field_name)

    def check_course_form_min_score_field_filled_correctly(self, min_score: str = '0'):
        """
        Check <Course Form [Min score field]> of the Create course page - filled correctly!

        - ✔ Field - filled correctly

        :param min_score: Min score
        """
        error = '❌ <Course Form [Min score field]> of the Create course page - filled incorrectly!'
        expect(self.course_form_min_score_field, error).to_have_value(min_score)



    # EXERCISES:
    # - Toolbar:
    # ──────────────────────────────────────────────────────────────┐
    def check_exercises_toolbar(self):
        """
        Check <Exercises Toolbar> of the Create course page

        - ✔ Title - visible
        - ✔ Text - correct
        - ✔ Create exercise Button - correct

        """
        self.check_exercises_toolbar_title_visible()
        self.check_exercises_toolbar_title_text()
        self.check_exercises_toolbar_create_exercise_btn_visible()
    # ──────────────────────────────────────────────────────────────┘
    # - Toolbar [Title]
    def check_exercises_toolbar_title_visible(self):
        """
        Check <Exercises Toolbar [Title]> of the Create course page - visible

        - ✔ Title - visible
        """
        error = '❌ <Exercises Toolbar [Title]> of the Create course page - invisible!'
        expect(self.exercise_toolbar_title, error).to_be_visible()

    def check_exercises_toolbar_title_text(self, title: str = 'Exercises'):
        """
        Check <Exercises Toolbar [Title] text> of the Create course page - correct

        - ✔ Text - correct

        :param title: Toolbar Title
        """
        error = '❌ <Exercises Toolbar [Title] text> of the Create course page - incorrect!'
        expect(self.exercise_toolbar_title, error).to_have_text(title)

    # - Toolbar [Create exercise button]
    def check_exercises_toolbar_create_exercise_btn_visible(self):
        """
        Check <Exercises Toolbar [Create exercise Button]> of the Create course page - visible

        - ✔ Button - visible
        """
        error = '❌ <Exercises Toolbar [Create exercise Button]> of the Create course page - invisible!'
        expect(self.exercise_toolbar_create_exercise_btn, error).to_be_visible()


    # - Empty view:
    # ────────────────────────────────────────────────────────┐
    def check_exercises_empty_view(self):
        """
        Check <Create exercise [Empty view]> of the Create course page

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.check_exercises_empty_view_icon_visible()
        self.check_exercises_empty_view_title_visible()
        self.check_exercises_empty_view_title()
        self.check_exercises_empty_view_description_visible()
        self.check_exercises_empty_view_description()
    # ────────────────────────────────────────────────────────┘
    # - Empty view [Icon]
    def check_exercises_empty_view_icon_visible(self):
        """
        Check <Exercises Empty view [Icon]> of the Create course page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Exercises Empty view [Icon]> of the Create course page - invisible!'
        expect(self.exercises_empty_view_icon, error).to_be_visible()

    # - Empty view [Title]
    def check_exercises_empty_view_title_visible(self):
        """
        Check <Exercises Empty view [Title]> of the Create course page - visible

        - ✔ Title - visible
        """
        error = '❌ <Exercises Empty view [Title]> of the Create course page - invisible!'
        expect(self.exercises_empty_view_title, error).to_be_visible()

    def check_exercises_empty_view_title(self, title: str = 'There is no exercises'):
        """
        Check <Exercises Empty view [Title] text> of the Create course page - correct

        - ✔ Text - correct

        :param title: Title
        """
        error = '❌ <Exercises Empty view [Title] text> of the Create course page - incorrect!'
        expect(self.exercises_empty_view_title, error).to_have_text(title)

    # - Empty view [Description]
    def check_exercises_empty_view_description_visible(self):
        """
        Check <Exercises Empty view [Description]> of the Create course page - visible

        - ✔ Description - visible
        """
        error = '❌ <Exercises Empty view [Description]> of the Create course page - invisible!'
        expect(self.exercises_empty_view_description, error).to_be_visible()

    def check_exercises_empty_view_description(self, description: str = 'Click on "Create exercise" button to create new exercise'):
        """
        Check <Exercises Empty view [Description] text> of the Create course page - correct

        - ✔ Text - correct

        :param description: Description
        """
        error = '❌ <Exercises Empty view [Description] text> of the Create course page - incorrect!'
        expect(self.exercises_empty_view_description, error).to_have_text(description)


    # - Exercise [SubTitle]:
    def check_exercise_subtitle_visible(self, index: int):
        """
        Check <Exercise [SubTitle]> of the Create course page - visible

        - ✔ SubTitle - visible

        :param index: Locator Index (ex: ...-exercise-{index}-box-toolbar-...)
        """
        error = '❌ <Exercise Toolbar [SubTitle]> of the Create course page - invisible!'
        expect(self.exercise_subtitle(index), error).to_be_visible()

    def check_exercise_subtitle_text(self, index: int):
        """
        Check <Exercise Toolbar [SubTitle] text> of the Create course page - correct

        - ✔ SubTitle text - correct (Ex: "#1 Exercise", "#2 Exercise", ...)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = '❌ <Exercise Toolbar [SubTitle] text> of the Create course page - incorrect!'
        expect(self.exercise_subtitle(index), error).to_have_text(f'#{index + 1} Exercise')

    # - Exercise [Delete exercise Button]
    def check_delete_exercise_btn_visible(self, index: int):
        """
        Check <Delete exercise Button> of the Create course page - visible

        - ✔ Button - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = '❌ <Delete exercise Button> of the Create course page - invisible!'
        expect(self.delete_exercise_btn(index), error).to_be_visible()



    # - Exercise Form
    # ────────────────────────────────────────────────────────────────────────────────┐
    def check_exercise_form(self, index: int, title: str | None = None, description: str | None = None):
        """
        Check <Exercise Form> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly (if filled)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        :param description: Exercise description
        """
        self.check_exercise_form_title_field(index, title)
        self.check_exercise_form_description_field(index, description)
    # ────────────────────────────────────────────────────────────────────────────────┘

    # - Exercise Form [Title field]
    # ──────────────────────────────────────────────────────────────────────────────┐
    def check_exercise_form_title_field(self, index: int, title: str | None = None):
        """
        Check <Exercise Form [Title field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly (if filled)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        """
        self.check_exercise_form_title_field_visible(index)
        self.check_exercise_form_title_field_name(index)
        if title:   # If is passed
            self.check_exercise_form_title_field_filled_correctly(index, title)
    # ──────────────────────────────────────────────────────────────────────────────┘
    def check_exercise_form_title_field_visible(self, index: int):
        """
        Check <Exercise Form [Title field]> of the Create course page - visible

        - ✔ Field - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = '❌ <Exercise Form [Title field]> of the Create course page - invisible!'
        expect(self.exercise_form_title_field(index), error).to_be_visible()

    def check_exercise_form_title_field_name(self, index: int):
        """
        Check <Exercise Form [Title field] name> of the Create course page - correct

        - ✔ Field - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = '❌ <Exercise Form [Title field] name> of the Create course page - incorrect!'
        expect(self.exercise_form_title_field(index), error).to_have_accessible_name('Title')

    def check_exercise_form_title_field_filled_correctly(self, index: int, title: str = 'Exercise title'):
        """
        Check <Exercise Form [Title field]> of the Create course page - filled correctly

        - ✔ Field - filled correctly

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title

        """
        error = '❌ <Exercise Form [Title field]> of the Create course page - filled incorrectly!'
        expect(self.exercise_form_title_field(index), error).to_have_value(title)


    # - Exercise Form [Description field]
    # ──────────────────────────────────────────────────────────────────────────────┐
    def check_exercise_form_description_field(self, index: int, description: str | None = None):
        """
        Check <Exercise Form [Description field]> of the Create course page

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly (if filled)

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description
        """
        self.check_exercise_form_description_field_visible(index)
        self.check_exercise_form_description_field_name(index)
        if description:  # If is passed
            self.check_exercise_form_description_field_filled_correctly(index, description)
    # ──────────────────────────────────────────────────────────────────────────────┘
    def check_exercise_form_description_field_visible(self, index: int):
        """
        Check <Exercise Form [Description field]> of the Create course page - visible

        - ✔ Field - visible

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = '❌ <Exercise Form [Description field]> of the Create course page - invisible!'
        expect(self.exercise_form_description_field(index), error).to_be_visible()

    def check_exercise_form_description_field_name(self, index: int):
        """
        Check <Exercise Form [Description field] name> of the Create course page - correct

        - ✔ Field name - correct

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = '❌ <Exercise Form [Description field] name> of the Create course page - incorrect!'
        expect(self.exercise_form_description_field(index), error).to_have_accessible_name('Description')

    def check_exercise_form_description_field_filled_correctly(self, index: int, description: str = 'Exercise description'):
        """
        Check <Exercise Form [Description field]> of the Create course page - filled correctly

        - ✔ Field - filled correctly

        :param index: Locator Index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description

        """
        error = '❌ <Exercise Form [Description field]> of the Create course page - filled incorrectly!'
        expect(self.exercise_form_description_field(index), error).to_have_value(description)
