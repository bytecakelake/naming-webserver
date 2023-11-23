from fastapi.templating import Jinja2Templates
from common import config


def __self__():
    templates = Jinja2Templates(directory=f"{config.webui_path}/template")