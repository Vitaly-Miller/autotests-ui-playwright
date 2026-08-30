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

        # ------------------------------------ Elements (path & name) (for debug) --------------------------------------
        self.empty_view_component = f'❌ {component} > {self.identifier} > Empty view'
        self.icon_element = f'{self.empty_view_component} > [Icon]'
        self.title_element = f'{self.empty_view_component} > [Title]'
        self.description_element = f'{self.empty_view_component} > [Description]'

        # ---------------------------------------------- ㉧ LOCATORS ---------------------------------------------------
        self.icon_locator = page.get_by_test_id(f'{identifier}-empty-view-icon')
        self.title_locator = page.get_by_test_id(f'{identifier}-empty-view-title-text')
        self.description_locator = page.get_by_test_id(f'{identifier}-empty-view-description-text')

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
    @allure.step('✔ Check visible [Icon]')
    def check_icon_visible(self):
        """
        ✔ Check visible [Icon]

        .
        """
        error = f'{self.icon_element} - invisible!'
        expect(self.icon_locator, error).to_be_visible()


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
    @allure.step('✔ Check visible [Title]')
    def check_title_visible(self):
        """
        ✔ Check visible [Title]

        .
        """
        error = f'{self.title_element} - invisible!'
        expect(self.title_locator, error).to_be_visible()

    @allure.step('✔ Check text of [Title]')
    def check_title_text(self, title: str):
        """
        ✔ Check text of [Title]

        :param title: Title text
        """
        error = f'{self.title_element} - incorrect text!'
        expect(self.title_locator, error).to_have_text(title)


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
    @allure.step('✔ Check visible [Description]')
    def check_description_visible(self):
        """
        ✔ Check visible [Description]

        .
        """
        error = f'{self.description_element} - invisible!'
        expect(self.description_locator, error).to_be_visible()

    @allure.step('✔ Check text of [Description]')
    def check_description_text(self, description: str):
        """
        ✔ Check text of [Description]

        :param description: Description
        """
        error = f'{self.description_element} - incorrect text!'
        expect(self.description_locator, error).to_have_text(description)

#=======================================================================================================================
