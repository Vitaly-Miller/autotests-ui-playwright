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
    # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ⚠️ NOT USING ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╮
    # [Title field]
    def _title_field(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

    # [Description field]
    def _description_field(self, index: int = 0) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')
    # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ FOR EXAMPLE ONLY ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╯


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Fill [Form]
    # ─────────────────────────────────────────────────────────────────────┐
    def fill(
            self,
            index: int = 0,
            title: str | None = None,
            description: str | None = None
    ):
        """
        - ▶ Fill [Exercise form]

        - ▶ Title field - fill
        - ▶ Description field - fill

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title
        :param description: Description
        """
        self.fill_title_field(index=index, title=title)
        self.fill_description_field(index=index, description=description)
    # ─────────────────────────────────────────────────────────────────────┘
    # Fill [Title field]
    def fill_title_field(self, index: int = 0, title: str | None = None):
        """
        ▶ Fill [Title field]

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title
        """
        if title is not None:
            self.title_field(index).fill(title)

    # Fill [Description field]
    def fill_description_field(self, index: int = 0, description: str | None = None):
        """
        ▶ Fill [Description field]

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Description
        """
        if description is not None:
            self.description_field(index).fill(description)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Form]
    # ───────────────────────────────────────────────────────────────────┐
    def check(
            self,
            index: int = 0,
            title: str | None = None,
            description: str | None = None
    ):
        """
        ✔ Check [Exercise form]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        :param description: Exercise description
        """
        self.check_title_field(index=index, title=title)
        self.check_description_field(index=index, description=description)
    # ────────────────────────────────────────────────────────────────────┘

    # [Title field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_title_field(self, index: int = 0, title: str | None = None):
        """
        ✔ Check [Title field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Title
        """
        if title is not None:
            self.check_title_field_value(index=index, title=title)
        else:
            self.check_title_field_visible(index)
            self.check_title_field_name(index)
            self.check_title_field_value(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_title_field_visible(self, index: int = 0):
        """
        ✔ Check [Title field] visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Title field] - invisible!'
        expect(self.title_field(index), error).to_be_visible()

    def check_title_field_name(self, index: int = 0):
        """
        ✔ Check [Title field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Title field] - incorrect name!'
        expect(self.title_field(index), error).to_have_accessible_name(self.TITLE_FIELD_NAME)

    def check_title_field_value(self, index: int = 0, title: str = 'Exercise title'):
        """
        ✔ Check [Title field] value

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Title field] - incorrect value!'
        expect(self.description_field(index), error).to_have_value(title)

    # [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_description_field(self, index: int = 0, description: str | None = None):
        """
        ✔ Check [Description field]

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - visible
        - ✔ Field - name
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Description
        """
        if description is not None:
            self.check_description_field_value(index=index, description=description)
        else:
            self.check_description_field_visible(index)
            self.check_description_field_name(index)
            self.check_description_field_value(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_description_field_visible(self, index: int = 0):
        """
        ✔ Check [Description field] visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Description field] - invisible!'
        expect(self.description_field(index), error).to_be_visible()

    def check_description_field_name(self, index: int = 0):
        """
        ✔ Check [Description field] name

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Description field] - incorrect name!'
        expect(self.description_field(index), error).to_have_accessible_name(self.DESCRIPTION_FIELD_NAME)

    def check_description_field_value(self, index: int = 0, description: str = 'Exercise description'):
        """
        ✔ Check [Description field] value

        If is passed:
        -------------
        - ✔ Field - value

        If is NOT passed:
        -----------------
        - ✔ Field - default value

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param description: Exercise description
        """
        error = f'❌ Create course page > Exercises > Exercise > Form > [Description field] - incorrect value!'
        expect(self.description_field(index), error).to_have_value(description)


#=======================================================================================================================
