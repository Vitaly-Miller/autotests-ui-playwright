"""
Image upload widget (component)
"""

import allure
from components.base_component import BaseComponent
from components.views.empty_view import EmptyViewComponent
from playwright.sync_api import Locator, Page
from elements.button import Button
from elements.icon import Icon
from elements.image import Image
from elements.input_file import InputFile
from elements.text import Text

#=======================================================================================================================
class CreateCourseImageUploadWidgetComponent(BaseComponent):
    """
    Image upload widget (component)

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
    PATH = 'Create course page > Image upload widget'
    IDENTIFIER = 'create-course-preview'

    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        self.preview_view_empty_view = EmptyViewComponent(page=page, identifier=self.IDENTIFIER, path=self.PATH)


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

    def upload_image_input_locator(self) -> Locator:       # hidden input for upload file
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-input')

    def remove_image_btn_locator(self) -> Locator:         # visible after upload image only
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')

    # Preview view [Image view]
    def preview_view_image_view_locator(self) -> Locator:
        return self.page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')


    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    # [Upload view]
    def upload_view_icon(self) -> Icon:
        return Icon(self.upload_view_icon_locator(), self.PATH, 'Upload view - Icon')

    def upload_view_title(self) -> Text:
        return Text(self.upload_view_title_locator(), self.PATH, 'Upload view - Title')

    def upload_view_description(self) -> Text:
        return Text(self.upload_view_description_locator(), self.PATH, 'Upload view - Description')

    def upload_image_btn(self) -> Button:
        return Button(self.upload_image_btn_locator(), self.PATH, 'Upload image button')

    def upload_image_input(self) -> InputFile:
        return InputFile(self.upload_image_input_locator(), self.PATH, 'Upload image input')

    def remove_image_btn(self) -> Button:
        return Button(self.remove_image_btn_locator(), self.PATH, 'Remove image button')

    # Preview view [Image view]
    def preview_view_image_view(self) -> Image:
        return Image(self.preview_view_image_view_locator(), self.PATH, 'Preview view - Image view')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Upload image file
    def upload_image(self, file: str):
        """
        ▶ Upload image file (from /PROJECT/testdata/files/)

        - ▶ Input - set file
        - ✔ Image view - visible
        - ✔ Remove image button - visible

        :param file: Image file name
        """
        self.upload_image_input().upload(file)

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
        self.check_preview_view(is_image_uploaded)
        self.check_upload_view(is_image_uploaded)
    # ───────────────────────────────────────────────┘

    # [Preview view]
    # ──────────────────────────────────────────┐
    @allure.step('✔ Check [Preview view]')
    def check_preview_view(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Preview view]

        Image uploaded (True):
        ----------------------
        - ✔ Preview view [Image view]

        Image did NOT upload (False - default):
        ---------------------------------------
        - ✔ Preview view [Empty view]

        :param is_image_uploaded: True / False
        """
        if is_image_uploaded:
            self.check_preview_view_image_view()
        else:
            self.check_preview_view_empty_view()
    # ───────────────────────────────────────────┘

    # Preview view [Empty view] (component)
    def check_preview_view_empty_view(self):
        """
        ✔ Check Preview view [Empty view]

        - ✔ Icon
        - ✔ Title
        - ✔ Description
        """
        self.preview_view_empty_view.check(
            title='Tap on "Upload image" button to select file',
            description='Recommended file size 540X300'
        )

    # Preview view [Image view]
    @allure.step('✔ Check [Image view]')
    def check_preview_view_image_view(self):
        """
        ✔ Check [Image view]

        - ✔ Image view - visible
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
    @allure.step('✔ Check [Icon]')
    def check_upload_view_icon(self):
        """
        ✔ Check [Icon]

        - ✔ Icon - visible
        """
        self.upload_view_icon().check_visible()


    # Upload view [Title]
    @allure.step('✔ Check [Title]')
    def check_upload_view_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.upload_view_title().check_visible()
        self.upload_view_title().check_text('Tap on "Upload image" button to select file')


    # Upload view [Description]
    @allure.step('✔ Check [Description]')
    def check_upload_view_description(self):
        """
        ✔ Check [Description]

        - ✔ Description - visible
        - ✔ Description - text
        """
        self.upload_view_description().check_visible()
        self.upload_view_description().check_text('Recommended file size 540X300')


    # Upload view [Upload image button]
    @allure.step('✔ Check [Upload image button]')
    def check_upload_image_btn(self):
        """
        ✔ Check [Upload image button]

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button - text
        """
        self.upload_image_btn().check_visible()
        self.upload_image_btn().check_enabled()
        self.upload_image_btn().check_text('Upload image')


    # Upload view [Remove image button]
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
            self.remove_image_btn().check_visible()
            self.remove_image_btn().check_enabled()
            self.remove_image_btn().check_text('Remove image')
        else:
            self.remove_image_btn().check_hidden()


#=======================================================================================================================
