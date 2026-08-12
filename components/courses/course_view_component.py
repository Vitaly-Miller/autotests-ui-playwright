"""
Course view (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from components.courses.course_view_menu_component import CourseViewMenuComponent

#=======================================================================================================================
"""
Elements:
- Menu (component)
- Title
- Image
- Max score
- Min score
- Estimated time
"""
class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        self.MAX_SCORE_TEXT = lambda max_score: f'Max score: {max_score}'
        self.MIN_SCORE_TEXT = lambda min_score: f'Min score: {min_score}'
        self.ESTIMATED_TIME_TEXT = lambda estimated_time: f'Estimated time: {estimated_time}'

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
        self.menu = CourseViewMenuComponent(page)

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.title = page.get_by_test_id('course-widget-title-text')
        self.image = page.get_by_test_id('course-preview-image')
        self.max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        self.min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        self.estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_menu_btn(self, index: int):
        """
        ▶ Click [Menu button]

        - Button - ✔ visible | - ▶ click

        :param index: nth-index —> for use in: locator.nth(index)
        """
        self.menu.click_menu_btn(index)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ──────────────────────────────────────────────────────────────────────┐
    def check_component(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        """
        ✔ Check [Course View]

        - ✔ Menu button - visible | - enabled
        - ✔ Image - visible
        - ✔ Title - visible | - text
        - ✔ Max score - visible | - text
        - ✔ Min score - visible | - text
        - ✔ Estimated time - visible | - text

        :param index: nth-index —> for use in: locator.nth(index)
        :param title: Course title
        :param max_score: Max score
        :param min_score: Min score
        :param estimated_time: Estimated time
        """
        self.menu.check_menu_btn(index)
        self.check_image(index)
        self.check_title(index=index, title=title)
        self.check_max_score(index=index, max_score=max_score)
        self.check_min_score(index=index, min_score=min_score)
        self.check_estimated_time(index=index, estimated_time=estimated_time)
    # ───────────────────────────────────────────────────────────────────────┘

    # Image
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_image(self, index: int):
        """
        ✔ Check [Image]

        :param index: nth-index —> for use in: locator.nth(index)
        """
        self.check_image_visible(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_image_visible(self, index: int):
        """
        ✔ Check [Image] visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ Courses list page -> Course View -> [Image] (nth-index: {index}) - invisible!'
        expect(self.image.nth(index), error).to_be_visible()

    # Title
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self, index: int, title: str):
        """
        ✔ Check [Title] visible

        - ✔ Title - visible
        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param title: Course title
        """
        self.check_title_visible(index)
        self.check_title_text(index=index, title=title)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_visible(self, index: int):
        """
        ✔ Check [Title] visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ Courses list page -> Course View -> [Title] (nth-index: {index}) - invisible!'
        expect(self.title.nth(index), error).to_be_visible()

    def check_title_text(self, index: int, title: str):
        """
        ✔ Check [Title] text

        :param index: nth-index —> for use in: locator.nth(index)
        :param title: Course title
        """
        error = f'❌ Courses list page -> Course View -> [Title] (nth-index: {index}) - incorrect text!'
        expect(self.title.nth(index), error).to_have_text(title)

    # Max score
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_max_score(self, index: int, max_score: str):
        """
        ✔ Check [Max score]

        - ✔ Max score - visible
        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param max_score: Max score
        """
        self.check_max_score_visible(index)
        self.check_max_score_text(index=index, max_score=max_score)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_max_score_visible(self, index: int):
        """
        ✔ Check [Max score] visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ Courses list page -> Course View -> [Max score] (nth-index: {index}) - invisible!'
        expect(self.max_score.nth(index), error).to_be_visible()

    def check_max_score_text(self, index: int, max_score: str):
        """
        ✔ Check [Max score] text

        :param index: nth-index —> for use in: locator.nth(index)
        :param max_score: Max score
        """
        error = f'❌ Courses list page -> Course View -> [Max score] (nth-index: {index}) - incorrect text!'
        expect(self.max_score.nth(index), error).to_have_text(self.MAX_SCORE_TEXT(max_score))

    # Min score
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_min_score(self, index: int, min_score: str):
        """
        ✔ Check <Course View [Min score]> of the Courses list page

        - ✔ Min score - visible
        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param min_score: Min score
        """
        self.check_min_score_visible(index)
        self.check_min_score_text(index=index, min_score=min_score)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_min_score_visible(self, index: int):
        """
        ✔ Check [Min score] visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ [Min score] (nth-index: {index}) - invisible!'
        expect(self.min_score.nth(index), error).to_be_visible()

    def check_min_score_text(self, index: int, min_score: str, ):
        """
        ✔ Check [Min score] text

        :param index: nth-index —> for use in: locator.nth(index)
        :param min_score: Min score
        """
        error = f'❌ Courses list page -> Course View -> [Min score] (nth-index: {index}) - incorrect text!'
        expect(self.min_score.nth(index), error).to_have_text(self.MIN_SCORE_TEXT(min_score))

    # Estimated time
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_estimated_time(self, index: int, estimated_time: str):
        """
        ✔ Check [Estimated time]

        - ✔ Estimated time - visible
        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param estimated_time: Estimated time
        """
        self.check_estimated_time_visible(index)
        self.check_estimated_time_text(index=index, estimated_time=estimated_time)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_estimated_time_visible(self, index: int):
        """
        ✔ Check [Estimated time] visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ Courses list page -> Course View -> [Estimated time] (nth-index: {index}) - invisible!'
        expect(self.estimated_time.nth(index), error).to_be_visible()

    def check_estimated_time_text(self, index: int, estimated_time: str):
        """
        ✔ Check [Estimated time] text

        :param index: nth-index —> for use in: locator.nth(index)
        :param estimated_time: Estimated time
        """
        error = f'❌ Courses list page -> Course View -> [Estimated time] (nth-index: {index}) - incorrect!'
        expect(self.estimated_time.nth(index), error).to_have_text(self.ESTIMATED_TIME_TEXT(estimated_time))

#=======================================================================================================================
