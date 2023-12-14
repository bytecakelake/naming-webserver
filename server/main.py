#-*- coding: utf-8 -*-
from fastapi import FastAPI, Request, Response, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import api
from common import config
from uuid import UUID, uuid4
import httpx


# FastAPI 세팅 {docs_url&redoc_url: API 문서 경로, favicon:웹페이지 아이콘 경로, default_response_class: 기본 응답 형식}
app = FastAPI(docs_url="/api/docs", redoc_url=None, favicon=None, default_response_class=HTMLResponse )



#라우터 등록
app.include_router(api.router)

# jinja2 템플릿 세팅
app.mount(f"/{config.webui_path}/static", StaticFiles(directory=f"{config.webui_path}/static"), name="static")
templates = Jinja2Templates(directory=f"{config.webui_path}/dynamic")



# 메인 페이지
@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('main.html', {"request": request})

@app.get('/docs')
async def license(request: Request):
    return templates.TemplateResponse('infomation.html', {"request": request})
