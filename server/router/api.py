from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from uuid import uuid1, UUID
from common import config
import pandas as pd
import numpy as np
from openai import OpenAI



router = APIRouter(prefix="/api", default_response_class=JSONResponse, tags=["api"])
openai = OpenAI(api_key=config.openai_api_key)

class Logs:
    generated = pd.DataFrame(columns=["id", 'user_prompt', 'nickname', 'explanation'], dtype=np.dtype('<U'))

@router.get('/openai/test')
async def nickname_generator(user_prompt: str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": config.sysetem_prompt},
            { "role": "assistant","content": config.assistant_prompt},
            {"role": "user",  "content": user_prompt},
        ],
        temperature=1.5,
        max_tokens=config.ans_limit,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response

@router.get('/generate')
async def generate(request: Request, user_prompt: str, none_preprossing: bool = False):
    #아무것도 입력하지 않았을 경우
    if user_prompt == "":
        return Response(status_code=400)
    #response = nickname_generator(user_prompt)

    nickname = "abc님"
    explanation = "당신의 이름입니다."
    uuid = uuid1()
    Logs.generated.loc[len(Logs.generated)+1] = [uuid, user_prompt, nickname, explanation]
    return {"uuid": uuid, "nickname": nickname, "explanation": explanation}
    

@router.get('/search')
async def search(request: Request, id: UUID,):
    response = Logs.generated.loc[Logs.generated['id'] == id]
    if len(response) == 0:
        return Response(status_code=404)
    else:
        return response.iloc[0]
   
