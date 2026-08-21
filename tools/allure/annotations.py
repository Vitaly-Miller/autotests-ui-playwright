"""
Allure Annotations + Enum
"""
from enum import StrEnum

#=======================================================================================================================
# ⚠️Python 3.11- ⮕ class ...(str, Enum):
# ⚠️Python 3.11+ ⮕ class ...(StrEnum):

#----------------------------------------------------- Allure Tags -----------------------------------------------------
# @allure.tag(Tag.<...>)
class Tag(StrEnum):
    AUTH = 'AUTHENTICATION'
    REGISTRATION = 'REGISTRATION'
    LOGIN = 'LOGIN'
    FILES = 'FILES'
    COURSES = 'COURSES'
    EXERCISES = 'EXERCISES'
    DASHBOARD = 'DASHBOARD'
    #------------------------
    REGRESSION = 'REGRESSION'
    SMOKE = 'SMOKE'
    NEGATIVE = 'NEGATIVE'
    VALIDATE = 'VALIDATE'
    #-------------------
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    NAVIGATE = 'NAVIGATE'
    #--------------------------
    PARAMETRIZE = 'PARAMETRIZE'
    UI = 'UI'


#---------------------------------------------- Allure Behaviors / Suites ----------------------------------------------
# @allure.epic() / @allure.parent_suite()
class Epic(StrEnum):
    AUTH = 'Authentication'
    DASHBOARD = 'Dashboard'
    COURSES = 'Courses'


# @allure.feature() / @allure.suite()
class Feature(StrEnum):
    LOGIN = 'Login feature'
    REGISTRATION = 'Registration feature'
    COURSES = 'Courses feature'
    EXERCISES = 'Exercises feature'
    DASHBOARD = 'Dashboard feature'


# @allure.story() / @allure.sub_suite()
class Story(StrEnum):
    # Positive scenario
    REGISTRATION = 'Registration'
    LOGIN = 'Login'
    COURSES = 'Courses'
    DASHBOARD = 'Dashboard'

    CREATE = 'Create'
    UPDATE = 'Update'       # Edit
    DELETE = 'Delete'
    NAVIGATE = 'Navigate'   # Redirect

    # Negative scenario
    REGISTRATION_NEGATIVE = 'Registration (negative)'
    LOGIN_NEGATIVE = 'Login (negative)'
    COURSES_NEGATIVE = 'Courses (negative)'
    DASHBOARD_NEGATIVE = 'Dashboard (negative)'
    CREATE_NEGATIVE = 'Create (negative)'
    UPDATE_NEGATIVE = 'Update (negative)'
    DELETE_NEGATIVE = 'Delete (negative)'
    NAVIGATE_NEGATIVE = 'Navigate (negative)'
    UI = 'UI'


#=======================================================================================================================
