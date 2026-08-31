"""
Courses list page > [Course card]
(Page component)
"""

import allure
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page
from components.courses.courses_list.course_card_menu_component import CourseCardMenuComponent
from elements.button import Button
from elements.image import Image
from elements.text import Text

#=======================================================================================================================
"""
[Course card]:
- Menu button (component)
- Title
- Image
- Max score
- Min score
- Estimated time
"""
class CourseCardComponent(BaseComponent):
    path = 'Courses list page > Course card'

    # 𝌆 DATA
    @staticmethod
    def max_score_text(max_score: str) -> str:
        return f'Max score: {max_score}'

    @staticmethod
    def min_score_text(min_score: str) -> str:
        return f'Min score: {min_score}'

    @staticmethod
    def estimated_time_text(estimated_time: str) -> str:
        return f'Estimated time: {estimated_time}'

    def __init__(self, page: Page):
        super().__init__(page)

        # --------------------------------------------- ⿳ COMPONENTS --------------------------------------------------
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
        return Text(self.title_locator(), self.path, 'Title')

    def menu_btn(self) -> Button:
        return Button(self.menu_btn_locator(), self.path, 'Menu button')

    def image(self) -> Image:
        return Image(self.image_locator(), self.path, 'Image')

    def max_score(self) -> Text:
        return Text(self.max_score_locator(), self.path, 'Max score')

    def min_score(self) -> Text:
        return Text(self.min_score_locator(), self.path, 'Min score')

    def estimated_time(self) -> Text:
        return Text(self.estimated_time_locator(), self.path, 'Estimated time')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Menu button]
    @allure.step('▶ Click [Menu button]')
    def click_menu_btn(self, nth_index: int = 0):
        """
        ▶ Click [Menu button]

        :param nth_index: nth-index —> for use in: locator.nth(nth_index)
        """
        self.menu_btn().click(nth=nth_index)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Course card]
    # ──────────────────────────────────────────────────────────────────────────────┐
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

        - ✔ Menu button - visible | - enabled
        - ✔ Image - visible
        - ✔ Title - visible | - text
        - ✔ Max score - visible | - text
        - ✔ Min score - visible | - text
        - ✔ Estimated time - visible | - text

        :param title: Course title
        :param max_score: Max score
        :param min_score: Min score
        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_menu_btn(nth_index)
        self.check_image(nth_index)
        self.check_title(nth_index=nth_index, title=title)
        self.check_max_score(nth_index=nth_index, max_score=max_score)
        self.check_min_score(nth_index=nth_index, min_score=min_score)
        self.check_estimated_time(nth_index=nth_index, estimated_time=estimated_time)
    # ───────────────────────────────────────────────────────────────────────────────┘

    # [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Title]')
    def check_title(self, title: str, nth_index: int = 0):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param title: Course title
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_title_visible(nth_index)
        self.check_title_text(title=title, nth_index=nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_title_visible(self, nth_index: int = 0):
        """
        ✔ Check [Title] is visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.title().check_visible(nth=nth_index)

    # Text
    def check_title_text(self, title: str, nth_index: int = 0):
        """
        ✔ Check [Title] text

        :param title: Course title
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.title().check_text(title, nth=nth_index)


    # [Menu button]
    # ────────────────────────────────────────┐
    @allure.step('✔ Check [Menu button]')
    def check_menu_btn(self, nth_index: int = 0):
        """
        ✔ Check [Menu button]

        - ✔ Button - visible
        - ✔ Button - enabled

        :param nth_index: nth-index —> for use in: locator.nth(nth_index)
        """
        self.check_menu_btn_visible(nth_index)
        self.check_menu_btn_enabled(nth_index)
    # ────────────────────────────────────────┘
    # Visible
    def check_menu_btn_visible(self, nth_index: int = 0):
        """
        ✔ Check [Menu button] is visible

        :param nth_index: nth-index —> for use in: locator.nth(nth_index)
        """
        self.menu_btn().check_visible(nth=nth_index)

    # Enabled
    def check_menu_btn_enabled(self, nth_index: int = 0):
        """
        ✔ Check [Menu button] is enabled

        :param nth_index: nth-index —> for use in: locator.nth(nth_index)
        """
        self.menu_btn().check_enabled(nth=nth_index)


    # [Image]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Image]')
    def check_image(self, nth_index: int = 0):
        """
        ✔ Check [Image]

        - ✔ Image - visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_image_visible(nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_image_visible(self, nth_index: int = 0):
        """
        ✔ Check [Image] is visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.image().check_visible(nth=nth_index)


    # [Max score]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Max score]')
    def check_max_score(self, max_score: str, nth_index: int = 0):
        """
        ✔ Check [Max score]

        - ✔ Max score - visible
        - ✔ Max score - text

        :param max_score: Max score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_max_score_visible(nth_index)
        self.check_max_score_text(nth_index=nth_index, max_score=max_score)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_max_score_visible(self, nth_index: int = 0):
        """
        ✔ Check [Max score] is visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.max_score().check_visible(nth=nth_index)

    # Text
    def check_max_score_text(self, max_score: str, nth_index: int = 0):
        """
        ✔ Check [Max score] text

        :param max_score: Max score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.max_score().check_text(self.max_score_text(max_score), nth=nth_index)


    # [Min score]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Min score]')
    def check_min_score(self, min_score: str, nth_index: int = 0):
        """
        ✔ Check [Min score]

        - ✔ Min score - visible
        - ✔ Min score - text

        :param min_score: Min score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_min_score_visible(nth_index)
        self.check_min_score_text(nth_index=nth_index, min_score=min_score)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_min_score_visible(self, nth_index: int = 0):
        """
        ✔ Check [Min score] is visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.min_score().check_visible(nth=nth_index)

    # Text
    def check_min_score_text(self, min_score: str, nth_index: int = 0):
        """
        ✔ Check [Min score] text

        :param min_score: Min score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.min_score().check_text(self.min_score_text(min_score), nth=nth_index)


    # [Estimated time]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Estimated time]')
    def check_estimated_time(self, estimated_time: str, nth_index: int = 0):
        """
        ✔ Check [Estimated time]

        - ✔ Estimated time - visible
        - ✔ Estimated time - text

        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_estimated_time_visible(nth_index)
        self.check_estimated_time_text(nth_index=nth_index, estimated_time=estimated_time)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    # Visible
    def check_estimated_time_visible(self, nth_index: int = 0):
        """
        ✔ Check [Estimated time] is visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.estimated_time().check_visible(nth=nth_index)

    # Text
    def check_estimated_time_text(self, estimated_time: str, nth_index: int = 0):
        """
        ✔ Check [Estimated time] text

        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.estimated_time().check_text(self.estimated_time_text(estimated_time), nth=nth_index)

#=======================================================================================================================
