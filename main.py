'''
파일명: main.py
'''
from urllib.request import Request

import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from user.interface.controllers.user_controller import router as user_router
from containers import Container

app = FastAPI()

app.include_router(user_router)
app.container = Container() # 애플리케이션을 구동할 때 앞에서 작성한 설정을 등록한다.


# 설정 변경하기
# 유효성 검사 에러 코드를 422에서 400으로 변경하기 - 파이단틱 에러 코드 버그
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content=exc.errors()
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
