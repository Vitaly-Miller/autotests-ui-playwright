"""
Create course page > Exercises > Exercise > [Form] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page, expect

#=======================================================================================================================
"""
[Form]:
- Title field
- Description field
"""
class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # [Title field]
        self.TITLE_FIELD_NAME = 'Title'
        # [Description field]
        self.DESCRIPTION_FIELD_NAME = 'Description'

        # --------------------------------------- ㉤ LOCATORS {dynamic} (lambda) ----------------------------------------
        # [Title field]
        self.title_field = lambda index: page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        # [Description field]
        self.description_field = lambda index: page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')

    # -------------------------------------------- ㉤ LOCATORS {dynamic} (def)-------------------------------------------
    # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ⚠️ NOT USING!  ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╮
    # [Title field]
    def _title_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

    # [Description field]
    def _description_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')
    # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ FOR EXAMPLE ONLY ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╯


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Form]
    # ────────────────────────────────────────────────────────────┐
    def fill_form(self, index: int, title: str, description: str):
        """
        - ▶ Fill [Form]

        - ▶ Fill [Title] field
        - ▶ Fill [Description] field

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title
        :param description: Description
        """
        self.title_field(index).fill(title)
        self.description_field(index).fill(description)
    # ────────────────────────────────────────────────────────────┘
    # Fill [Title field]
    def fill_title_field(self, index: int, title: str):
        """
        ▶ Fill [Title] field

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title
        """
        self.description_field(index).fill(title)

    # Fill [Description field]
    def fill_description_field(self, index: int, description: str):
        """
        ▶ Fill [Description] field

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Description
        """
        self.description_field(index).fill(description)


    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Form]
    # ─────────────────────────────────────────────────────────────────────┐
    def check_form(
            self,
            index: int,
            title: str | None = None,
            description: str | None = None
    ):
        """
        ✔ Check [Form]

        - ✔ Title field - visible | - name | - filled / default value
        - ✔ Description field - visible | - name | - filled / default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        :param description: Exercise description
        """
        self.check_title_field(index=index, title=title)
        self.check_description_field(index=index, description=description)
    # ──────────────────────────────────────────────────────────────────────┘

    # [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title_field(self, index: int, title: str | None = None):
        """
        ✔ Check [Title field]

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly / default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        """
        self.check_title_field_visible(index)
        self.check_title_field_name(index)
        if title:
            self.check_title_field_filled(index=index, title=title)
        else:
            self.check_title_field_filled(index)
        # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_field_visible(self, index: int):
        """
        ✔ Check [Title field] visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Title field] - invisible!'
        expect(self.title_field(index), error).to_be_visible()

    def check_title_field_name(self, index: int):
        """
        ✔ Check [Title field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Title field] - incorrect name!'
        expect(self.title_field(index), error).to_have_accessible_name(self.TITLE_FIELD_NAME)

    def check_title_field_filled(self, index: int, title: str = 'Exercise title'):
        """
        ✔ Check [Title field] filled correctly

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        -----------------
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Title field] - filled incorrectly!'
        expect(self.description_field(index), error).to_have_value(title)


    # [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_description_field(self, index: int, description: str | None = None):
        """
        ✔ Check [Description field]

        - ✔ Field - visible
        - ✔ Field name - correct
        - ✔ Field - filled correctly / default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description
        """
        self.check_description_field_visible(index)
        self.check_description_field_name(index)
        if description:
            self.check_description_field_filled(index=index, description=description)
        else:
            self.check_description_field_filled(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_description_field_visible(self, index: int):
        """
        ✔ Check [Description field] visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Description field] - invisible!'
        expect(self.description_field(index), error).to_be_visible()

    def check_description_field_name(self, index: int):
        """
        ✔ Check [Description field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Description field] - incorrect name!'
        expect(self.description_field(index), error).to_have_accessible_name(self.DESCRIPTION_FIELD_NAME)

    def check_description_field_filled(self, index: int, description: str = 'Exercise description'):
        """
        ✔ Check [Description field] filled correctly

        If is passed:
        -------------
        - ✔ Field - filled correctly

        If is NOT passed:
        -----------------
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Description field] - filled incorrectly!'
        expect(self.description_field(index), error).to_have_value(description)


#=======================================================================================================================
