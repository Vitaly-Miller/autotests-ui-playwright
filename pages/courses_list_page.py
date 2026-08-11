"""
Courses List page
"""

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.emty_view_component import EmptyViewComponent
from components.courses.course_view_component import CourseViewComponent
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
        self.course_view = CourseViewComponent(page)

        # ------------------------------------------ ㉧ LOCATORS (static) -----------------------------------------------
        # Toolbar
        self.toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.toolbar_create_course_btn = page.get_by_test_id('courses-list-toolbar-create-course-button')

        # Empty view (component)
        # See —> /components/views/empty_view_component.py

        # Course View (component)
        # See — > /components/courses/course_view_component.py


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_toolbar_create_course_btn(self):
        """
        Click <Toolbar [Create course] button>  of the Courses List page

        - ✔ Button - visible
        - ▶ Button - click
        """
        self.check_toolbar_create_course_btn_visible()
        self.toolbar_create_course_btn.click()



    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ════════════════════════════╗
    def check_empty_page(self):
        """
        Check ALL Elements of the Courses List Empty page (EMPTY)

        (NO Course Cards)

        - ✔ Toolbar
        - ✔ Empty View
        """
        self.check_toolbar()
        self.check_empty_view()
    # ════════════════════════════╝

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


    # COMPONENTS
    # Navbar + Sidebar (components)
    def check_navbar_and_sidebar(self, username: str):
        """
        Check <Navbar> + <Sidebar> components

        - ✔ Navbar - visible | Text - correct
        - ✔ Sidebar - Buttons - visible | Icons - visible | Text - correct
        """
        self.navbar.check_component(username)
        self.sidebar.check_component()


    # Empty View (component):
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


    # Course View (component)
    def check_course_view(
        self,
        index: int,
        title: str,
        max_score: str,
        min_score: str,
        estimated_time: str
    ):
        """
        Check ALL Elements of the <Course View> component of the Courses List page

        - ✔ Menu (component)
        - ✔ Image - visible
        - ✔ Title - visible | Text - correct
        - ✔ Max score - visible | Text - correct
        - ✔ Min score - visible | Text - correct
        - ✔ Estimated time - visible | Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param title: Course title
        :param max_score: Course Max score
        :param min_score: Course Min score
        :param estimated_time: Course estimated time
        """
        self.course_view.check_component(
            index=index,
            title=title,
            max_score=max_score,
            min_score=min_score,
            estimated_time=estimated_time
        )

#=======================================================================================================================
