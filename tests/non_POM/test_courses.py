"""
Test
Courses page is opening
"""
import pytest
from playwright.sync_api import expect

#=======================================================================================================================
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'

@pytest.mark.courses
@pytest.mark.regression
def test_courses_page_is_opening(chromium_page):
    page = chromium_page

    # ⿹ Open page
    page.goto(courses_url)

    # ㉧ LOCATORS
    courses_header = page.get_by_role(role='heading', name='Courses')
    folder_icon = page.get_by_test_id('courses-list-empty-view-icon')
    no_result = page.get_by_role(role='heading', name='There is no results')
    description = page.get_by_test_id('courses-list-empty-view-description-text')

    # ✔︎ EXPECTATIONS
    expect(page,'❌ Wrong page URL!').to_have_url(courses_url)
    expect(courses_header, '❌ Wrong page header text!').to_have_text('Courses')
    expect(folder_icon,'❌ Folder icon is invisible!').to_be_visible()
    expect(no_result, '❌ Wrong text!').to_have_text('There is no results')
    expect(description,'❌ Wrong description').to_have_text('Results from the load test pipeline will be displayed here')


    # ⏳
    page.wait_for_timeout(1000)
#=======================================================================================================================
