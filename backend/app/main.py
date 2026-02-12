from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.routers import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # URL вашего React приложения
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)