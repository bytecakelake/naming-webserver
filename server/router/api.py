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
    generated = pd.DataFrame(columns=['prompt', 'nickname', 'explanation'], dtype=np.dtype('<U'))


async def nickname_generator(user_prompt: str):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": config.sysetem_prompt},
            { "role": "assistant","content": config.assistant_prompt},
            {"role": "user",  "content": user_prompt},
        ],
        temperature=1.2,
        max_tokens=config.ans_limit,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = response.choices[0].message.content.replace("\n\n", "\n").replace(": ", ":").split("\n")
    if len(content) != 2:
        print(" 비정상적인 생성기 응답감지. 다시 시도를 권장합니다.")
        print(content)
        return Response(status_code=500)
    nickname = content[1].split(":")[-1]
    if "(" in nickname and ")" in nickname:
        print("닉네임에 부가설명이 감지되어 제거하였습니다.")
        nickname = nickname.split("(")[0]
    explanation = content[0].split(":")[1]
    return {"nickname": nickname, "explanation": explanation}

@router.get('/generate', status_code=202)
async def generator_gate(request: Request, mode: str, prompt: str):
    
    if prompt == "":
        return Response(status_code=400)
    if mode == "nickname":
        content = await nickname_generator(prompt)
        #content = {"nickname": "테스트", "explanation": "테스트"}

        uuid = uuid1()
        Logs.generated.loc[uuid] = {"nickname": content["nickname"], "explanation": content["explanation"], "prompt": prompt}
        return {"uuid": uuid, "nickname": content["nickname"], "explanation": content["explanation"]}
    return Response(status_code=400)

@router.get('/search')
async def search(request: Request, uuid: UUID,):
    try:
        return Logs.generated.loc[uuid]
    except KeyError:
        return Response(status_code=404)

   
