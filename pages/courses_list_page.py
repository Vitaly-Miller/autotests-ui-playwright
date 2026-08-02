"""
Courses List page
"""
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

#=======================================================================================================================
class CoursesListPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # ┌╴ ㉧ LOCATORS (static):
        # ├ Toolbar
        self.toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.toolbar_create_course_btn = page.get_by_test_id('courses-list-toolbar-create-course-button')
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
        self.course_menu_btn = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_btn = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_btn = page.get_by_test_id('course-view-delete-menu-item')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_toolbar_create_course_btn(self):
        """
        Click <Toolbar Create course> button of the Courses List page

        - ✔ Button - visible
        - ▶ Button - Click
        """
        self.check_courses_toolbar_create_course_btn_visible()
        self.toolbar_create_course_btn.click()


    def click_course_card_menu_btn(self, index: int = 0):
        """
        Click <Course card menu> button

        - ✔ Object - enabled
        - ▶ Button - Click

        :param index: Element DOM-index if more than one <Course Card>
        """
        self.check_course_card_menu_btn_visible()
        self.course_menu_btn.nth(index).click()


    def click_course_card_menu_edit_course_btn(self, index: int = 0):
        """
        Click <Course card menu Edit course> button of the Courses List page

        - ▶ <Course card menu> button - Click
        - ✔ <Edit course> button - enabled
        - ▶ <Edit course> button - Click

        :param index: Element DOM-index if more than one <Course Card>
        """
        self.click_course_card_menu_btn(index)
        self.check_course_card_menu_edit_course_btn_visible(index)
        self.course_edit_menu_btn.nth(index).click()

    def click_course_card_menu_delete_course_btn(self, index: int = 0):
        """
        Click <Course card menu Delete course> button of the Courses List page

        - ▶ <Course card menu> button - Click
        - ✔ <Delete course> button - enabled
        - ▶ <Delete course> button - Click

        :param index: Element DOM-index if more than one <Course Card>
        """
        self.click_course_card_menu_btn(index)
        self.check_course_card_menu_delete_course_btn_visible(index)
        self.course_delete_menu_btn.nth(index).click()


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # Toolbar:
    # --------------------- Check Suite --------------------
    def check_courses_toolbar(self):
        """
        Check <Toolbar> of the Courses List page (Suite 3-in-1)

        .
        """
        self.check_courses_toolbar_title_visible()
        self.check_courses_toolbar_create_course_btn_visible()
        self.check_courses_toolbar_title_text()

    # ------------------------------------------------------
    def check_courses_toolbar_title_visible(self):
        """
        Check <Toolbar title> visible of the Courses List page

        - ✔ Title - visible
        """
        error = '❌ <Toolbar title> of the Courses List page - invisible!'
        expect(self.toolbar_title, error).to_be_visible()

    def check_courses_toolbar_title_text(self, text: str = 'Courses'):
        """
        Check <Toolbar title> text of the Courses List page

        - ✔ Text - correct

        :param text: "Courses" (default)
        """
        error = '❌ <Toolbar title> text of the Courses List page - incorrect!'
        expect(self.toolbar_title, error).to_have_text(text)

    def check_courses_toolbar_create_course_btn_visible(self):
        """
        Check <Toolbar Create course> button of the Courses List page

        - ✔ Button - visible
        """
        error = '❌ <Toolbar Create course> of the Courses List page - invisible!'
        expect(self.toolbar_create_course_btn, error).to_be_visible()



    # Empty view:
    # --------------------- Check Suite --------------------
    def check_courses_empty_view(self):
        """
        Check <Courses Empty View> of the Courses List page (Suite 5-in-1)

        (without created Course cards)
        """
        self.check_courses_empty_view_icon_visible()
        self.check_courses_empty_view_title_visible()
        self.check_courses_empty_view_description_visible()
        self.check_courses_empty_view_title_text()
        self.check_courses_empty_view_description_text()

    # ------------------------------------------------------
    def check_courses_empty_view_icon_visible(self):
        """
        Check <Empty View icon> of the Course List page - visible

        - ✔ Icon - visible
        """
        error = '❌ <Empty view icon> of the Courses List page - invisible!'
        expect(self.empty_view_icon, error).to_be_visible()

    def check_courses_empty_view_title_visible(self):
        """
        Check <Empty View title> of the Course List page - visible

        - ✔ Title - visible

        """
        error = '❌ <Empty View title> of the Courses List page - invisible!'
        expect(self.empty_view_title, error).to_be_visible()

    def check_courses_empty_view_description_visible(self):
        """
        Check <Empty View description> of the Course List page - visible

        - ✔ Description - visible
        """
        error = '❌ <Empty View description> of the Courses List page - invisible!'
        expect(self.empty_view_description, error).to_be_visible()

    def check_courses_empty_view_title_text(self, title: str = 'There is no results'):
        """
        Check <Empty View title> text of the Course List page - correct

        - ✔ Text - correct
        """
        error = '❌ <Empty View title> text of the Courses List page - incorrect!'
        expect(self.empty_view_title, error).to_have_text(title)

    def check_courses_empty_view_description_text(self, text: str = 'Results from the load test pipeline will be displayed here'):
        """
        Check <Empty View description> text of the Course List page - correct

        - ✔ Text - correct
        """
        error = '❌ <Empty View description> text of the Courses List page - incorrect!'
        expect(self.empty_view_description, error).to_have_text(text)



    # Course Card:
    # ------------------------ Check Suite ------------------
    def check_course_card(
            self,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str,
            index: int = 0):
        """
        Check <Curse card> of the Courses List page (Suite 10-in-1)

        :param title: Course title
        :param max_score: Max score
        :param min_score: Min score
        :param estimated_time: Estimated time
        :param index: Element DOM-index if more than one <Course Card>
        """
        self.check_course_card_image_visible(index)
        self.check_course_card_title_visible()
        self.check_course_card_title_text(title=title, index=index)
        self.check_course_card_max_score_visible()
        self.check_course_card_max_score_text(max_score=max_score, index=index)
        self.check_course_card_min_score_visible()
        self.check_course_card_min_score_text(min_score=min_score, index=index)
        self.check_course_card_estimated_time_visible(index)
        self.check_course_card_estimated_time_text(estimated_time=estimated_time, index=index)
        self.check_course_card_menu_btn_visible(index=index)

    # --------------------------------------------------------
    def check_course_card_image_visible(self, index: int = 0):
        """
        Check <Course card image> of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card image> Courses List page - invisible!'
        expect(self.course_image.nth(index), error).to_be_visible()


    def check_course_card_title_visible(self, index: int = 0):
        """
        Check <Course card title> of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card title> of the Courses List page - invisible!'
        expect(self.course_title.nth(index), error).to_be_visible()

    def check_course_card_title_text(self, title: str, index: int = 0):
        """
        Check <Course card title> text of the Courses List page - correct

        :param title: Course title
        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card title> text of the Course List page - incorrect!'
        expect(self.course_title.nth(index), error).to_have_text(title)


    def check_course_card_max_score_visible(self, index: int = 0):
        """
        Check <Course card Max score> of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card Max score> of the Course List page - invisible!'
        expect(self.course_max_score.nth(index), error).to_be_visible()

    def check_course_card_max_score_text(self, max_score: str, index: int = 0):
        """
        Check <Course card Max score> text of the Courses List page - correct

        :param max_score: Max score
        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card Max score> text of the Course List page - incorrect!'
        expect(self.course_max_score.nth(index), error).to_have_text(f'Max score: {max_score}')


    def check_course_card_min_score_visible(self, index: int = 0):
        """
        Check <Course card Min score> of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card Min score> of the Course List page - invisible!'
        expect(self.course_min_score.nth(index), error).to_be_visible()

    def check_course_card_min_score_text(self, min_score: str, index: int = 0):
        """
        Check <Course card Min score> text of the Courses List page - correct

        :param min_score: Min score
        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card Min score> text of the Course List page - incorrect!'
        expect(self.course_min_score.nth(index), error).to_have_text(f'Min score: {min_score}')


    def check_course_card_estimated_time_visible(self, index: int = 0):
        """
        Check <Course card Estimated time> of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card Estimated time> of the Course List page - invisible!'
        expect(self.course_estimated_time.nth(index), error).to_be_visible()

    def check_course_card_estimated_time_text(self, estimated_time: str, index: int = 0):
        """
        Check <Course card Estimated time> text of the Courses List page - correct

        :param estimated_time: Estimated time
        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card Estimated time> text of the Course List page - incorrect!'
        expect(self.course_estimated_time.nth(index), error).to_have_text(f'Estimated time: {estimated_time}')


    # Course Card buttons:
    def check_course_card_menu_btn_visible(self, index: int = 0):
        """
        Check <Course card menu> button of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card menu> button of the Courses List page - invisible!'
        expect(self.course_menu_btn.nth(index), error).to_be_visible()

    def check_course_card_menu_edit_course_btn_visible(self, index: int = 0):
        """
        Check <Course card menu Edit course> button of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card menu Edit course> button of the Courses List page - invisible!'
        expect(self.course_edit_menu_btn.nth(index), error).to_be_visible()

    def check_course_card_menu_delete_course_btn_visible(self, index: int = 0):
        """
        Check <Course card menu Delete course> button of the Courses List page - visible

        :param index: Element DOM-index if more than one <Course Card>
        """
        error = '❌ <Course card menu Delete course> button of the Courses List page - invisible!'
        expect(self.course_delete_menu_btn.nth(index), error).to_be_visible()
