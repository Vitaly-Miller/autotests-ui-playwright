"""
Courses list page > [Course card] (component)
"""
import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.courses.courses_list.course_card_menu_component import CourseCardMenuComponent

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
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.MAX_SCORE_TEXT = lambda max_score: f'Max score: {max_score}'
        self.MIN_SCORE_TEXT = lambda min_score: f'Min score: {min_score}'
        self.ESTIMATED_TIME_TEXT = lambda estimated_time: f'Estimated time: {estimated_time}'

        # ------------------------------------- >>> [Element] path (for debug) -----------------------------------------
        self.course_card_component = '❌ Courses list page > Course card'
        self.title_element = lambda nth_index: f'{self.course_card_component} > [Title] (nth-index: {nth_index})'
        self.menu_btn_element = lambda nth_index: f'{self.course_card_component} > [Menu button] (nth-index: {nth_index})'
        self.image_element = lambda nth_index: f'{self.course_card_component} > [Image] (nth-index: {nth_index})'
        self.max_score_element = lambda nth_index: f'{self.course_card_component} > [Max score] (nth-index: {nth_index})'
        self.min_score_element = lambda nth_index: f'{self.course_card_component} > [Min score] (nth-index: {nth_index})'
        self.estimated_time_element = lambda nth_index: f'{self.course_card_component} > [Estimated time] (nth-index: {nth_index})'

        # --------------------------------------------- ⿳ COMPONENTS --------------------------------------------------
        self.menu = CourseCardMenuComponent(page)

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.title = page.get_by_test_id('course-widget-title-text')
        self.menu_btn = page.get_by_test_id('course-view-menu-button')
        self.image = page.get_by_test_id('course-preview-image')
        self.max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        self.min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        self.estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Click [Menu button]
    @allure.step('▶ Click [Menu button]')
    def click_menu_btn(self, nth_index: int = 0):
        """
        ▶ Click [Menu button]

        - ✔ Menu button - visible
        - ▶ Menu button - click

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        self.check_menu_btn_visible(nth_index)
        self.menu_btn.nth(nth_index).click()

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Course card]
    # ──────────────────────────────────────────────────────────────────────────────┐
    @allure.step('✔ Check [Course card]')
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
        ✔ Check visible [Title]

        - ✔ Title - visible
        - ✔ Title - text

        :param title: Course title
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_title_visible(nth_index)
        self.check_title_text(title=title, nth_index=nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Title]')
    def check_title_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Title]

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.title_element(nth_index)} - invisible!'
        expect(self.title.nth(nth_index), error).to_be_visible()

    @allure.step('✔ Check text of [Title]')
    def check_title_text(self, title: str, nth_index: int = 0):
        """
        ✔ Check text of [Title]

        :param title: Course title
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.title_element(nth_index)} - incorrect text!'
        expect(self.title.nth(nth_index), error).to_have_text(title)


    # [Menu button]
    # ────────────────────────────────────────┐
    @allure.step('✔ Check [Menu button]')
    def check_menu_btn(self, nth_index: int = 0):
        """
        ✔ Check [Menu button]

        - ✔ Button - visible
        - ✔ Button - enabled

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        self.check_menu_btn_visible(nth_index)
        self.check_menu_btn_enabled(nth_index)
    # ────────────────────────────────────────┘
    @allure.step('✔ Check visible [Menu button]')
    def check_menu_btn_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Menu button]

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'{self.menu_btn_element(nth_index)} - invisible!'
        expect(self.menu_btn.nth(nth_index), error).to_be_visible()

    @allure.step('✔ Check enabled [Menu button]')
    def check_menu_btn_enabled(self, nth_index: int = 0):
        """
        ✔ Check enabled [Menu button]

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'{self.menu_btn_element(nth_index)} - disabled!'
        expect(self.menu_btn.nth(nth_index), error).to_be_enabled()


    # [Image]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    @allure.step('✔ Check [Image]')
    def check_image(self, nth_index: int = 0):
        """
        ✔ Check [Image]

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_image_visible(nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Image]')
    def check_image_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Image]

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.image_element(nth_index)} - invisible!'
        expect(self.image.nth(nth_index), error).to_be_visible()


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
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Max score]')
    def check_max_score_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Max score]

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.max_score_element(nth_index)} - invisible!'
        expect(self.max_score.nth(nth_index), error).to_be_visible()

    @allure.step('✔ Check text of [Max score]')
    def check_max_score_text(self, max_score: str, nth_index: int = 0):
        """
        ✔ Check text of [Max score]

        :param max_score: Max score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.max_score_element(nth_index)} - incorrect text!'
        expect(self.max_score.nth(nth_index), error).to_have_text(self.MAX_SCORE_TEXT(max_score))


    # [Min score]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    @allure.step('✔ Check visible [Min score]')
    def check_min_score_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Min score]

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.min_score_element(nth_index)} - invisible!'
        expect(self.min_score.nth(nth_index), error).to_be_visible()

    @allure.step('✔ Check text of [Min score]')
    def check_min_score_text(self, min_score: str, nth_index: int = 0):
        """
        ✔ Check text of [Min score]

        :param min_score: Min score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.min_score_element(nth_index)} - incorrect text!'
        expect(self.min_score.nth(nth_index), error).to_have_text(self.MIN_SCORE_TEXT(min_score))


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
    @allure.step('✔ Check visible [Estimated time]')
    def check_estimated_time_visible(self, nth_index: int = 0):
        """
        ✔ Check visible [Estimated time]

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.estimated_time_element(nth_index)} - invisible!'
        expect(self.estimated_time.nth(nth_index), error).to_be_visible()

    @allure.step('✔ Check text of [Estimated time]')
    def check_estimated_time_text(self, estimated_time: str, nth_index: int = 0):
        """
        ✔ Check text of [Estimated time]

        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'{self.estimated_time_element(nth_index)} - incorrect!'
        expect(self.estimated_time.nth(nth_index), error).to_have_text(self.ESTIMATED_TIME_TEXT(estimated_time))

#=======================================================================================================================
