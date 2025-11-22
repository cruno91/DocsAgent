from typing import Protocol, Iterable, List, Any, Optional, TypedDict, Literal


class ChatMessage(TypedDict):
    role: Literal["user", "assistant", "system"]
    content: str


class ChatModel(Protocol):
    """Synchronous chat completion interface."""

    def chat(
        self,
        messages: List[ChatMessage],
        temperature: float = 0.0,
        max_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> str:
        ...


class StreamingChatModel(Protocol):
    """Optional streaming interface."""

    def stream_chat(
        self,
        messages: List[ChatMessage],
        temperature: float = 0.0,
        max_tokens: Optional[int] = None,
        **kwargs: Any,
    ) -> Iterable[str]:
        ...