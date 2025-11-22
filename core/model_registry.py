from core.settings import settings
from models.base import ChatMessage
from models.ollama import OllamaChatModel


class EchoChatModel:
    """Tiny test backend that just echoes the last user message."""

    def chat(
        self,
        messages: list[ChatMessage],
        temperature: float = 0.0,
        max_tokens: int | None = None,
        **kwargs,
    ) -> str:
        for msg in reversed(messages):
            if msg["role"] in ("user", "assistant"):
                return f"[echo] {msg['content']}"
        return "[echo] (no content)"

    def stream_chat(
        self,
        messages: list[ChatMessage],
        temperature: float = 0.0,
        max_tokens: int | None = None,
        **kwargs,
    ):
        yield self.chat(messages, temperature=temperature, max_tokens=max_tokens, **kwargs)


def get_chat_model() -> OllamaChatModel | EchoChatModel:
    backend = settings.MODEL_BACKEND.lower()

    if backend == "ollama":
        return OllamaChatModel(
            base_url=str(settings.OLLAMA_BASE_URL),
            model=settings.OLLAMA_MODEL,
        )

    if backend == "echo":
        return EchoChatModel()

    raise ValueError(f"Unsupported MODEL_BACKEND: {settings.MODEL_BACKEND!r}")
