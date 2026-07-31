"""
Courses listpage
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class CoursesListPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ┌╴ 𝌆 DATA:
        # ├ Page URL
        self.url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'


        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_btn = page.get_by_test_id('courses-list-toolbar-create-course-button')
        # ├ Empty view
        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')
        # ├ Course Card
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')
        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_memu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_memu_button = page.get_by_test_id('course-view-delete-menu-item')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_create_course_btn(self):
        """
        Click <Create course> button

        - ✔ Button - visible
        - ▶ Button - Click
        """
        expect(self.create_course_btn).to_be_visible()
        self.create_course_btn.click()


    def click_course_menu_btn(self, index: int = 0):
        """
        Click <Course menu> button

        - ✔ <Course menu> button - enabled
        - ▶ <Course menu> button - Click

        :param index: Element index if more than one <Course Card>
        """
        expect(self.course_edit_memu_button.nth(index)).to_be_enabled()
        self.course_menu_button.nth(index).click()


    def click_edit_course_btn(self, index: int = 0):
        """
        Click <Edit course> button

        - ▶ <Course menu> button - Click (func)
        - ✔ <Edit course> button - enabled
        - ▶ <Edit course> button - Click

        :param index: Element index if more than one <Course Card>
        """
        self.click_course_menu_btn(index)
        expect(self.course_edit_memu_button.nth(index)).to_be_enabled()
        self.course_edit_memu_button.nth(index).click()


    def click_delete_course_btn(self, index: int = 0):
        """
        Click <Delete course> button

        - ▶ <Course menu> button - Click (func)
        - ✔ <Delete course> button - enabled
        - ▶ <Delete course> button - Click

        :param index: Element index if more than one <Course Card>
        """
        self.click_course_menu_btn(index)
        expect(self.course_edit_memu_button.nth(index)).to_be_enabled()
        self.course_edit_memu_button.nth(index).click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar:
    def check_toolbar_title(self):
        """
        Check <Toolbar title> of the Courses List page

        - ✔ Title - visible
        - ✔ Title text - correct
        """
        error_visible = '❌ <Toolbar title> of the Courses List page - invisible!'
        error_text = '❌ <Toolbar title> text of the Courses List page - incorrect!'
        expect(self.toolbar_title, error_visible).to_be_visible()
        expect(self.toolbar_title, error_text).to_have_text('Courses')


    # Empty view:
    def check_empty_view(self):
        """
        Check <Empty View> of the Courses List page

        - ✔ Icon - visible
        - ✔ Title - visible | text - correct
        - ✔ Description - visible | text - correct
        """
        error_icon_visible = '❌ <Empty view icon> of the Courses List page - invisible!'
        error_title_visible = '❌ <Empty view title> of the Courses List page - invisible!'
        error_description_visible = '❌ <Empty view description> of the Courses List page - invisible!'
        error_title_text = '❌ <Empty view title> text of the Courses List page - incorrect!'
        error_description_text = '❌ <Empty view description> text of the Courses List page - incorrect!'
        expect(self.empty_view_icon, error_icon_visible).to_be_visible()
        expect(self.empty_view_title, error_title_visible).to_be_visible()
        expect(self.empty_view_description, error_description_visible).to_be_visible()
        expect(self.empty_view_title, error_title_text).to_have_text('There is no results')
        expect(self.empty_view_description, error_description_text).to_have_text('Results from the load test pipeline will be displayed here')

    # Course Card:
    def check_course_card(
            self,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str,
            index: int = 0       # Element index if more than one <Course Card>
    ):
        """
        Check <Course Card> of the Courses List page

        - ✔ Image - visible
        - ✔ Title - visible | text - correct
        - ✔ Max score - visible | text - correct
        - ✔ Min score - visible | text - correct
        - ✔ Estimated time - visible | text - correct

        :param title: Course title
        :param max_score: Max score
        :param min_score: Min score
        :param estimated_time: Estimated time
        :param index: Element index if more than one <Course Card>
        """
        error_image_visible = '❌ <Course image> of the Course card - invisible!'
        error_title_visible = '❌ <Course title> of the Course card - invisible!'
        error_title_text = '❌ <Course title> text of the Course card - incorrect!'
        error_max_score_visible = '❌ <Max score> of the Course card - invisible!'
        error_max_score_text = '❌ <Max score> text of the Course card - incorrect!'
        error_min_score_visible = '❌ <Min score> of the Course card - invisible!'
        error_min_score_text = '❌ <Min score> text of the Course card - incorrect!'
        error_estimated_time_visible = '❌ <Estimated time> of the Course card - invisible!'
        error_estimated_time_text = '❌ <Estimated time> text of the Course card - incorrect!'
        expect(self.course_image.nth(index), error_image_visible).to_be_visible()
        expect(self.course_title.nth(index), error_title_visible).to_be_visible()
        expect(self.course_title.nth(index), error_title_text).to_have_text(title)
        expect(self.course_max_score.nth(index), error_max_score_visible).to_be_visible()
        expect(self.course_max_score.nth(index), error_max_score_text).to_have_text(f'Max score: {max_score}')
        expect(self.course_min_score.nth(index), error_min_score_visible).to_be_visible()
        expect(self.course_min_score.nth(index), error_min_score_text).to_have_text(f'Min score: {min_score}')
        expect(self.course_estimated_time.nth(index), error_estimated_time_visible).to_be_visible()
        expect(self.course_estimated_time.nth(index), error_estimated_time_text).to_have_text(f'Estimated time: {estimated_time}')
