# uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

# CORSの設定
origins = [
    "http://localhost:3000",
]

@app.get("/")
def root():
    return {'status': 'OK'}