"""
Courses card (component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page
from components.courses.courses_list.course_card_menu_component import CourseCardMenuComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text

#=======================================================================================================================
class CourseCardComponent(BaseComponent):
    """
    Courses card (component)

    - Menu button (component)
    - Title
    - Image
    - Max score
    - Min score
    - Estimated time
    """
    PATH = 'Courses list page > Course card'

    def __init__(self, page: Page):
        super().__init__(page)

        # ⿳ COMPONENTS
        self.menu = CourseCardMenuComponent(page)

    # -------------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
    def title_locator(self) -> Locator:
        return self.page.get_by_test_id('course-widget-title-text')

    def menu_btn_locator(self) -> Locator:
        return self.page.get_by_test_id('course-view-menu-button')

    def image_locator(self) -> Locator:
        return self.page.get_by_test_id('course-preview-image')

    def max_score_locator(self) -> Locator:
        return self.page.get_by_test_id('course-max-score-info-row-view-text')

    def min_score_locator(self) -> Locator:
        return self.page.get_by_test_id('course-min-score-info-row-view-text')

    def estimated_time_locator(self) -> Locator:
        return self.page.get_by_test_id('course-estimated-time-info-row-view-text')

    # -------------------------------------------------- ◈ ELEMENTS -----------------------------------------------------
    def title(self) -> Text:
        return Text(self.title_locator(), self.PATH, 'Title')

    def menu_btn(self) -> Button:
        return Button(self.menu_btn_locator(), self.PATH, 'Menu button')

    def image(self) -> Image:
        return Image(self.image_locator(), self.PATH, 'Image')

    def max_score(self) -> Text:
        return Text(self.max_score_locator(), self.PATH, 'Max score')

    def min_score(self) -> Text:
        return Text(self.min_score_locator(), self.PATH, 'Min score')

    def estimated_time(self) -> Text:
        return Text(self.estimated_time_locator(), self.PATH, 'Estimated time')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Menu button]
    @allure.step('▶ Click [Menu button]')
    def click_menu_btn(self, nth_index: int = 0):
        """
        ▶ Click [Menu button]

        :param nth_index: nth-index —> for use in: locator.nth(nth_index)
        """
        self.menu_btn().click(nth_index)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Course card]
    # ───────────────────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [{title} - course card]')
    def check(
        self,
        title: str,
        max_score: str,
        min_score: str,
        estimated_time: str,
        nth_index: int = 0
    ):
        """
        ✔ Check [Course card]

        - ✔ Menu button
        - ✔ Image
        - ✔ Title
        - ✔ Max score
        - ✔ Min score
        - ✔ Estimated time

        :param title: Course title
        :param max_score: Max score
        :param min_score: Min score
        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_menu_btn(nth_index)
        self.check_image(nth_index)
        self.check_title(title,nth_index )
        self.check_max_score(max_score,nth_index)
        self.check_min_score(min_score,nth_index)
        self.check_estimated_time(estimated_time,nth_index)
    # ────────────────────────────────────────────────────────────────────────────┘

    # [Title]
    @allure.step('✔ Check [Title]')
    def check_title(self, title: str, nth_index: int = 0):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param title: Course title
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.title().check_visible(nth_index)
        self.title().check_text(title, nth_index)

    # [Menu button]
    @allure.step('✔ Check [Menu button]')
    def check_menu_btn(self, nth_index: int = 0):
        """
        ✔ Check [Menu button]

        - ✔ Button - visible
        - ✔ Button - enabled

        :param nth_index: nth-index —> for use in: locator.nth(nth_index)
        """
        self.menu_btn().check_visible(nth_index)
        self.menu_btn().check_enabled(nth_index)

    # [Image]
    @allure.step('✔ Check [Image]')
    def check_image(self, nth_index: int = 0):
        """
        ✔ Check [Image]

        - ✔ Image - visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.image().check_visible(nth_index)


    # [Max score]
    @allure.step('✔ Check [Max score]')
    def check_max_score(self, max_score: str, nth_index: int = 0):
        """
        ✔ Check [Max score]

        - ✔ Max score - visible
        - ✔ Max score - text

        :param max_score: Max score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.max_score().check_visible(nth_index)
        self.max_score().check_text(text=f'Max score: {max_score}', nth=nth_index)


    # [Min score]
    @allure.step('✔ Check [Min score]')
    def check_min_score(self, min_score: str, nth_index: int = 0):
        """
        ✔ Check [Min score]

        - ✔ Min score - visible
        - ✔ Min score - text

        :param min_score: Min score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.min_score().check_visible(nth_index)
        self.min_score().check_text(text=f'Min score: {min_score}', nth=nth_index)


    # [Estimated time]
    @allure.step('✔ Check [Estimated time]')
    def check_estimated_time(self, estimated_time: str, nth_index: int = 0):
        """
        ✔ Check [Estimated time]

        - ✔ Estimated time - visible
        - ✔ Estimated time - text

        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.estimated_time().check_visible(nth_index)
        self.estimated_time().check_text(text=f'Estimated time: {estimated_time}', nth=nth_index)

#=======================================================================================================================
