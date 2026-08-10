"""
Courses List page
"""

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.emty_view_component import EmptyViewComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
class CoursesListPage(BasePage):       # Дочерний класс (наследует класс BasePage)
    URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

    def __init__(self, page: Page):     # Конструктор класса, принимающий Page
        super().__init__(page)          # Передаёт page в конструктор BasePage

        # -------------------------------------------------- 𝌆 DATA ---------------------------------------------------
        self.IDENTIFIER = 'courses-list'
        self.EMPTY_VIEW_TITLE = 'There is no results'
        self.EMPTY_VIEW_DESCRIPTION = 'Results from the load test pipeline will be displayed here'

        # ----------------------------------------------- ⿴ COMPONENTS ------------------------------------------------
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page=page, identifier=self.IDENTIFIER)

        # ------------------------------------------ ㉧ LOCATORS (static) -----------------------------------------------
        # Toolbar
        self.toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.toolbar_create_course_btn = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # Empty view (component)
        # See —> /components/views/empty_view_component.py

        # Course View (component)
        # See — > /components/courses/course_view_component.py
        # self.course_title = page.get_by_test_id('course-widget-title-text')
        # self.course_image = page.get_by_test_id('course-preview-image')
        # self.course_max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        # self.course_min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        # self.course_estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')
        # See —> /components/courses/course_view_menu_component.py
        # self.course_menu_btn = page.get_by_test_id('course-view-menu-button')
        # self.course_edit_menu_btn = page.get_by_test_id('course-view-edit-menu-item')
        # self.course_delete_menu_btn = page.get_by_test_id('course-view-delete-menu-item')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_toolbar_create_course_btn(self):
        """
        Click <Toolbar [Create course] button>  of the Courses List page

        - ✔ Button - visible
        - ▶ Button - click
        """
        self.check_toolbar_create_course_btn_visible()
        self.toolbar_create_course_btn.click()

    # def click_course_card_menu_btn(self, index: int):
    #     """
    #     Click <Course card [Menu] button>
    #
    #     - ✔ Button - visible
    #     - ▶ Button - click
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     self.check_course_card_menu_btn_visible(index)
    #     self.course_menu_btn.nth(index).click()
    #
    #
    # def click_course_card_menu_edit_course_btn(self, index: int):
    #     """
    #     Click <Course card menu [Edit course] button>  of the Courses List page
    #
    #     - ▶ <Course card menu> button - click
    #     - ✔ <Edit course> button - enabled
    #     - ▶ <Edit course> button - click
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     self.click_course_card_menu_btn(index)
    #     self.check_course_card_menu_edit_course_btn_visible(index)
    #     self.course_edit_menu_btn.nth(index).click()
    #
    # def click_course_card_menu_delete_course_btn(self, index: int):
    #     """
    #     Click <Course card menu [Delete course] button> of the Courses List page
    #
    #     - ▶ <Course card menu> button - click
    #     - ✔ <Delete course> button - enabled
    #     - ▶ <Delete course> button - click
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     self.click_course_card_menu_btn(index)
    #     self.check_course_card_menu_delete_course_btn_visible(index)
    #     self.course_delete_menu_btn.nth(index).click()
    #

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ALL Elements (NO Course Cards)
    # ════════════════════════════╗
    def check_all_elements(self):
        """
        Check ALL Elements of the Courses List page

        (NO Course Cards)

        - ✔ Toolbar
        - ✔ Empty View
        """
        self.check_toolbar()
        self.check_empty_view()
    # ════════════════════════════╝

    # Navbar + Sidebar (components)
    # ────────────────────────────────────────────────┐
    def check_navbar_and_sidebar(self, username: str):
        """
        Check <Navbar> + <Sidebar> components

        - ✔ Navbar - visible | Text - correct
        - ✔ Sidebar - Buttons - visible | Icons - visible | Text - correct
        """
        self.navbar.check_navbar(username)
        self.sidebar.check_sidebar()
    # ────────────────────────────────────────────────┘

    # Toolbar:
    # ────────────────────────────────────────────────┐
    def check_toolbar(self):
        """
        Check <Toolbar> of the Courses List page

        - ✔ Title - visible
        - ✔ Title text - correct
        - ✔ <Create course> button - visible
        """
        self.check_toolbar_title_visible()
        self.check_toolbar_create_course_btn_visible()
        self.check_toolbar_title_text()
    # ────────────────────────────────────────────────┘
    def check_toolbar_title_visible(self):
        """
        Check <Toolbar [Title]> visible of the Courses List page

        - ✔ Title - visible
        """
        error = f'❌ <Toolbar [Title]> of the Courses List page - invisible!'
        expect(self.toolbar_title, error).to_be_visible()

    def check_toolbar_title_text(self):
        """
        Check <Toolbar [Title] text> of the Courses List page

        - ✔ Text - correct
        """
        error = f'❌ <Toolbar [Title] text> of the Courses List page - incorrect!'
        expect(self.toolbar_title, error).to_have_text('Courses')

    def check_toolbar_create_course_btn_visible(self):
        """
        Check <Toolbar [Create course] button> of the Courses List page

        - ✔ Button - visible
        """
        error = f'❌ <Toolbar [Create course] button> of the Courses List page - invisible!'
        expect(self.toolbar_create_course_btn, error).to_be_visible()


    # Empty View (component):
    # ─────────────────────────────────────────────┐
    def check_empty_view(self):
        """
        Check ALL elements of the <Empty View> component of the Courses List page

        - ✔ Icon - visible
        - ✔ Title - visible | Text - correct
        - ✔ Description - visible | Text - correct
        """
        self.empty_view.check_component(
            title=self.EMPTY_VIEW_TITLE,
            description=self.EMPTY_VIEW_DESCRIPTION)
    # ──────────────────────────────────────────────┘

    # Course Card: (by DOM-index)
    # ─────────────────────────────────────────────────────────────────────────────────────────┐
    def check_course_card(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str):
        """
        Check <Course card> of the Courses List page

        - ✔ Image - visible
        - ✔ Title - visible | Text - correct
        - ✔ Max score - visible | Text - correct
        - ✔ Min score - visible | Text - correct
        - ✔ Estimated time - visible | Text - correct
        - ✔ Menu button - visible

        :param index: Element DOM-index of <Course Card>
        :param title: Course title
        :param max_score: Max score
        :param min_score: Min score
        :param estimated_time: Estimated time
        """
        self.check_course_card_image_visible(index)
        self.check_course_card_title_visible(index)
        self.check_course_card_title_text(title=title, index=index)
        self.check_course_card_max_score_visible(index)
        self.check_course_card_max_score_text(max_score=max_score, index=index)
        self.check_course_card_min_score_visible(index)
        self.check_course_card_min_score_text(min_score=min_score, index=index)
        self.check_course_card_estimated_time_visible(index)
        self.check_course_card_estimated_time_text(estimated_time=estimated_time, index=index)
        self.check_course_card_menu_btn_visible(index=index)
    # ─────────────────────────────────────────────────────────────────────────────────────────┘
    # # Course Card [Image]:
    # def check_course_card_image_visible(self, index: int):
    #     """
    #     Check <Course card [Image]> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Image]> Courses List page - invisible!'
    #     expect(self.course_image.nth(index), error).to_be_visible()
    #
    #
    # # Course Card [Title]
    # def check_course_card_title_visible(self, index: int):
    #     """
    #     Check <Course card [Title]> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Title]> of the Courses List page - invisible!'
    #     expect(self.course_title.nth(index), error).to_be_visible()
    #
    # def check_course_card_title_text(self, title: str, index: int):
    #     """
    #     Check <Course card [Title] text> of the Courses List page - correct
    #
    #     :param title: Course title
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Title] text> of the Courses List page - incorrect!'
    #     expect(self.course_title.nth(index), error).to_have_text(title)
    #
    # # Course Card [Max score]
    # def check_course_card_max_score_visible(self, index: int):
    #     """
    #     Check <Course card [Max score]> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Max score]> of the Courses List page - invisible!'
    #     expect(self.course_max_score.nth(index), error).to_be_visible()
    #
    # def check_course_card_max_score_text(self, max_score: str, index: int):
    #     """
    #     Check <Course card [Max score] text> of the Courses List page - correct
    #
    #     :param max_score: Max score
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Max score] text> of the Courses List page - incorrect!'
    #     expect(self.course_max_score.nth(index), error).to_have_text(f'Max score: {max_score}')
    #
    # # Course Card [Min score]
    # def check_course_card_min_score_visible(self, index: int):
    #     """
    #     Check <Course card [Min score]> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Min score]> of the Courses List page - invisible!'
    #     expect(self.course_min_score.nth(index), error).to_be_visible()
    #
    # def check_course_card_min_score_text(self, min_score: str, index: int):
    #     """
    #     Check <Course card [Min score] text> of the Courses List page - correct
    #
    #     :param min_score: Min score
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Min score] text> of the Courses List page - incorrect!'
    #     expect(self.course_min_score.nth(index), error).to_have_text(f'Min score: {min_score}')
    #
    # # Course Card [Estimated time]
    # def check_course_card_estimated_time_visible(self, index: int):
    #     """
    #     Check <Course card [Estimated time]> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Estimated time]> of the Courses List page - invisible!'
    #     expect(self.course_estimated_time.nth(index), error).to_be_visible()
    #
    # def check_course_card_estimated_time_text(self, estimated_time: str, index: int):
    #     """
    #     Check <Course card [Estimated time] text> of the Courses List page - correct
    #
    #     :param estimated_time: Estimated time
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Estimated time] text> of the Courses List page - incorrect!'
    #     expect(self.course_estimated_time.nth(index), error).to_have_text(f'Estimated time: {estimated_time}')


    # # Course View [Menu] button
    # def check_course_card_menu_btn_visible(self, index: int):
    #     """
    #     Check <Course card [Menu] button> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card [Menu button]> of the Courses List page - invisible!'
    #     expect(self.course_menu_btn.nth(index), error).to_be_visible()
    #
    # # Course Card Menu [Edit course button]
    # def check_course_card_menu_edit_course_btn_visible(self, index: int):
    #     """
    #     Check <Course card Menu [Edit course] button> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card Menu [Edit course] button> of the Courses List page - invisible!'
    #     expect(self.course_edit_menu_btn.nth(index), error).to_be_visible()
    #
    # def check_course_card_menu_edit_course_btn_text(self, index: int):
    #     """
    #     Check <Course card Menu [Edit course] button text> of the Courses List page - correct
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card Menu [Edit course] button text> of the Courses List page - incorrect!'
    #     expect(self.course_edit_menu_btn.nth(index), error).to_have_text('Edit')
    #
    # # Course Card Menu [Delete course button]
    # def check_course_card_menu_delete_course_btn_visible(self, index: int):
    #     """
    #     Check <Course card Menu [Delete course] button> of the Courses List page - visible
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card Menu [Delete course] button> of the Courses List page - invisible!'
    #     expect(self.course_delete_menu_btn.nth(index), error).to_be_visible()
    #
    # def check_course_card_menu_delete_course_btn_text(self, index: int):
    #     """
    #     Check <Course card Menu [Delete course] button text> of the Courses List page - correct
    #
    #     :param index: Element DOM-index if more than one <Course Card>
    #     """
    #     error = f'❌ <Course card Menu [Delete course] button text> of the Courses List page - incorrect!'
    #     expect(self.course_delete_menu_btn.nth(index), error).to_have_text('Delete')
    #

#=======================================================================================================================
