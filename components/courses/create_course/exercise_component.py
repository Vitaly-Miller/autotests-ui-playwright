"""
Create course page > Exercises > [Exercise] (component)
"""
from components.base_component import BaseComponent
from playwright.sync_api import Locator, Page, expect

#=======================================================================================================================
"""
Elements:
- Toolbar
  - Title
  - Delete exercise button

- Form
  - Title field
  - Description field
"""
class CreateCourseExerciseComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # ------------------------------------------------ 𝌆 DATA ------------------------------------------------------
        # [Toolbar]
        self.TOOLBAR_TITLE_TEXT = lambda index: f'#{index + 1} Exercise'
        # Form > [Title field]
        self.TITLE_FIELD_NAME = 'Title'
        # Form > [Description field]
        self.DESCRIPTION_FIELD_NAME = 'Description'

       # ---------------------------------------- ㉤ LOCATORS {dynamic} (lambda) ---------------------------------------
        # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ⚠️ NOT USING! - FOR EXAMPLE ONLY ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╮
        # [Toolbar]
        self._toolbar_title = lambda index: page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')
        self._delete_exercise_btn = lambda index: page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')
        # [Form]
        self._title_field = lambda index: page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')
        self._description_field = lambda index=0: page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')
        # ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ ⬇︎ use dynamic def-locators ⬇︎ ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄╯

    # -------------------------------------------- ㉤ LOCATORS {dynamic} (def)-------------------------------------------
    # [Toolbar]
    def toolbar_title(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-subtitle-text')

    def delete_exercise_btn(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-{index}-box-toolbar-delete-exercise-button')

    # [Form]
    def title_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-title-{index}-input')

    def description_field(self, index: int) -> Locator:
        return self.page.get_by_test_id(f'create-course-exercise-form-description-{index}-input')


    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    def click_delete_exercise_btn(self, index: int):
        """
        ▶ Click [Delete exercise button]

        - ✔ Button - visible
        - ▶ Button - click

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.check_delete_exercise_btn(index)
        self.delete_exercise_btn(index).click()

    def fill_form(self, index: int, title: str, description: str):
        """
        - ▶ Fill [Form]

        - ✔ Check [Form field]s - titles | - visible | - names | - default values
        - ▶ Fill [Form field]s - title | - description
        - ✔ Check [Form field]s - titles | - visible | - names | - filled values

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        :param description: Description title
        """
        self.check_form(index)
        self.title_field(index).fill(title)
        self.description_field(index).fill(description)
        self.check_form(
            index=index,
            title=title,
            description=description
        )

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # ───────────────────────────────────────┐
    def check_exercise(
            self,
            index: int,
            title: str | None = None,
            description: str | None = None
    ):
        """
        ✔ Check [Exercise]

        - ✔ Toolbar - Title | Delete exercise button
        - ✔ Form - Title | Description

        :param index: index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        :param title: Exercise title
        :param description: Exercise description
        :return:
        """
        self.check_toolbar(index)
        self.check_form(
            index=index,
            title=title,
            description=description)
    # ───────────────────────────────────────┘

    # [Toolbar]
    # ───────────────────────────────────────┐
    def check_toolbar(self, index: int):
        """
        ✔ Check [Toolbar]

        - ✔ Title - visible | - text
        - ✔ Delete exercise button - visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.check_toolbar_title(index)
        self.check_delete_exercise_btn(index)
    # ───────────────────────────────────────┘

    # Toolbar [Title]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_toolbar_title(self, index: int):
        """
        ✔ Check [Title]

        - ✔ Title - visible
        - ✔ Text - correct

        :param index: Locator DOM-index (ex: ...-exercise-{index}-box-toolbar-...)
        """
        self.check_toolbar_title_visible(index)
        self.check_toolbar_title_text(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_toolbar_title_visible(self, index: int):
        """
        ✔ Check [Title] visible

        :param index: Locator DOM-index (ex: ...-exercise-{index}-box-toolbar-...)
        """
        error = f'❌ Registration page > <Create course page > Exercises > Exercise > Toolbar > [Title] - invisible!'
        expect(self.toolbar_title(index), error).to_be_visible()

    def check_toolbar_title_text(self, index: int):
        """
        ✔ Check [Title] text

        (Ex: "#1 Exercise", "#2 Exercise", ...)

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Registration page > <Create course page > Exercises > Exercise > Toolbar > [Title] - incorrect text!'
        expect(self.toolbar_title(index), error).to_have_text(self.TOOLBAR_TITLE_TEXT(index))

    # Toolbar [Delete exercise button]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    def check_delete_exercise_btn(self, index: int):
        """
        ✔ Check [Delete exercise button]

        - ✔ Button - visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        self.check_delete_exercise_btn_visible(index)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
    def check_delete_exercise_btn_visible(self, index: int):
        """
        ✔ Check [Delete exercise button] visible

        :param index: Locator DOM-index (Ex: "...-exercise-{index}-box-toolbar-...")
        """
        error = f'❌ Create course page > Exercises > Exercise > Toolbar > [Delete exercise button] - invisible!'
        expect(self.delete_exercise_btn(index), error).to_be_visible()


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

    # Form [Title field]
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


    # Form [Description field]
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
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
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘
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
