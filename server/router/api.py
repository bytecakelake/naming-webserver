from typing import Any
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from common import config
import pandas as pd
import time

class GenerateFrame(BaseModel):
    uid: int
    id: int
    user_prompt: str | None = None
    nickname: str | None = None
    explanation: str | None = None
    model: str = "gpt-3.5-turbo"

class GenerateData:
    columns=['uid', 'id', 'user_prompt', 'nickname', 'explanation', 'model']
    def __init__(self):
            self.Frame = pd.DataFrame(data=[], columns=self.columns)
            self.last_gid = 0
    def load(self):
        self.Frame = pd.read_csv(config.data_path, index_col=0)
        self.last_gid = len(self.Frame) + 1

    def __call__(self,  page: int | None = None, size: int | None = None, start:int | None = None, end: int | None = None):
        if start is None:
            start = (page-1)*size
        if end > page*size or end is None:
            end = page*size
        if end > len(self.Frame):
            end = len(self.Frame)
        print(self.Frame)
        return self.Frame[start:end]
    def add(self, data: GenerateFrame):
        #row =pd.DataFrame(data=[[data.uid, self.last_gid, data.user_prompt, data.nickname, data.explanation, data.model]], columns=self.columns)
        pd.concat([self.Frame, data[self.columns]], ignore_index=True)

router = APIRouter(prefix='/api', default_response_class=JSONResponse, tags=['api'])

data = GenerateData()


async def ummm(t):
    time.sleep(t)
    return "ummm"

@router.get('/nickname/generate')
async def generate(request: Request, user_prompt: str):
    nickname = user_prompt + "님"
    data.add({"uid" :1, "user_prompt":"any", "nickname": nickname, "explanation": "is GOD"})
    return {"nickname": nickname}
    

@router.get('/nickname/search')
async def search(request: Request, uid: str = 1, page: int = 1, size: int = 1):
    
    return data(page=page, size=size)
