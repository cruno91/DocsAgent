from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(title="AI Docs", version="0.1.0")
    return app
