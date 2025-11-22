from pydantic import Field, AnyHttpUrl
from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    MODEL_BACKEND: Literal["ollama", "echo"] = Field(
        "ollama", description="LLM backend: ollama, echo (test)"
    )

    OLLAMA_BASE_URL: AnyHttpUrl = Field(
        "http://localhost:11434", description="Ollama HTTP endpoint"
    )
    OLLAMA_MODEL: str = Field(
        "llama3.1",
        description="Default Ollama model name",
    )

    class Config:
        env_prefix = "DOCSAGENT_"
        env_file = ".env"


settings = Settings()