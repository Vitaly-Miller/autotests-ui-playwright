"""
Courses list page > [Course card] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.courses.courses_list.course_card_menu_component import CourseCardMenuComponent

#=======================================================================================================================
"""
[Course card]:
- Menu (component)
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

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
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
    # ───────────────────────────────────────────────────────────────────────┐
    def check_course_card(
            self,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str,
            nth_index: int = 0
    ):
        """
        ✔ Check [Course View]

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
    # ───────────────────────────────────────────────────────────────────────┘

    # Title
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self, title: str, nth_index: int = 0):
        """
        ✔ Check [Title] visible

        - ✔ Title - visible
        - ✔ Text - correct

        :param title: Course title
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_title_visible(nth_index)
        self.check_title_text(title=title, nth_index=nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self, nth_index: int = 0):
        """
        ✔ Check [Title] visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Title] (nth-index: {nth_index}) - invisible!'
        expect(self.title.nth(nth_index), error).to_be_visible()

    def check_title_text(self, title: str, nth_index: int = 0):
        """
        ✔ Check [Title] text

        :param title: Course title
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Title] (nth-index: {nth_index}) - incorrect text!'
        expect(self.title.nth(nth_index), error).to_have_text(title)


    # [Menu button]
    # ───────────────────────────────────────────┐
    def check_menu_btn(self, nth_index: int = 0):
        """
        ✔ Check [Menu button]

        - ✔ Button - visible
        - ✔ Button - enabled

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        self.check_menu_btn_visible(nth_index)
        self.check_menu_btn_enabled(nth_index)
    # ───────────────────────────────────────────┘
    def check_menu_btn_visible(self, nth_index: int = 0):
        """
        ✔ Check [Menu button] visible

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'❌ Courses list page > Course View > [Menu button] (nth_index: {nth_index}) - invisible!'
        expect(self.menu_btn.nth(nth_index), error).to_be_visible()

    def check_menu_btn_enabled(self, nth_index: int = 0):
        """
        ✔ Check [Menu button] enabled

        :param nth_index: nth_index —> for use in: locator.nth(nth_index)
        """
        error = f'❌ Courses list page > Course View > [Menu button] (nth_index: {nth_index}) - disabled!'
        expect(self.menu_btn.nth(nth_index), error).to_be_enabled()


    # Image
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_image(self, nth_index: int = 0):
        """
        ✔ Check [Image]

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_image_visible(nth_index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_image_visible(self, nth_index: int = 0):
        """
        ✔ Check [Image] visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Image] (nth-index: {nth_index}) - invisible!'
        expect(self.image.nth(nth_index), error).to_be_visible()


    # Max score
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_max_score(self, max_score: str, nth_index: int = 0):
        """
        ✔ Check [Max score]

        - ✔ Max score - visible
        - ✔ Text - correct

        :param max_score: Max score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_max_score_visible(nth_index)
        self.check_max_score_text(nth_index=nth_index, max_score=max_score)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_max_score_visible(self, nth_index: int = 0):
        """
        ✔ Check [Max score] visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Max score] (nth-index: {nth_index}) - invisible!'
        expect(self.max_score.nth(nth_index), error).to_be_visible()

    def check_max_score_text(self, max_score: str, nth_index: int = 0):
        """
        ✔ Check [Max score] text

        :param max_score: Max score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Max score] (nth-index: {nth_index}) - incorrect text!'
        expect(self.max_score.nth(nth_index), error).to_have_text(self.MAX_SCORE_TEXT(max_score))


    # Min score
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_min_score(self, min_score: str, nth_index: int = 0):
        """
        ✔ Check [Min score]

        - ✔ Min score - visible
        - ✔ Text - correct

        :param min_score: Min score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_min_score_visible(nth_index)
        self.check_min_score_text(nth_index=nth_index, min_score=min_score)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_min_score_visible(self, nth_index: int = 0):
        """
        ✔ Check [Min score] visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ [Min score] (nth-index: {nth_index}) - invisible!'
        expect(self.min_score.nth(nth_index), error).to_be_visible()

    def check_min_score_text(self, min_score: str, nth_index: int = 0):
        """
        ✔ Check [Min score] text

        :param min_score: Min score
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Min score] (nth-index: {nth_index}) - incorrect text!'
        expect(self.min_score.nth(nth_index), error).to_have_text(self.MIN_SCORE_TEXT(min_score))


    # Estimated time
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_estimated_time(self, estimated_time: str, nth_index: int = 0):
        """
        ✔ Check [Estimated time]

        - ✔ Estimated time - visible
        - ✔ Text - correct

        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        self.check_estimated_time_visible(nth_index)
        self.check_estimated_time_text(nth_index=nth_index, estimated_time=estimated_time)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_estimated_time_visible(self, nth_index: int = 0):
        """
        ✔ Check [Estimated time] visible

        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Estimated time] (nth-index: {nth_index}) - invisible!'
        expect(self.estimated_time.nth(nth_index), error).to_be_visible()

    def check_estimated_time_text(self, estimated_time: str, nth_index: int = 0):
        """
        ✔ Check [Estimated time] text

        :param estimated_time: Estimated time
        :param nth_index: For use: locator.nth(nth_index) - (default: 0)
        """
        error = f'❌ Courses list page > Course View > [Estimated time] (nth-index: {nth_index}) - incorrect!'
        expect(self.estimated_time.nth(nth_index), error).to_have_text(self.ESTIMATED_TIME_TEXT(estimated_time))

#=======================================================================================================================
