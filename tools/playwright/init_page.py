"""
Pages (helper)
"""
import allure
from playwright.sync_api import Playwright, StorageState, ViewportSize

from config import Browser, Dir, settings

#=======================================================================================================================
# Page for pytest fixture (helper)
def init_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_engine: Browser,
        storage_state: StorageState | None = None
):
    """
    Page for pytest fixture (helper)

    Launches the browser, creates a context (with or without Storage state),
    starts Tracing and yields the Page to the test. On teardown stops Tracing,
    attaches trace + video to Allure and closes the context/browser.

    Used in fixtures via ``yield from``::

        yield from init_playwright_page(
            playwright=playwright,
            test_name=request.node.name,
            browser_engine=request.param,
            storage_state=storage_state
        )

    :param playwright: Playwright (built-in fixture from pytest_playwright)
    :param test_name: Current test name (request.node.name) — for video/trace paths and Allure attachment names
    :param browser_engine: Browser engine [chromium] / [webkit] / [firefox]
    :param storage_state: Authorized state / None → guest context without authorization
    :return: yield page: Page
    """
    browser = playwright[browser_engine].launch(
        headless=settings.headless,
        slow_mo=settings.slow_mo
    )
    context = browser.new_context(
        base_url=settings.base_url,
        storage_state=storage_state,            # ┐
        # storage_state=Dir.STORAGE_STATE_FILE, # ┘
        locale='en-US',
        viewport=ViewportSize(width=1100, height=1200),
        record_video_dir=f'{Dir.VIDEOS}/{test_name}'
    )
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    page = context.new_page()
    # mock_static_resources(page)  # (optional)

    try:
        yield page

    finally:
        trace_path = f'{Dir.TRACING}/{test_name}.zip'
        try:
            context.tracing.stop(path=trace_path)
            allure.attach.file(
                source=trace_path,
                name=f'{test_name}_trace',
                attachment_type=allure.attachment_type.ZIP
            )

        finally:
            try:
                context.close()
            finally:
                browser.close()

            video = page.video
            if video:
                allure.attach.file(
                    source=video.path(),
                    name=f'{test_name}_video',
                    attachment_type=allure.attachment_type.WEBM
                )


#=======================================================================================================================
