from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import base64
import json

def chatgpt(key: str, prompt: str):
    from openai import OpenAI
    client = OpenAI(api_key=key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ]
        )
    return response

app = FastAPI()



webui_path = "contents/webui"
app.mount(f"/{webui_path}/static", StaticFiles(directory=f"{webui_path}/static"), name="static")
templates = Jinja2Templates(directory=f"{webui_path}/template")


@app.get('/api', response_class=JSONResponse)
async def generator_API(requset: Request):
    print(requset.query_params)
    return 

@app.get('/', response_class=HTMLResponse)
async def root(request: Request, pompt: str | None):
    return templates.TemplateResponse('index.html', {"request": request, "client_ip": request.client.host})




