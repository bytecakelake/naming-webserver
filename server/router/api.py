from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from common import config

router = APIRouter(prefix='/api')



@router.get('/nickname', response_class=JSONResponse)
async def generate(request: Request, user_prompt: str):
    return nickname_generatior(config.openai_api_key, user_prompt)