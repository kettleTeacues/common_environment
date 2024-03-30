# uvicorn main:app --reload
from fastapi import FastAPI

from routers import hello

app = FastAPI()
app.include_router(hello.router)

# CORSの設定
origins = [
    "http://localhost:3000",
]

@app.get("/")
def root():
    return {'status': 'OK'}