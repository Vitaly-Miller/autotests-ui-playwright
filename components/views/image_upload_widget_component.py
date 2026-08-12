"""
Image Upload Widget component
"""

from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.views.emty_view_component import EmptyViewComponent

#=======================================================================================================================
"""
Elements:
- Preview empty view
- Preview image view
- Upload empty view
- Upload view
"""
class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.IDENTIFIER = 'create-course-preview'   # Unique part of locator
        # Upload View
        self.UPLOAD_VIEW_TITLE_TEXT = 'Tap on "Upload image" button to select file'
        self.UPLOAD_VIEW_DESCRIPTION_TEXT = 'Recommended file size 540X300'
        self.UPLOAD_IMAGE_BUTTON_TEXT = 'Upload image'
        self.REMOVE_IMAGE_BUTTON_TEXT = 'Remove image'
        # Preview
        self.PREVIEW_EMPTY_VIEW_TITLE = 'Tap on "Upload image" button to select file'
        self.PREVIEW_EMPTY_VIEW_DESCRIPTION = 'Recommended file size 540X300'

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
        # Preview [Empty view]
        self.preview_empty_view = EmptyViewComponent(page=page, identifier=self.IDENTIFIER)

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        # Preview [Image View]
        self.preview_image_view = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

        # Upload Image View
        self.upload_image_view_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.upload_image_view_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_image_view_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')

        # Upload Image View [Buttons]
        self.upload_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_image_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')       # hidden input for upload file
        self.remove_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button') # visible after upload image only

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------


    def click_remove_btn(self):
        """
        Click <Remove image Button> of the Create course page

        - ✔ Button - visible | - enabled | - text
        - ▶ Button - click
        """
        self.check_remove_image_btn()
        self.remove_image_btn.click()

    def upload_image(self, file: str):
        """
        Upload image for Course

        - ▶ Upload image file form - /PROJECT/testdata/files/
        - ✔ Image - visible
        - ✔ Remove image button - visible

        :param file: Image file name
        """
        self.upload_image_input.set_input_files(self.FILES/file)
        self.check_preview_image_view()
        self.check_remove_image_btn()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Preview [Empty view] (component)
    # ──────────────────────────────────────────────────────╮
    def check_preview_empty_view(self):
        """
        ✔ Check [Preview Empty view] component

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.preview_empty_view.check_component(
            title=self.PREVIEW_EMPTY_VIEW_TITLE,
            description=self.PREVIEW_EMPTY_VIEW_DESCRIPTION)
    # ──────────────────────────────────────────────────────╯

    # Preview [Image View]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_preview_image_view(self):
        """
        ✔ Check [Image view]

        - ✔ Image - visible
        """
        self.check_preview_image_view_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_preview_image_view_visible(self):
        """
        ✔ Check [Image view] visible

        .
        """
        error = f'❌ Create course page -> Upload widget -> Preview -> [Image view] - invisible!'
        expect(self.preview_image_view, error).to_be_visible()


    # Upload image view:
    # ─────────────────────────────────────────────┐
    def check_upload_image_view(self):
        """
        ✔ Check [Upload image view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        - ✔ Upload image button - visible | - enabled | - text
        - ✔ Remove image button - visible/invisible | - enabled | - text
        """
        self.check_upload_image_view_icon()
        self.check_upload_image_view_title()
        self.check_upload_image_view_description()
        self.check_upload_image_btn()
        self.check_remove_image_btn()
    # ─────────────────────────────────────────────┘

    # Upload image view [Icon]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_image_view_icon(self):
        """
        ✔ Check <Upload image View [Icon]>

        - ✔ Icon - visible
        """
        self.check_upload_image_view_icon_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_upload_image_view_icon_visible(self):
        """
        ✔ Check [Icon]> visible

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Icon] - invisible!'
        expect(self.upload_image_view_icon, error).to_be_visible()


    # Upload image view [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_image_view_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Text - correct
        """
        self.check_upload_image_view_title_visible()
        self.check_upload_image_view_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_upload_image_view_title_visible(self):
        """
        ✔ Check [Title] visible

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Title] - invisible!'
        expect(self.upload_image_view_title, error).to_be_visible()

    def check_upload_image_view_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Title] - incorrect text!'
        expect(self.upload_image_view_title, error).to_have_text(self.UPLOAD_VIEW_TITLE_TEXT)


    # Upload image view [Description]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_image_view_description(self):
        """
        ✔ Check [Description]

        - ✔ Description - visible
        - ✔ Text - correct
        """
        self.check_upload_image_view_description_visible()
        self.check_upload_image_view_description_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_upload_image_view_description_visible(self):
        """
        ✔ Check [Description] visible

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image View -> [Description] - invisible!'
        expect(self.upload_image_view_description, error).to_be_visible()

    def check_upload_image_view_description_text(self):
        """
        ✔ Check [Description] text

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image View -> [Description] - incorrect text!'
        expect(self.upload_image_view_description, error).to_have_text(self.UPLOAD_VIEW_DESCRIPTION_TEXT)


    # Upload image view [Upload image Button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_image_btn(self):
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
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Upload image button] - invisible!'
        expect(self.upload_image_btn, error).to_be_visible()

    def check_upload_image_btn_enable(self):
        """
        ✔ Check [Upload image button] enabled

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Upload image button] - disabled!'
        expect(self.upload_image_btn, error).to_be_enabled()

    def check_upload_image_btn_text(self):
        """
        ✔ Check [Upload image button] text

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Upload image button] - incorrect text!'
        expect(self.upload_image_btn, error).to_have_text(self.UPLOAD_IMAGE_BUTTON_TEXT)


    # Upload image view [Remove image button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_remove_image_btn(self):
        """
        ✔ Check [Remove image button]

        If image UPLOADED (auto checking):
        -----------------
        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button text - correct

        If image did NOT upload (auto checking):
        -----------------------
        - ✔ Button - invisible
        """
        if self.preview_image_view.is_visible():
            self.check_remove_image_btn_visible()
            self.check_remove_image_btn_enable()
            self.check_remove_image_btn_text()
        else:
            self.check_remove_image_btn_invisible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_remove_image_btn_visible(self):
        """
        ✔ Check [Remove image button] visible

        (For case - If image UPLOADED)

        - ✔ Button - visible
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Remove image button] - invisible!'
        expect(self.remove_image_btn, error).to_be_visible()

    def check_remove_image_btn_invisible(self):
        """
        ✔ Check [Remove image button] invisible

        (For case - if image did NOT upload)
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Remove image button] - visible!'
        expect(self.remove_image_btn, error).not_to_be_visible()

    def check_remove_image_btn_enable(self):
        """
        ✔ Check [Remove image button] enabled

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Remove image button] - disabled!'
        expect(self.remove_image_btn, error).to_be_enabled()

    def check_remove_image_btn_text(self):
        """
        ✔ Check [Remove image button] text

        .
        """
        error = f'❌ Create course page -> Upload widget -> Upload image view -> [Remove image button] - incorrect text!'
        expect(self.remove_image_btn, error).to_have_text(self.REMOVE_IMAGE_BUTTON_TEXT)
