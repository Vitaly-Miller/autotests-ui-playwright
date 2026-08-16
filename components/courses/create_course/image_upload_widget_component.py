"""
Create course page > [Image Upload Widget] component
"""

from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.views.emty_view_component import EmptyViewComponent

#=======================================================================================================================
"""
Widget:
- Upload view
- Preview [Empty view] / [Image view]
"""
class CreateCourseImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        # [Upload view]
        self.UPLOAD_VIEW_TITLE_TEXT = 'Tap on "Upload image" button to select file'
        self.UPLOAD_VIEW_DESCRIPTION_TEXT = 'Recommended file size 540X300'
        self.UPLOAD_IMAGE_BTN_TEXT = 'Upload image'
        self.REMOVE_IMAGE_BTN_TEXT = 'Remove image'  # visible after upload image only
        # Preview [Empty view]
        self.PREVIEW_EMPTY_VIEW_TITLE_TEXT = 'Tap on "Upload image" button to select file'
        self.PREVIEW_EMPTY_VIEW_DESCRIPTION_TEXT = 'Recommended file size 540X300'

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
        # Preview [Empty view]
        self.preview_empty_view = EmptyViewComponent(page=page, identifier='create-course-preview')

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        # [Upload view]
        self.upload_image_view_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.upload_image_view_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_view_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.upload_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_image_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')  # hidden input for upload file
        self.remove_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')  # visible after upload image only

        # Preview [Image View]
        self.preview_image_view = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def upload_image(self, file: str):
        """
        ▶ Upload image file

        - ▶ Upload image file form - /PROJECT/testdata/files/
        - ✔ Image - visible
        - ✔ Remove image button - visible

        :param file: Image file name
        """
        self.upload_image_input.set_input_files(self.FILES/file)
        self.check_preview(is_image_uploaded=True)
        self.check_remove_image_btn(is_image_uploaded=True)

    def click_remove_btn(self):
        """
        ▶ Click [Remove image button]

        - ✔ Button - visible | - enabled | - text
        - ▶ Button - click
        """
        self.check_remove_image_btn(is_image_uploaded=True)
        self.remove_image_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Image Upload Widget]
    def check_image_upload_widget(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Image Upload Widget]

        - ✔ Preview view - [Image view] / [Empty view]
        - ✔ Upload view - Icon | Title | Description | Remove image button

        :param is_image_uploaded: True/False
        """
        self.check_preview(is_image_uploaded)
        self.check_upload_view(is_image_uploaded)

    # [Preview]
    # ───────────────────────────────────────────────────────┐
    def check_preview(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Preview]

        Image uploaded (True):
        ------------------
        - ✔  Check <Preview [Image view]> - Image visible

        Image did NOT upload (False - default):
        ------------------
        - ✔ Check <Preview [Empty view]> - Icon | - Title | - Description

        :param is_image_uploaded: True/False
        """
        if is_image_uploaded:
            self.check_preview_image_view()
        else:
            self.check_preview_empty_view()
    # ───────────────────────────────────────────────────────┘

    # Preview [Empty view] (component)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_preview_empty_view(self):
        """
        ✔ Check <Preview [Empty view]>

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.preview_empty_view.check_empty_view(
            title=self.PREVIEW_EMPTY_VIEW_TITLE_TEXT,
            description=self.PREVIEW_EMPTY_VIEW_DESCRIPTION_TEXT)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

    # Preview [Image view]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_preview_image_view(self):
        """
        ✔ Check <Preview [Image view]>

        - ✔ Image - visible
        """
        self.check_preview_image_view_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_preview_image_view_visible(self):
        """
        ✔ Check <Preview [Image view]> visible

        .
        """
        error = f'❌ Create course page > Image upload widget > Preview > [Image view] - invisible!'
        expect(self.preview_image_view, error).to_be_visible()


    # [Upload view]
    # ─────────────────────────────────────────────────────────────────┐
    def check_upload_view(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Upload view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        - ✔ Upload image button - visible | - enabled | - text
        - ✔ Remove image button - visible/invisible | - enabled | - text
        """
        self.check_upload_view_icon()
        self.check_upload_view_title()
        self.check_upload_view_description()
        self.check_upload_image_btn()
        self.check_remove_image_btn(is_image_uploaded)
    # ─────────────────────────────────────────────────────────────────┘

    # - Upload view [Icon]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_view_icon(self):
        """
        ✔ Check [Icon]

        - ✔ Icon - visible
        """
        self.check_upload_view_icon_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_upload_view_icon_visible(self):
        """
        ✔ Check [Icon]> visible

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Icon] - invisible!'
        expect(self.upload_image_view_icon, error).to_be_visible()


    # - Upload view [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_view_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Text - correct
        """
        self.check_upload_view_title_visible()
        self.check_upload_view_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_upload_view_title_visible(self):
        """
        ✔ Check [Title] visible

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Title] - invisible!'
        expect(self.upload_image_view_title, error).to_be_visible()

    def check_upload_view_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Title] - incorrect text!'
        expect(self.upload_image_view_title, error).to_have_text(self.UPLOAD_VIEW_TITLE_TEXT)


    # - Upload view [Description]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_view_description(self):
        """
        ✔ Check [Description]

        - ✔ Description - visible
        - ✔ Text - correct
        """
        self.check_upload_view_description_visible()
        self.check_upload_view_description_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_upload_view_description_visible(self):
        """
        ✔ Check [Description] visible

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Description] - invisible!'
        expect(self.upload_image_view_description, error).to_be_visible()

    def check_upload_view_description_text(self):
        """
        ✔ Check [Description] text

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Description] - incorrect text!'
        expect(self.upload_image_view_description, error).to_have_text(self.UPLOAD_VIEW_DESCRIPTION_TEXT)


    # - Upload view [Upload image button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_image_btn(self, ):
        """
        ✔ Check <Upload image button>

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Text - correct
        """
        self.check_upload_image_btn_visible()
        self.check_upload_image_btn_enable()
        self.check_upload_image_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_upload_image_btn_visible(self):
        """
        ✔ Check [Upload image button] visible

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Upload image button] - invisible!'
        expect(self.upload_image_btn, error).to_be_visible()

    def check_upload_image_btn_enable(self):
        """
        ✔ Check [Upload image button] enabled

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Upload image button] - disabled!'
        expect(self.upload_image_btn, error).to_be_enabled()

    def check_upload_image_btn_text(self):
        """
        ✔ Check [Upload image button] text

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Upload image button] - incorrect text!'
        expect(self.upload_image_btn, error).to_have_text(self.UPLOAD_IMAGE_BTN_TEXT)


    # - Upload view [Remove image button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_remove_image_btn(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Remove image button]

        Image uploaded (True):
        -----------------
        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button text - correct

        Image did NOT upload (False - default):
        -----------------------
        - ✔ Button - invisible

        :param is_image_uploaded: True/False
        """
        if is_image_uploaded:
            self.check_remove_image_btn_visible()
            self.check_remove_image_btn_enable()
            self.check_remove_image_btn_text()
        else:
            self.check_remove_image_btn_invisible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_remove_image_btn_visible(self):
        """
        ✔ Check [Remove image button] visible

        (For case - If image UPLOADED)

        - ✔ Button - visible
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Remove image button] - invisible!'
        expect(self.remove_image_btn, error).to_be_visible()

    def check_remove_image_btn_invisible(self):
        """
        ✔ Check [Remove image button] invisible

        (For case - if image did NOT upload)
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Remove image button] - visible!'
        expect(self.remove_image_btn, error).not_to_be_visible()

    def check_remove_image_btn_enable(self):
        """
        ✔ Check [Remove image button] enabled

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Remove image button] - disabled!'
        expect(self.remove_image_btn, error).to_be_enabled()

    def check_remove_image_btn_text(self):
        """
        ✔ Check [Remove image button] text

        .
        """
        error = f'❌ Create course page > Image upload widget > Upload view > [Remove image button] - incorrect text!'
        expect(self.remove_image_btn, error).to_have_text(self.REMOVE_IMAGE_BTN_TEXT)
