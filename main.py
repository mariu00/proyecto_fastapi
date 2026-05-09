from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"ano_actual": datetime.now().year},
    )


@app.get("/recetas", response_class=HTMLResponse)
async def recetas(request: Request):
    return templates.TemplateResponse(
        request=request, name="recetas.html", context={"ano_actual": datetime.now().year},
    )


@app.get("/tips", response_class=HTMLResponse)
async def tips(request: Request):
    return templates.TemplateResponse(
        request=request, name="tips.html", context={"ano_actual": datetime.now().year},
    )
