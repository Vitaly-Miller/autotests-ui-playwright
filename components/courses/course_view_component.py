"""
Course View component
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
        self.MAX_SCORE_PART_TEXT = 'Max score:'            # Part of text (Ex: "Max score: 100")
        self.MIN_SCORE_PART_TEXT = 'Min score:'            # Part of text (Ex: "Min score: 10")
        self.ESTIMATED_TIME_PART_TEXT = 'Estimated time:'  # Part of text (Ex: "Estimated time: 5h")

        # --------------------------------------------- ⿴ COMPONENTS --------------------------------------------------
        self.menu = CourseViewMenuComponent(page)          # Course View Menu

        # ---------------------------------------------- ㉧ LOCATORS ----------------------------------------------------
        self.title = page.get_by_test_id('course-widget-title-text')
        self.image = page.get_by_test_id('course-preview-image')
        self.max_score = page.get_by_test_id('course-max-score-info-row-view-text')
        self.min_score = page.get_by_test_id('course-min-score-info-row-view-text')
        self.estimated_time = page.get_by_test_id('course-estimated-time-info-row-view-text')

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_menu_btn(self, index: int):
        """
        Click <Course View [Menu button]> of the Courses List page

        -  Button - ✔ visible | ▶ click

        :param index: nth-index —> for use in: locator.nth(index)
        """
        self.menu.click_menu_btn(index)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ══════════════════════════════════════════════════════════════════════╗
    def check_component(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        """
        Check <Course View> component of the Courses List page

        - ✔ Menu button - visible | enabled
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
        self.menu.check_menu_btn(index)
        self.check_image_visible(index)
        self.check_title(index=index, title=title)
        self.check_max_score(index=index, max_score=max_score)
        self.check_min_score(index=index, min_score=min_score)
        self.check_estimated_time(index=index, estimated_time=estimated_time)
    # ═══════════════════════════════════════════════════════════════════════╝

    # Image
    def check_image_visible(self, index: int):
        """
        Check <Course View [Image]> of the Courses List page - visible

        - ✔ Image - visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ <Course View [Image] (nth-index: {index})> of the Courses List page - invisible!'
        expect(self.image.nth(index), error).to_be_visible()

    # Title
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title(self, index: int, title: str):
        """
        Check <Course View [Title]> of the Courses List page - visible

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
        Check <Course View [Title]> of the Courses List page - visible

        - ✔ Title - visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ <Course View [Title] (nth-index: {index})> of the Courses List page - invisible!'
        expect(self.title.nth(index), error).to_be_visible()

    def check_title_text(self, title: str, index: int):
        """
        Check <Course View [Title] text> of the Courses List page - correct

        - ✔ Text - correct

        :param title: Course title
        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ <Course View [Title] text (nth-index: {index})> of the Courses List page - incorrect!'
        expect(self.title.nth(index), error).to_have_text(title)

    # Max score
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_max_score(self, index: int, max_score: str):
        """
        Check <Course View [Max score]> of the Courses List page

        - ✔ Min score - visible
        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param max_score: Max score
        """
        self.check_max_score_visible(index)
        self.check_max_score_text(index=index, max_score=max_score)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_max_score_visible(self, index: int):
        """
        Check <Course View [Max score]> of the Courses List page - visible

        - ✔ Max score - visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ <Course View [Max score] (nth-index: {index})> of the Courses List page - invisible!'
        expect(self.max_score.nth(index), error).to_be_visible()

    def check_max_score_text(self, max_score: str, index: int):
        """
        Check <Course View [Max score] text> of the Courses List page - correct

        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param max_score: Max score
        """
        error = f'❌ <Course View [Max score] text (nth-index: {index})> of the Courses List page - incorrect!'
        expect(self.max_score.nth(index), error).to_have_text(f'{self.MAX_SCORE_PART_TEXT} {max_score}')

    # Min score
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_min_score(self, index: int, min_score: str):
        """
        Check <Course View [Min score]> of the Courses List page

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
        Check <Course View [Min score]> of the Courses List page - visible

        - ✔ Min score - visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ <Course View [Min score] (nth-index: {index})> of the Courses List page - invisible!'
        expect(self.min_score.nth(index), error).to_be_visible()

    def check_min_score_text(self, index: int, min_score: str, ):
        """
        Check <Course View [Min score] text> of the Courses List page - correct

        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param min_score: Min score

        """
        error = f'❌ <Course View [Min score] text (nth-index: {index})> of the Courses List page - incorrect!'
        expect(self.min_score.nth(index), error).to_have_text(f'{self.MIN_SCORE_PART_TEXT} {min_score}')

    # Estimated time
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_estimated_time(self, index: int, estimated_time: str):
        """
        Check <Course View [Estimated time]> of the Courses List page

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
        Check <Course View [Estimated time]> of the Courses List page - visible

        - ✔ Estimated time - visible

        :param index: nth-index —> for use in: locator.nth(index)
        """
        error = f'❌ <Course View [Estimated time] (nth-index: {index})> of the Courses List page - invisible!'
        expect(self.estimated_time.nth(index), error).to_be_visible()

    def check_estimated_time_text(self, index: int, estimated_time: str):
        """
        Check <Course View [Estimated time] text> of the Courses List page - correct

        - ✔ Text - correct

        :param index: nth-index —> for use in: locator.nth(index)
        :param estimated_time: Estimated time

        """
        error = f'❌ <Course View [Estimated time] text (nth-index: {index})> of the Courses List page - incorrect!'
        expect(self.estimated_time.nth(index), error).to_have_text(f'{self.ESTIMATED_TIME_PART_TEXT} {estimated_time}')

#=======================================================================================================================
