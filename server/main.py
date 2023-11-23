from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from router import api
from common import config


app = FastAPI()

app.include_router(api.router)


app.mount(f"/{config.webui_path}/static", StaticFiles(directory=f"{config.webui_path}/static"), name="static")





@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "client_ip": request.client.host})




