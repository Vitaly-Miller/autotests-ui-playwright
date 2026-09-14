"""
Base page
(Page object model)
"""

from playwright.sync_api import Page, expect
from re import Pattern
import allure
from tools.logger import get_logger

#=======================================================================================================================
class BasePage:                                          # Родительский класс
    logger = get_logger('PAGE    ', True)  # Logger (название и отображение в консоли)

    def __init__(self, page: Page):                      # Конструктор класса, принимающий page
        self.page = page

    # --------------------------------------------------- ▶ ACTIONS ----------------------------------------------------
    # Open page
    def open(self, url: str):
        """
        ⿹ Open page

        - ▶ Open page

        :param url: Page URL
        """
        step = f'⿹ Open page URL: {url}'
        with allure.step(step):
            self.logger.info(step)
            self.page.goto(url=url)

    # Reload page
    def reload(self):
        """
        ↺ Reload current page

        .
        """
        step = f'↻ Reload page URL: {self.page.url}'
        with allure.step(step):
            self.logger.info(step)
            self.page.reload()

    # Wait (timeout)
    def wait(self, timeout: int = 2):
        """
        Wait (timeout) sec

        :param timeout: Timeout in sec (2 sec by default)
        """
        step = f'... wait {timeout} sec'
        with allure.step(step):
            self.logger.info(step)
            self.page.wait_for_timeout(timeout * 1000)

    # ------------------------------------------------- ✔️EXPECTATIONS -------------------------------------------------
    # [Current URL] - ⚠️Дублирование из BaseComponent
    def check_current_url(self, url: str | Pattern[str]):
        """
        ✔ Check [Current page URL]

        :param url: Expected page URL
        """
        step = f'✔ Check current page URL is "{url}"'
        error = '❌ Current page URL - incorrect!'
        with allure.step(step):
            self.logger.info(step)
            expect(self.page, error).to_have_url(url)

#=======================================================================================================================
