from fastapi import FastAPI
from .core.app import create_app
from .api.v1.hello import router as hello_router

app: FastAPI = create_app()
app.include_router(hello_router, prefix="/v1")
