"""
Mock
"""

from playwright.sync_api import Page, Route

#=======================================================================================================================

# v.1 Blocking resource loading (lambda)
def mock_static_resources(page: Page):
    """
    Blocks loading of static resources on the page (icons, images, video, audio, fonts)

    Used to speed up tests by avoiding unnecessary network load.

    :param page: Page on which static resource loading should be blocked
    """
    page.route('**/*.{ico,png,jpg,svg,webp,mp4,webm,ogg,mp3,woff,woff2}', lambda route: route.abort())


#-----------------------------------------------------------------------------------------------------------------------
# v.2 Blocking resource loading (with a message on each block)
def abort(route: Route):
    """
    Handler function for an intercepted request: logs the URL and aborts its loading

    :param route: Intercepted Playwright request (passed automatically by page.route)
    """
    print(f'\nAborting URL: {route.request.url}')   # For logging (Aborting URL: https://fonts.gstatic.com/s/roboto/v51/KFO7CnqEu92Fr1ME7kSn66aGLdTylUAMa3yUBHMdazQ.woff2)
    route.abort()                                   # Abort loading resource

def mock_static_resources_comment(page: Page):
    """
    Blocks loading of static resources on the page (icons, images, video, audio, fonts)

    Used to speed up tests by avoiding unnecessary network load.

    :param page: Page on which static resource loading should be blocked
    """
    page.route('**/*.{ico,png,jpg,svg,webp,mp4,webm,ogg,mp3,woff,woff2}', abort)

#=======================================================================================================================
