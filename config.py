"""
Project config (via Pydantic-settings)
"""

from pathlib import Path
from pydantic import BaseModel, EmailStr, HttpUrl, FilePath     # validators
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import StrEnum

#================================================== Settings Classes ===================================================
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
    Test User

    .
    """
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    """
    Test Data

    .
    """
    image_file_1: FilePath
    image_file_2: FilePath


#---------------------------------------------- MAIN Class + .env-config -----------------------------------------------
class Settings(BaseSettings):
    """
    Base project settings with .env-config

    .
    """
    # .env-config
    model_config = SettingsConfigDict(        # CONFIG файла с переменными окружения (.env)
        extra='allow',                        # Разрешаем дополнительные переменные (например для CI) (optional)
        env_file='.env',                      # - Название файла с переменными окружения (.env)
        env_file_encoding='utf-8',            # - Кодировка файла с переменными окружения (.env)
        env_nested_delimiter='.'              # - Разделитель вложенных моделей в .env (ex. HTTPX_CLIENT.BASE_URL='...')
    )

    # Атрибуты c валидацией
    base_url: HttpUrl
    browser: Browser
    chromium_channel: ChromiumChannel | None = None
    headless: bool
    slow_mo: int  # mc
    storage_state_file: FilePath
    test_user: TestUser
    test_data: TestData
    tracing_dir: Path
    video_dir: Path

    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┐
    # Использовать, если base_url: HttpUrl
    @property
    def base_url_str(self) -> str:
        """
        HttpUrl —> 'str'

        Использовать, если base_url: HttpUrl (Pydantic-аннотация)

        :return: Base URL (string)
        """
        return str(self.base_url)
    # ╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴╴┘

#------------------------------------------------------ Helper ---------------------------------------------------------
settings = Settings()


#=======================================================================================================================
