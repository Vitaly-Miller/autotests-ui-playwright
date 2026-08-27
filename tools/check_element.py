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
            element: str,
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
        :param element: Element name      (for logging)  (Ex: 'Description field']
        :param visible: True/False
        :param enabled: True/False                       (Active for action)
        :param name: Element has name     (accessible)   (Ex: 'Description')
        :param text: Element has a text                  (Ex: 'Create course')
        :param value: Value of element                   (Ex: 'This is my description in the field')
        :param attribute_type: Element has an attribute  (Ex: 'href', 'placeholder', etc.)
        :param attribute_value: Value of attribute       (Ex: '#/auth/registration', 'Enter description here', etc.)
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check [{element}]'):
            if visible:
                Check.visible(locator=locator, element_path=element_path, element=element, index=index)
            else:
                Check.invisible(locator=locator, element_path=element_path, element=element, index=index)

            if enabled is not None:
                if enabled:
                    Check.enabled(locator=locator, element_path=element_path, element=element, index=index)
                else:
                    Check.disabled(locator=locator, element_path=element_path, element=element, index=index)

            if name is not None:
                Check.name(locator=locator, element_path=element_path, element=element, name=name, index=index)

            if text is not None:
                Check.text(locator=locator, element_path=element_path, element=element, text=text, index=index)

            if value is not None:
                Check.value(locator=locator, element_path=element_path, element=element, value=value, index=index)

            if attribute_type is not None and attribute_value is not None:
                Check.attribute(
                    locator=locator,
                    element_path=element_path,
                    element=element,
                    attribute_type=attribute_type,
                    attribute_value=attribute_value,
                    index=index
                )

    #------------------------------------------------- Visible / Invisible -------------------------------------------------
    # Visible
    @staticmethod
    def visible(
            locator: Locator,
            element_path: str,
            element: str,
            index: int = 0
    ):
        """
        ✔ Check visible [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name  (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index    (for logging)
        """
        with allure.step(f'✔ Check visible [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - invisible!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - invisible!'
            expect(locator, error).to_be_visible()

    # Invisible
    @staticmethod
    def invisible(
            locator: Locator,
            element_path: str,
            element: str,
            index: int = 0
    ):
        """
        ✔ Check invisible [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name      (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check invisible [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - invisible!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - invisible!'
            expect(locator, error).not_to_be_visible()

    #-------------------------------------------------- Enabled / Disabled -------------------------------------------------
    # Enabled
    @staticmethod
    def enabled(
            locator: Locator,
            element_path: str,
            element: str,
            index: int = 0
    ):
        """
        ✔ Check enabled [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name      (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check enabled [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - disabled!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - disabled!'
            expect(locator, error).to_be_enabled()

    # Disabled
    @staticmethod
    def disabled(
            locator: Locator,
            element_path: str,
            element: str,
            index: int = 0
    ):
        """
        ✔ Check disabled [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name      (for logging)  (Ex: 'Description field']
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check disabled [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - enabled!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - enabled!'
            expect(locator, error).to_be_disabled()

    #-------------------------------------------------------- Name ---------------------------------------------------------
    # Name
    @staticmethod
    def name(
            locator: Locator,
            element_path: str,
            element: str,
            name: str,
            index: int = 0
    ):
        """
        ✔ Check name of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name      (for logging)  (Ex: 'Description field']
        :param name: Element has name     (accessible)   (Ex: 'Description']
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check name of [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - incorrect name!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - incorrect name!'
            expect(locator, error).to_have_accessible_name(name)

    #-------------------------------------------------------- Text ---------------------------------------------------------
    # Text
    @staticmethod
    def text(
            locator: Locator,
            element_path: str,
            element: str,
            text: str,
            index: int = 0
    ):
        """
        ✔ Check contain text of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name  (for logging)      (Ex: 'Description field']
        :param text: Text of element                     (Ex: 'Create course')
        :param index: DOM/nth - index    (for logging)
        """
        with allure.step(f'✔ Check text of [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - incorrect text!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - incorrect text!'
            expect(locator, error).to_have_text(text)

    # Contain text
    @staticmethod
    def contain_text(
            locator: Locator,
            element_path: str,
            element: str,
            text: str,
            index: int = 0
    ):
        """
        ✔ Check contain text of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name      (for logging)  (Ex: 'Description field']
        :param text: Part of the text                    (Ex: ...'ate cour'...)
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check contain text of [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - does not contain text!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - does not contain text!'
            expect(locator, error).to_contain_text(text)

    #-------------------------------------------------------- Value --------------------------------------------------------
    # Text
    @staticmethod
    def value(
            locator: Locator,
            element_path: str,
            element: str,
            value: str,
            index: int = 0
    ):
        """
        ✔ Check value of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name      (for logging)  (Ex: 'Description field']
        :param value: Value of element                   (Ex: 'This is my description in the field')
        :param index: DOM/nth - index     (for logging)
        """
        with allure.step(f'✔ Check value of [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - incorrect value!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) - incorrect value!'
            expect(locator, error).to_have_value(value)

    #------------------------------------------------------ Attribute ------------------------------------------------------
    # Attribute
    @staticmethod
    def attribute(
            locator: Locator,
            element_path: str,
            element: str,
            attribute_type: str,
            attribute_value: str,
            index: int = 0):
        """
        ✔ Check attribute value of [Element]

        :param locator: Locator
        :param element_path: Element path (for logging)  (Ex: 'Create course page > Exercises > Exercise > Form')
        :param element: Element name  (for logging)      (Ex: 'Description field']
        :param attribute_type: Attribute type            (Ex: 'href', 'placeholder', etc.)
        :param attribute_value: Attribute value          (Ex: '#/auth/registration', 'Enter description here', etc.)
        :param index: DOM/nth - index    (for logging)
        """
        with allure.step(f'✔ Check "{attribute_type}"-attribute value of [{element}]'):
            if index == 0:
                error = f'❌ {element_path} > [{element}] - incorrect "{attribute_type}"-attribute value!'
            else:
                error = f'❌ {element_path} > [{element}] (index: {index}) incorrect "{attribute_type}"-attribute value!'
            expect(locator, error).to_have_attribute(attribute_type, attribute_value)

#=======================================================================================================================
