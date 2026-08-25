"""
Empty view (component)
"""
import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

#=======================================================================================================================
"""
[Empty view]:
- Icon
- Title
- Description
"""
class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, component: str):
        """
        :param page: Page
        :param identifier: Unique part of locator (courses-list | create-course-preview | create-course-exercises)
        :param component: Component navigate-path
        """
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.identifier = identifier.capitalize()     # for logging

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.empty_view_component = f'❌ {component} > {self.identifier} > Empty view'
        self.icon_element = f'{self.empty_view_component} > [Icon]'
        self.title_element = f'{self.empty_view_component} > [Title]'
        self.description_element = f'{self.empty_view_component} > [Description]'

        # ---------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
        self.icon = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description = page.get_by_test_id(f'{identifier}-empty-view-description-text')

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Empty view]
    # ─────────────────────────────────────┐
    @allure.step('✔ Check [Empty view]')
    def check(self, title: str, description: str):
        """
        ✔ Check [Empty view]

        - ✔ Icon - visible
        - ✔ Title - visible | - text
        - ✔ Description - visible | - text

        :param title: Title text
        :param description: Description text
        """
        self.check_icon_visible()
        self.check_title(title)
        self.check_description(description)
    # ─────────────────────────────────────┘

    # [Icon]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Icon]')
    def check_icon(self):
        """
        ✔ Check [Icon]

        - ✔ Icon - visible
        """
        self.check_icon_visible()
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Icon] is visible')
    def check_icon_visible(self):
        """
        ✔ Check [Icon]  is visible

        .
        """
        error = f'{self.icon_element} - invisible!'
        expect(self.icon, error).to_be_visible()


    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_title(self, title: str):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param title: Title
        """
        self.check_title_visible()
        self.check_title_text(title)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Title] is visible')
    def check_title_visible(self):
        """
        ✔ Check [Title]  is visible

        .
        """
        error = f'{self.title_element} - invisible!'
        expect(self.title, error).to_be_visible()

    @allure.step('✔ Check [Title] text')
    def check_title_text(self, title: str):
        """
        ✔ Check [Title] text

        :param title: Title text
        """
        error = f'{self.title_element} - incorrect text!'
        expect(self.title, error).to_have_text(title)


    # [Description]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Description]')
    def check_description(self, description: str):
        """
        ✔ Check [Description]

        - ✔ Description - visible
        - ✔ Description - text

        :param description: Description text
        """
        self.check_description_visible()
        self.check_description_text(description)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check [Description] is visible')
    def check_description_visible(self):
        """
        ✔ Check [Description]  is visible

        .
        """
        error = f'{self.description_element} - invisible!'
        expect(self.description, error).to_be_visible()

    @allure.step('✔ Check [Description] text')
    def check_description_text(self, description: str):
        """
        ✔ Check [Description] text

        :param description: Description
        """
        error = f'{self.description_element} - incorrect text!'
        expect(self.description, error).to_have_text(description)

#=======================================================================================================================
