import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response
from dependency.database import DatabaseHelper

description = """
Memory - нейросеть для гравировки
"""

app = FastAPI(
    title="XXXXXX",
    description=description,
    summary="XXXXXXXX",
    version="0.0.1",
    contact={
        "name": "XXXXX",
        "telegram": "XXXXXX"
    }
)
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

app.include_router()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = DatabaseHelper()
        response = await call_next(request)
    finally:
        await request.state.db.engine.dispose()
    return response


if __name__ == "__main__":
    # запуск сервера
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
