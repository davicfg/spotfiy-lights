from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from dotenv import load_dotenv


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")

@app.get("/callback")
def callback(request: Request):
    return {"call": "back"}


@app.get("/login")
def login(request: Request):
    return {"lo": "gin"}