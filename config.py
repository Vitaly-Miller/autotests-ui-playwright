"""
Project config (via Pydantic-settings)
"""

from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import StrEnum

#=======================================================================================================================
BASE_DIR = Path(__file__).parent                   # Base directory

#-------------------------------------------------- Settings Classes ---------------------------------------------------
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
    CHROMIUM = 'chromium' # Default
    CHROME = 'chrome'
    MSEDGE = 'msedge'


class TestUser(BaseModel):
    """
    Test user credentials (from .env)

    .
    """
    email: str
    username: str
    password: str

class TestData(BaseModel):
    """
    Static test data

    .
    """
    image_file_1: Path = BASE_DIR / 'testdata/files/image_1.jpg'
    image_file_2: Path = BASE_DIR / 'testdata/files/image_2.jpg'


#---------------------------------------------- MAIN Class + .env-config -----------------------------------------------
class Settings(BaseSettings):
    """
    Base project settings with .env-config

    .
    """
    model_config = SettingsConfigDict(        # CONFIG файла с переменными окружения (.env)
        extra='allow',                        # Разрешаем дополнительные переменные (например для CI) (optional)
        env_file=BASE_DIR / '.env',           # - Название файла с переменными окружения (.env)
        env_file_encoding='utf-8',            # - Кодировка файла с переменными окружения (.env)
        env_nested_delimiter='.'              # - Разделитель вложенных моделей в .env (ex. HTTPX_CLIENT.BASE_URL='...')
    )

    # Из .env (обязательные)
    base_url: str
    browser: Browser
    headless: bool
    slow_mo: int  # ms
    test_user: TestUser

    # Опциональные / с дефолтами
    chromium_channel: ChromiumChannel | None = None
    storage_state_file: Path = BASE_DIR / 'storage_state.json'
    test_data: TestData = TestData()
    tracing_dir: Path = BASE_DIR / 'tracing'
    video_dir: Path = BASE_DIR / 'videos'


#------------------------------------------------------ Helper ---------------------------------------------------------
settings = Settings()

#=======================================================================================================================
