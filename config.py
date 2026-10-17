"""
Project config
"""
from enum import StrEnum
from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from tools.data_generator import fake

#=======================================================================================================================
class Dir:
    """
    Directories & files

    .
    """
    # Directories
    BASE_DIR = Path(__file__).parent                      # 🗂️Project ROOT (Base directory)
    TESTDATA = BASE_DIR / 'testdata'                      # ├─ 📁testdata/
    FILES = TESTDATA / 'files'                            # │  └─ 📁files/
    TRACING = BASE_DIR / 'tracing'                        # ├─ 📁tracing/
    VIDEOS = BASE_DIR / 'videos'                          # ├─ 📁videos/
    ALLURE_RESULTS = BASE_DIR / 'allure-results'          # ├─ 📁allure-results/
    # Files
    STORAGE_STATE_FILE = BASE_DIR / 'storage_state.json'  # └─ storage_state.json

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
    email: str = Field(default_factory=fake.email)
    username: str = Field(default_factory=fake.username)
    password: str = Field(default_factory=fake.password)

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


#----------------------------------------------------- RUN Settings ----------------------------------------------------
class Settings(BaseSettings):
    """
    Project run settings - from .env

    .
    """
    model_config = SettingsConfigDict(
        env_file=Dir.BASE_DIR / '.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
        extra='ignore'
    )

    base_url: str
    browser: list[Browser]
    headless: bool
    slow_mo: int                                    # ms
    test_user: TestUser = Field(default_factory=TestUser)   # or use manual mode via .env


settings = Settings()
#=======================================================================================================================
