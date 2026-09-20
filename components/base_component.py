"""
BASE component
"""

import allure
from playwright.sync_api import Page, expect
from re import Pattern
from tools.logger import get_logger

#=======================================================================================================================
class BaseComponent:
    """
    Base component (page component)

    .
    """
    logger = get_logger('COMPONENT', True)

    def __init__(self, page: Page):
        self.page = page

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Current URL]
    def check_current_url(self, url: str | Pattern[str]):
        """
        ✔ Check [Current page URL]

        :param url: Expected page URL
        """
        step = f'✔ Check current page URL is {url}'
        error = '❌ Current page URL - incorrect!'
        with allure.step(step):
            self.logger.info(step)
            expect(self.page, error).to_have_url(url)
    #=======================================================================================================================
