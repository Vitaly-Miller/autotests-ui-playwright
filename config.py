"""
Project config
"""

from pathlib import Path
from enum import StrEnum
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

#=======================================================================================================================
class Dir:
    """
    Directories & files

    .
    """
    # Directories
    BASE_DIR = Path(__file__).parent      # 🗂️Project ROOT (Base directory)
    TESTDATA = BASE_DIR / 'testdata'      # ├─ 📁testdata/
    FILES = TESTDATA / 'files'            # │  └─ 📁files/
    TRACING = BASE_DIR / 'tracing'        # ├─ 📁tracing/
    VIDEOS = BASE_DIR / 'videos'          # └─ 📁videos/
    # Files
    STORAGE_STATE_FILE = BASE_DIR / 'storage_state.json'

class Endpoint(StrEnum):
    """
    Endpoints

    .
    """
    REGISTRATION = '#/auth/registration'
    LOGIN = '#/auth/login'
    DASHBOARD = '#/dashboard'
    COURSES = '#/courses'
    CREATE_COURSE = f'{COURSES}/create'


class TestUser(BaseModel):
    """
    Test user credentials — from .env

    .
    """
    email: str
    username: str
    password: str


class Browser(StrEnum):
    """
    Browser (Engine)

    playwright.[BROWSER].launch()

    - chromium - Chromium
    - firefox  - Firefox
    - webkit   - Safari
    """
    CHROMIUM = 'chromium'
    FIREFOX = 'firefox'
    WEBKIT = 'webkit'

class ChromiumChannel(StrEnum):
    """
    Chromium channel (UI)

    playwright.chromium.launch(channel=[CHANNEL])

    - chromium - Chromium (default)
    - chrome   - Google Chrome
    - msedge   - Microsoft Edge
    """
    CHROMIUM = 'chromium'
    CHROME = 'chrome'
    MSEDGE = 'msedge'


#-----------------------------------------------------------------------------------------------------------------------
class Settings(BaseSettings):
    """
    Project settings - from .env

    .
    """
    model_config = SettingsConfigDict(
        env_file=Dir.BASE_DIR / '.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
        extra='ignore',
    )

    base_url: str
    browser: list[Browser]
    headless: bool
    slow_mo: int  # ms
    test_user: TestUser
    chromium_channel: ChromiumChannel | None = None    # ⚠ закомментировать в .env при webkit / firefox


settings = Settings()

#=======================================================================================================================
