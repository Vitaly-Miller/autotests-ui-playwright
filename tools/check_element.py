"""
Check element
"""
import allure
from playwright.sync_api import Locator, expect

#=======================================================================================================================
class Check:
    #------------------------------------------------------- [Element] -------------------------------------------------
    @staticmethod
    def element(
            locator: Locator,
            element_path: str,
            element_name: str,
            visible: bool = True,
            enabled: bool | None = None,
            text: str | None = None,
            name: str | None = None,
            value: str | None = None,
            attribute_type: str | None = None,
            attribute_value: str | None = None,
            index: int = 0
    ):
        """
        ✔ Check [Element]

        - ✔ Element - visible / invisible
        - ✔ Element - enabled / disabled (optional)
        - ✔ Element - text (optional)
        - ✔ Element - name (optional)
        - ✔ Element - value (optional)
        - ✔ Element - attribute value (optional)


        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name (for logging)  (Ex: 'Description field']
        :param visible: True/False
        :param enabled: True/False                       (Active for action)
        :param name: Element has name     (accessible)   (Ex: 'Description')
        :param text: Element has a text                  (Ex: 'Create course')
        :param value: Value of element                   (Ex: 'This is my description in the field')
        :param attribute_type: Element has an attribute  (Ex: 'href', 'placeholder', etc.)
        :param attribute_value: Value of attribute       (Ex: '#/auth/registration', 'Enter description here', etc.)
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check [{element_name}]'):
            if visible:
                Check.visible(locator=locator, element_path=element_path, element_name=element_name, index=index)
            else:
                Check.invisible(locator=locator, element_path=element_path, element_name=element_name, index=index)

            if enabled is not None:
                if enabled:
                    Check.enabled(locator=locator, element_path=element_path, element_name=element_name, index=index)
                else:
                    Check.disabled(locator=locator, element_path=element_path, element_name=element_name, index=index)

            if name is not None:
                Check.name(locator=locator, element_path=element_path, element_name=element_name, name=name, index=index)

            if text is not None:
                Check.text(locator=locator, element_path=element_path, element_name=element_name, text=text, index=index)

            if value is not None:
                Check.value(locator=locator, element_path=element_path, element_name=element_name, value=value, index=index)

            if attribute_type is not None and attribute_value is not None:
                Check.attribute(
                    locator=locator,
                    element_path=element_path,
                    element_name=element_name,
                    attribute_type=attribute_type,
                    attribute_value=attribute_value,
                    index=index
                )

    #------------------------------------------------- Visible / Invisible -------------------------------------------------
    # Visible
    @staticmethod
    @allure.step('✔ Check visible of {element_name}')
    def visible(
            locator: Locator,
            element_path: str,
            element_name: str,
            index: int = 0
    ):
        """
        ✔ Check visible [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name  (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index    (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - invisible!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - invisible!'
        expect(locator, error).to_be_visible()

    # Invisible
    @staticmethod
    @allure.step('✔ Check invisible of {element_name}')
    def invisible(
            locator: Locator,
            element_path: str,
            element_name: str,
            index: int = 0
    ):
        """
        ✔ Check invisible [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name      (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index     (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - invisible!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - invisible!'
        expect(locator, error).not_to_be_visible()

    #-------------------------------------------------- Enabled / Disabled -------------------------------------------------
    # Enabled
    @staticmethod
    @allure.step('✔ Check enabled of {element_name}')
    def enabled(
            locator: Locator,
            element_path: str,
            element_name: str,
            index: int = 0
    ):
        """
        ✔ Check enabled [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name      (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index     (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - disabled!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - disabled!'
        expect(locator, error).to_be_enabled()

    # Disabled
    @staticmethod
    @allure.step('✔ Check disabled of {element_name}')
    def disabled(
            locator: Locator,
            element_path: str,
            element_name: str,
            index: int = 0
    ):
        """
        ✔ Check disabled [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name      (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index     (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - enabled!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - enabled!'
        expect(locator, error).to_be_disabled()

    #-------------------------------------------------------- Name ---------------------------------------------------------
    # Name
    @staticmethod
    @allure.step('✔ Check name of {element_name}')
    def name(
            locator: Locator,
            element_path: str,
            element_name: str,
            name: str,
            index: int = 0
    ):
        """
        ✔ Check name of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name      (for logging)  (Ex: 'Description field']
        :param name: Element has name     (accessible)   (Ex: 'Description']
        :param index: DOM/nth - index     (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - incorrect name!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - incorrect name!'
        expect(locator, error).to_have_accessible_name(name)

    #-------------------------------------------------------- Text ---------------------------------------------------------
    # Text
    @staticmethod
    @allure.step('✔ Check text of {element_name}')
    def text(
            locator: Locator,
            element_path: str,
            element_name: str,
            text: str,
            index: int = 0
    ):
        """
        ✔ Check contain text of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name  (for logging)      (Ex: 'Description field']
        :param text: Text of element                     (Ex: 'Create course')
        :param index: DOM/nth - index    (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - incorrect text!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - incorrect text!'
        expect(locator, error).to_have_text(text)

    # Contain text
    @staticmethod
    @allure.step('✔ Check contain text of {element_name}')
    def contain_text(
            locator: Locator,
            element_path: str,
            element_name: str,
            text: str,
            index: int = 0
    ):
        """
        ✔ Check contain text of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name      (for logging)  (Ex: 'Description field']
        :param text: Part of the text                    (Ex: ...'ate cour'...)
        :param index: DOM/nth - index     (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - does not contain text!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - does not contain text!'
        expect(locator, error).to_contain_text(text)

    #-------------------------------------------------------- Value --------------------------------------------------------
    # Text
    @staticmethod
    @allure.step('✔ Check value of {element_name}]')
    def value(
            locator: Locator,
            element_path: str,
            element_name: str,
            value: str,
            index: int = 0
    ):
        """
        ✔ Check value of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name      (for logging)  (Ex: 'Description field']
        :param value: Value of element                   (Ex: 'This is my description in the field')
        :param index: DOM/nth - index     (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - incorrect value!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) - incorrect value!'
        expect(locator, error).to_have_value(value)

    #------------------------------------------------------ Attribute ------------------------------------------------------
    # Attribute
    @staticmethod
    @allure.step('✔ Check {attribute_type}-attribute value of {element_name}')
    def attribute(
            locator: Locator,
            element_path: str,
            element_name: str,
            attribute_type: str,
            attribute_value: str,
            index: int = 0):
        """
        ✔ Check attribute value of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element_name: Element name  (for logging)      (Ex: 'Description field']
        :param attribute_type: Attribute type            (Ex: 'href', 'placeholder', etc.)
        :param attribute_value: Attribute value          (Ex: '#/auth/registration', 'Enter description here', etc.)
        :param index: DOM/nth - index    (for logging)
        """
        if index == 0:
            error = f'❌ {element_path} > [{element_name}] - incorrect "{attribute_type}"-attribute value!'
        else:
            error = f'❌ {element_path} > [{element_name}] (index: {index}) incorrect "{attribute_type}"-attribute value!'
        expect(locator, error).to_have_attribute(attribute_type, attribute_value)

#=======================================================================================================================
