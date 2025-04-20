'''
파일명: main.py
'''
import uvicorn
from fastapi import FastAPI

app = FastAPI()


# 클라이언트에서 요청할 엔드포인트
#   base url -> GET www.naver.com/
@app.get("/")
def hello():
    return {"Hello": "FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
