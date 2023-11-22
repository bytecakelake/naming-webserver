from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from openai import OpenAI
from common import config

def nickname_generatior(key: str, user_prompt: str):

    response = llm.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": config.base_prompt
        },
        {
        "role": "assistant",
        "content": "어떤 닉네임을 생성해 드릴까요?"
        },
        {
        "role": "user",
        "content": user_prompt
        },
    ],
    temperature=1.5,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response

llm = OpenAI(api_key=config.openai_api_key)
app = FastAPI()



webui_path = "contents/webui"
app.mount(f"/{webui_path}/static", StaticFiles(directory=f"{webui_path}/static"), name="static")
templates = Jinja2Templates(directory=f"{webui_path}/template")


@app.get('/api', response_class=JSONResponse)
async def generate(request: Request, user_prompt: str):
    return nickname_generatior(config.openai_api_key, user_prompt)

@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "client_ip": request.client.host})




