from typing import List, Iterable, Optional, Any
import json
import requests

from core.settings import settings
from models.base import ChatMessage


class OllamaChatModel:
    """
    Thin wrapper around Ollama /api/chat endpoint.
    """

    def __init__(
        self,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = 60.0,
    ) -> None:
        self.base_url = (base_url or str(settings.OLLAMA_BASE_URL)).rstrip("/")
        self.model = model or settings.OLLAMA_MODEL
        self.timeout = timeout

    def chat(
        self,
        messages: List[ChatMessage],
        temperature: float = 0.0,
        max_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> str:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": temperature,
            },
        }

        if max_tokens is not None:
            payload["options"]["num_predict"] = max_tokens

        if "options" in kwargs:
            payload["options"].update(kwargs.pop("options"))

        url = f"{self.base_url}/api/chat"
        resp = requests.post(url, json=payload, timeout=self.timeout)
        resp.raise_for_status()
        data = resp.json()

        # Ollama /api/chat response format:
        # { "message": {"role": "...", "content": "..."}, ... }
        message = data.get("message") or {}
        return str(message.get("content", ""))

    def stream_chat(
        self,
        messages: List[ChatMessage],
        temperature: float = 0.0,
        max_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[str]:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": True,
            "options": {
                "temperature": temperature,
            },
        }

        if max_tokens is not None:
            payload["options"]["num_predict"] = max_tokens

        if "options" in kwargs:
            payload["options"].update(kwargs.pop("options"))

        url = f"{self.base_url}/api/chat"
        with requests.post(url, json=payload, stream=True, timeout=self.timeout) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if not line:
                    continue
                try:
                    data = json.loads(line.decode("utf-8"))
                except json.JSONDecodeError:
                    continue
                msg = data.get("message") or {}
                content = msg.get("content", "")
                if content:
                    yield content