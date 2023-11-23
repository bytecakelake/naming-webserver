
adress = "127.0.0.1" 
port = 5000
debug = False
webui_path = "database/webui"

ans_limit = 200
openai_api_key_path = "common\openai_api_key.txt"
base_prompt_path = "nickname_prompts/prompt-1.txt"



openai_api_key = open(openai_key_path, "r").read()
base_prompt = open(base_prompt_path, "r").read()