"""
Create course page > [Image upload widget]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from playwright.sync_api import Locator, Page
from elements.button import Button
from elements.icon import Icon
from elements.image import Image
from elements.input_file import InputFile
from elements.text import Text

#=======================================================================================================================
"""
[Image upload widget]:
- Upload view:
    - Icon
    - Title
    - Description
    - Upload image button
    - Remove image button
- Preview view:
    - Empty view (component)
    - Image view
"""
class CreateCourseImageUploadWidgetComponent(BaseComponent):
    path = 'Create course page > Image upload widget'

    # 𝌆 DATA
    # [Upload view]
    IDENTIFIER = 'create-course-preview'
    UPLOAD_VIEW_TITLE_TEXT = 'Tap on "Upload image" button to select file'
    UPLOAD_VIEW_DESCRIPTION_TEXT = 'Recommended file size 540X300'
    UPLOAD_IMAGE_BTN_TEXT = 'Upload image'
    REMOVE_IMAGE_BTN_TEXT = 'Remove image'  # visible after upload image only
    # Preview view [Empty view]
    PREVIEW_EMPTY_VIEW_TITLE_TEXT = 'Tap on "Upload image" button to select file'
    PREVIEW_EMPTY_VIEW_DESCRIPTION_TEXT = 'Recommended file size 540X300'

    def __init__(self, page: Page):
        super().__init__(page)

        # --------------------------------------------- ⿳ COMPONENTS --------------------------------------------------
        self.preview_view_empty_view = EmptyViewComponent(page=page, identifier=self.IDENTIFIER, path=self.path)

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    # [Upload view]
    def upload_view_icon_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')

    def upload_view_title_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')

    def upload_view_description_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')

    def upload_image_btn_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')

    def upload_image_input_locator(self) -> Locator:  # hidden input for upload file
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-input')

    def remove_image_btn_locator(self) -> Locator:  # visible after upload image only
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

    # Preview view [Image view]
    def preview_view_image_view_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')

    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    # [Upload view]
    def upload_view_icon(self) -> Icon:
        return Icon(self.upload_view_icon_locator(), self.path, 'Upload view - Icon')

    def upload_view_title(self) -> Text:
        return Text(self.upload_view_title_locator(), self.path, 'Upload view - Title')

    def upload_view_description(self) -> Text:
        return Text(self.upload_view_description_locator(), self.path, 'Upload view - Description')

    def upload_image_btn(self) -> Button:
        return Button(self.upload_image_btn_locator(), self.path, 'Upload image button')

    def upload_image_input(self) -> InputFile:
        return InputFile(self.upload_image_input_locator(), self.path, 'Upload image input')

    def remove_image_btn(self) -> Button:
        return Button(self.remove_image_btn_locator(), self.path, 'Remove image button')

    # Preview view [Image view]
    def preview_view_image_view(self) -> Image:
        return Image(self.preview_view_image_view_locator(), self.path, 'Preview view - Image view')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Upload image file
    @allure.step('▶ Upload image file')
    def upload_image(self, file: str):
        """
        ▶ Upload image file (from /PROJECT/testdata/files/)

        - ▶ Input - set file
        - ✔ Image view - visible
        - ✔ Remove image button - visible

        :param file: Image file name
        """
        self.upload_image_input().upload(file)
        self.check_preview_view_image_view_visible()
        self.check_remove_image_btn_visible()

    # Click [Remove image button]
    def click_remove_btn(self):
        """
        ▶ Click [Remove image button]

        .
        """
        self.remove_image_btn().click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Image upload widget]
    # ───────────────────────────────────────────────┐
    @allure.step('✔ Check [Image upload widget]')
    def check(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Image upload widget]

        - ✔ Preview view - [Image view] / [Empty view]
        - ✔ Upload view - Icon | - Title | - Description | - Remove image button

        :param is_image_uploaded: True / False
        """
        self.check_preview(is_image_uploaded)
        self.check_upload_view(is_image_uploaded)
    # ───────────────────────────────────────────────┘

    # [Preview view]
    # ───────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Preview view]')
    def check_preview(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Preview view]

        Image uploaded (True):
        ----------------------
        - ✔ Preview view [Image view] - image visible

        Image did NOT upload (False - default):
        ---------------------------------------
        - ✔ Preview view [Empty view] - Icon | - Title | - Description

        :param is_image_uploaded: True / False
        """
        if is_image_uploaded:
            self.check_preview_view_image_view()
        else:
            self.check_preview_view_empty_view()
    # ───────────────────────────────────────────────────────┘

    # Preview view [Empty view] (component)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_preview_view_empty_view(self):
        """
        ✔ Check Preview view [Empty view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.preview_view_empty_view.check(
            title=self.PREVIEW_EMPTY_VIEW_TITLE_TEXT,
            description=self.PREVIEW_EMPTY_VIEW_DESCRIPTION_TEXT
        )
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

    # Preview view [Image view]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Image view]')
    def check_preview_view_image_view(self):
        """
        ✔ Check [Image view]

        - ✔ Image view - visible
        """
        self.check_preview_view_image_view_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_preview_view_image_view_visible(self):
        """
        ✔ Check [Image view] is visible

        .
        """
        self.preview_view_image_view().check_visible()


    # [Upload view]
    # ────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Upload view]')
    def check_upload_view(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Upload view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        - ✔ Upload image button - visible | - enabled | - text
        - ✔ Remove image button - visible/hidden | - enabled | - text

        :param is_image_uploaded: True / False
        """
        self.check_upload_view_icon()
        self.check_upload_view_title()
        self.check_upload_view_description()
        self.check_upload_image_btn()
        self.check_remove_image_btn(is_image_uploaded)
    # ────────────────────────────────────────────────────────────┘

    # Upload view [Icon]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Icon]')
    def check_upload_view_icon(self):
        """
        ✔ Check [Icon]

        - ✔ Icon - visible
        """
        self.check_upload_view_icon_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_upload_view_icon_visible(self):
        """
        ✔ Check [Icon] is visible

        .
        """
        self.upload_view_icon().check_visible()


    # Upload view [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_upload_view_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.check_upload_view_title_visible()
        self.check_upload_view_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_upload_view_title_visible(self):
        """
        ✔ Check [Title] is visible

        .
        """
        self.upload_view_title().check_visible()

    # Text
    def check_upload_view_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        self.upload_view_title().check_text(self.UPLOAD_VIEW_TITLE_TEXT)


    # Upload view [Description]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Description]')
    def check_upload_view_description(self):
        """
        ✔ Check [Description]

        - ✔ Description - visible
        - ✔ Description - text
        """
        self.check_upload_view_description_visible()
        self.check_upload_view_description_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_upload_view_description_visible(self):
        """
        ✔ Check [Description] is visible

        .
        """
        self.upload_view_description().check_visible()

    # Text
    def check_upload_view_description_text(self):
        """
        ✔ Check [Description] text

        .
        """
        self.upload_view_description().check_text(self.UPLOAD_VIEW_DESCRIPTION_TEXT)


    # Upload view [Upload image button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Upload image button]')
    def check_upload_image_btn(self):
        """
        ✔ Check [Upload image button]

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button - text
        """
        self.check_upload_image_btn_visible()
        self.check_upload_image_btn_enabled()
        self.check_upload_image_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_upload_image_btn_visible(self):
        """
        ✔ Check [Upload image button] is visible

        .
        """
        self.upload_image_btn().check_visible()

    # Enabled
    def check_upload_image_btn_enabled(self):
        """
        ✔ Check [Upload image button] is enabled

        .
        """
        self.upload_image_btn().check_enabled()

    # Text
    def check_upload_image_btn_text(self):
        """
        ✔ Check [Upload image button] text

        .
        """
        self.upload_image_btn().check_text(self.UPLOAD_IMAGE_BTN_TEXT)


    # Upload view [Remove image button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Remove image button]')
    def check_remove_image_btn(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Remove image button]

        Image uploaded (True):
        ----------------------
        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button - text

        Image did NOT upload (False by default):
        ---------------------------------------
        - ✔ Button - hidden

        :param is_image_uploaded: True / False
        """
        if is_image_uploaded:
            self.check_remove_image_btn_visible()
            self.check_remove_image_btn_enabled()
            self.check_remove_image_btn_text()
        else:
            self.check_remove_image_btn_hidden()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_remove_image_btn_visible(self):
        """
        ✔ Check [Remove image button] is visible

        (For case - if image UPLOADED)
        """
        self.remove_image_btn().check_visible()

    # Hidden
    def check_remove_image_btn_hidden(self):
        """
        ✔ Check [Remove image button] is hidden

        (For case - if image did NOT upload)
        """
        self.remove_image_btn().check_hidden()

    # Enabled
    def check_remove_image_btn_enabled(self):
        """
        ✔ Check [Remove image button] is enabled

        .
        """
        self.remove_image_btn().check_enabled()

    # Text
    def check_remove_image_btn_text(self):
        """
        ✔ Check [Remove image button] text

        .
        """
        self.remove_image_btn().check_text(self.REMOVE_IMAGE_BTN_TEXT)


#=======================================================================================================================
