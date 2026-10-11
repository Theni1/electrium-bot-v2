from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore", hide_input_in_errors=True
    )

    openai_api_key: str
    database_url: str

    tavily_api_key: str | None = None
    discord_token: str | None = None
    discord_ask_channel_id: int | None = None
    discord_guild_id: int | None = None


settings = Settings()
