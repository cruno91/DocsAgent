from fastapi import APIRouter, HTTPException

from core.model_registry import get_chat_model          # your registry with config switching
from models.base import ChatMessage

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"message": "hello world"}

@router.get("/llm-test")
async def llm_test():
    llm = get_chat_model()

    messages: list[ChatMessage] = [
        {
            "role": "system",
            "content": "You are a simple ping model. Reply with a short confirmation.",
        },
        {
            "role": "user",
            "content": "Say: LLM connection OK.",
        },
    ]

    try:
        answer = llm.chat(messages)
    except Exception as exc:
        # if Ollama isn't running / bad URL, you’ll see it here
        raise HTTPException(status_code=500, detail=f"LLM call failed: {exc!s}")

    return {
        "backend": "configured",   # could also expose settings.MODEL_BACKEND
        "ok": True,
        "answer": answer,
        "provider": llm.base_url,
        "model": llm.model,
    }