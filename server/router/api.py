from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse
from uuid import uuid1, UUID
import pandas as pd
from core.bot.naming import Nicus
from pydantic import BaseModel


bot = Nicus()
router = APIRouter(prefix="/api", default_response_class=JSONResponse, tags=["api"])

class Log:
    name = pd.DataFrame(columns=['prompt', 'name', 'description'])

class GetNameModel(BaseModel):
    prompt: str

@router.post('/generate/{language}/name', status_code=202)
async def naming(language:str, item: GetNameModel):
    if language not in ['en', 'ko']:
        return Response(status_code=404)
    if language == 'en':
        language = 'english'
    elif language == 'ko':
        language = 'Korean'
    content = bot.generate(item.prompt, language)['content']
    content['uuid'] = str(uuid1())
    content['prompt'] = item.prompt
    return content


   
