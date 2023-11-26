
# 서버 설정
adress = "127.0.0.1" 
port = 5000
debug = False
webui_path = "database/webui"

# OPENAI 설정
ans_limit = 200
openai_api_key_path = "common/openai_api_key.txt"
sysetem_prompt_path = "database/prompt/nickname/default-v2-kr.txt"
assist_prompt = "어떤 닉네임을 생성해 드릴까요?"


# 파일 읽기
openai_api_key = open(openai_api_key_path, "r", encoding="utf-8").read()
sysetem_prompt = open(sysetem_prompt_path, "r", encoding="utf-8").read()
