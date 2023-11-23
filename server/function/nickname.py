from openai import OpenAI
from common import config

def nickname_generatior(key: str, user_prompt: str):
    llm = OpenAI(api_key=config.openai_api_key)
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
    max_tokens=config.ans_limit,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response