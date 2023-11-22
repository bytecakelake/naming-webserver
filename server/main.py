from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import base64
import json

class Conents(BaseModel):
    befoe_request: json
    uid: int
    after_request: json


app = FastAPI()



webui_path = "contents/webui"
app.mount(f"/{webui_path}/static", StaticFiles(directory=f"{webui_path}/static"), name="static")
templates = Jinja2Templates(directory=f"{webui_path}/template")

@app.middleware("http")
async def base64_conversion(request: Request, next_prosess):
    print(request.query_params.count('content'))
    response = await next_prosess(request)
    return response

@app.get('/api', response_class=JSONResponse)
async def generator_API(requset: Request):
    print(requset.query_params)
    return 

@app.get('/', response_class=HTMLResponse)
async def root(request: Request, uid: int | None):
    return templates.TemplateResponse('index.html', {"request": request, "uid": uid})




