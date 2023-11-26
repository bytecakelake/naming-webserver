#-*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from pydantic import BaseModel, Base64Encoder
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uuid import uuid4
from router import api
from common import config
import base64


# FastAPI 세팅 {docs_url&redoc_url: API 문서 경로, favicon:웹페이지 아이콘 경로, default_response_class: 기본 응답 형식}
app = FastAPI(docs_url="/api/docs", redoc_url=None, favicon=None, default_response_class=HTMLResponse )



#라우터 등록
#app.include_router(api.router)

# jinja2 템플릿 세팅
app.mount(f"/{config.webui_path}/static", StaticFiles(directory=f"{config.webui_path}/static"), name="static")
templates = Jinja2Templates(directory=f"{config.webui_path}/template")

# 에러 핸들러
@app.middleware("http")
async def resoponse_error_handler(request: Request, call_next):
    response = await call_next(request) # 다음 미들웨어 또는 라우터로 넘어감

    status_code = response.status_code
    if status_code == 404: # 존재하지 않는 페이지
        return templates.TemplateResponse('error.html', {"request": request, "status_code": status_code}, status_code=status_code)
        
    return response
    

# 메인 페이지
@app.get('/')
async def root(request: Request, content: str = ""):
    print(content)
    return templates.TemplateResponse('index.html', {"request": request,"client_ip": request.client.host})

@app.get('/encode/{path}/a')
async def root(request: Request, path: str):
    return f"{path}"
@app.get('/{path}')
async def root(request: Request, path: str):
    return RedirectResponse(url=f'/encode/{base64.b64encode(path.encode("utf-8")).decode("utf-8")}/a')


