"""
Create course page > [Image upload widget] (component)
"""
import allure
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.views.emty_view_component import EmptyViewComponent

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
    def __init__(self, page: Page):
        super().__init__(page)

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        # [Upload view]
        self.UPLOAD_VIEW_TITLE_TEXT = 'Tap on "Upload image" button to select file'
        self.UPLOAD_VIEW_DESCRIPTION_TEXT = 'Recommended file size 540X300'
        self.UPLOAD_IMAGE_BTN_TEXT = 'Upload image'
        self.REMOVE_IMAGE_BTN_TEXT = 'Remove image'  # visible after upload image only
        # Preview view [Empty view]
        self.PREVIEW_EMPTY_VIEW_TITLE_TEXT = 'Tap on "Upload image" button to select file'
        self.PREVIEW_EMPTY_VIEW_DESCRIPTION_TEXT = 'Recommended file size 540X300'

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.image_upload_widget_component = '❌ Create course page > Image upload widget'
        self.preview_view_image_view_element = f'{self.image_upload_widget_component} > Preview view > [Image view]'
        self.upload_view_icon_element = f'{self.image_upload_widget_component} > Upload view > [Icon]'
        self.upload_view_title_element = f'{self.image_upload_widget_component} > Upload view > [Title]'
        self.upload_view_description_element = f'{self.image_upload_widget_component} > Upload view > [Description]'
        self.upload_image_btn_element = f'{self.image_upload_widget_component} > Upload view > [Upload image button]'
        self.remove_image_btn_element = f'{self.image_upload_widget_component} > Uploaded view > [Remove image button]'

        # --------------------------------------------- ⿳ COMPONENTS --------------------------------------------------
        self.preview_view_empty_view = EmptyViewComponent(
            page=page,
            identifier='create-course-preview',
            component=f'{self.image_upload_widget_component}'
        )
        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        # [Upload view]
        self.upload_view_image_view_icon = page.get_by_test_id('create-course-preview-image-upload-widget-info-icon')
        self.upload_view_image_view_title = page.get_by_test_id('create-course-preview-image-upload-widget-info-title-text')
        self.upload_view_image_view_description = page.get_by_test_id('create-course-preview-image-upload-widget-info-description-text')
        self.upload_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-upload-button')
        self.upload_image_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')        # hidden input for upload file
        self.remove_image_btn = page.get_by_test_id('create-course-preview-image-upload-widget-remove-button')  # visible after upload image only
        # Preview view [Image View]
        self.preview_view_image_view = page.get_by_test_id('create-course-preview-image-upload-widget-preview-image')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # [Upload image]
    @allure.step('▶ Upload image file')
    def upload_image(self, file: str):
        """
        ▶ Upload image file

        - ▶ Upload image file form - /PROJECT/testdata/files/
        - ✔ Image - visible
        - ✔ Remove image button - visible

        :param file: Image file name
        """
        self.upload_image_input.set_input_files(self.FILES/file)
        self.check_preview_view_image_view_visible()
        self.check_remove_image_btn_visible()

    # Click [Remove image button]
    @allure.step('▶ Click [Remove image button]')
    def click_remove_btn(self):
        """
        ▶ Click [Remove image button]

        - ✔ Button - enabled
        - ▶ Button - click
        """
        self.check_remove_image_btn_enable()
        self.remove_image_btn.click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Image upload widget]
    # ───────────────────────────────────────────────┐
    @allure.step('✔ Check [Image upload widget]')
    def check(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Image upload widget]

        - ✔ Preview view - [Image view] / [Empty view]
        - ✔ Upload view - Icon | - Title | - Description | - Remove image button

        :param is_image_uploaded: True/False
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
        - ✔  Check <Preview view [Image view]> - Image visible

        Image did NOT upload (False - default):
        ---------------------------------------
        - ✔ Check <Preview view [Empty view]> - Icon | - Title | - Description

        :param is_image_uploaded: True/False
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
        ✔ Check [Empty view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text
        """
        self.preview_view_empty_view.check(
            title=self.PREVIEW_EMPTY_VIEW_TITLE_TEXT,
            description=self.PREVIEW_EMPTY_VIEW_DESCRIPTION_TEXT)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

    # Preview view [Image view]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Image view]')
    def check_preview_view_image_view(self):
        """
        ✔ Check [Image view]

        - ✔ Image view - image
        """
        self.check_preview_view_image_view_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Image view] is visible')
    def check_preview_view_image_view_visible(self):
        """
        ✔ Check [Image view]  is visible

        - Image view - image
        """
        error = f'{self.preview_view_image_view_element} - invisible!'
        expect(self.preview_view_image_view, error).to_be_visible()


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
        - ✔ Remove image button - visible/invisible | - enabled | - text
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
    @allure.step('✔ Check [Icon] is visible')
    def check_upload_view_icon_visible(self):
        """
        ✔ Check [Icon]  is visible

        .
        """
        error = f'{self.upload_view_icon_element} - invisible!'
        expect(self.upload_view_image_view_icon, error).to_be_visible()


    # Upload view [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_upload_view_title(self):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text
        """
        self.check_upload_view_title_visible()
        self.check_upload_view_title_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Title] is visible')
    def check_upload_view_title_visible(self):
        """
        ✔ Check [Title]  is visible

        .
        """
        error = f'{self.upload_view_title_element} - invisible!'
        expect(self.upload_view_image_view_title, error).to_be_visible()

    @allure.step('✔ Check [Title] text')
    def check_upload_view_title_text(self):
        """
        ✔ Check [Title] text

        .
        """
        error = f'{self.upload_view_title_element} - incorrect text!'
        expect(self.upload_view_image_view_title, error).to_have_text(self.UPLOAD_VIEW_TITLE_TEXT)


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
    @allure.step('✔ Check [Description] is visible')
    def check_upload_view_description_visible(self):
        """
        ✔ Check [Description]  is visible

        .
        """
        error = f'{self.upload_view_description_element} - invisible!'
        expect(self.upload_view_image_view_description, error).to_be_visible()

    @allure.step('✔ Check [Description] text')
    def check_upload_view_description_text(self):
        """
        ✔ Check [Description] text

        .
        """
        error = f'{self.upload_view_description_element} - incorrect text!'
        expect(self.upload_view_image_view_description, error).to_have_text(self.UPLOAD_VIEW_DESCRIPTION_TEXT)


    # Upload view [Upload image button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Upload image button]')
    def check_upload_image_btn(self, ):
        """
        ✔ Check [Upload image button]

        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button - text
        """
        self.check_upload_image_btn_visible()
        self.check_upload_image_btn_enable()
        self.check_upload_image_btn_text()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Upload image button] is visible')
    def check_upload_image_btn_visible(self):
        """
        ✔ Check [Upload image button]  is visible

        .
        """
        error = f'{self.upload_image_btn_element} - invisible!'
        expect(self.upload_image_btn, error).to_be_visible()

    @allure.step('✔ Check [Upload image button] is enable')
    def check_upload_image_btn_enable(self):
        """
        ✔ Check [Upload image button] is enabled

        .
        """
        error = f'{self.upload_image_btn_element} - disabled!'
        expect(self.upload_image_btn, error).to_be_enabled()

    @allure.step('✔ Check [Upload image button] text')
    def check_upload_image_btn_text(self):
        """
        ✔ Check [Upload image button] text

        .
        """
        error = f'{self.upload_image_btn_element} - incorrect text!'
        expect(self.upload_image_btn, error).to_have_text(self.UPLOAD_IMAGE_BTN_TEXT)


    # Upload view [Remove image button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_remove_image_btn(self, is_image_uploaded: bool = False):
        """
        ✔ Check [Remove image button]

        Image uploaded (True):
        ----------------------
        - ✔ Button - visible
        - ✔ Button - enabled
        - ✔ Button - text

        Image did NOT upload (False - default):
        ---------------------------------------
        - ✔ Button - invisible

        :param is_image_uploaded: True/False
        """
        if is_image_uploaded:
            with allure.step('✔ Check [Remove image button] UI'):
                self.check_remove_image_btn_visible()
                self.check_remove_image_btn_enable()
                self.check_remove_image_btn_text()
        else:
            self.check_remove_image_btn_invisible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Remove image button] is visible')
    def check_remove_image_btn_visible(self):
        """
        ✔ Check [Remove image button]  is visible

        (For case - If image UPLOADED)

        - ✔ Button - visible
        """
        error = f'{self.remove_image_btn_element} - invisible!'
        expect(self.remove_image_btn, error).to_be_visible()

    @allure.step('✔ Check [Remove image button] is invisible')
    def check_remove_image_btn_invisible(self):
        """
        ✔ Check [Remove image button] is invisible

        (For case - if image did NOT upload)
        """
        error = f'{self.remove_image_btn_element} - visible!'
        expect(self.remove_image_btn, error).not_to_be_visible()

    @allure.step('✔ Check [Remove image button] is enable')
    def check_remove_image_btn_enable(self):
        """
        ✔ Check [Remove image button] is enabled

        .
        """
        error = f'{self.remove_image_btn_element} - disabled!'
        expect(self.remove_image_btn, error).to_be_enabled()

    @allure.step('✔ Check [Remove image button] text')
    def check_remove_image_btn_text(self):
        """
        ✔ Check [Remove image button] text

        .
        """
        error = f'{self.remove_image_btn_element} - incorrect text!'
        expect(self.remove_image_btn, error).to_have_text(self.REMOVE_IMAGE_BTN_TEXT)
