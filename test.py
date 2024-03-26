from typing import Annotated

import fastapi
from fastapi import Request, Form
from fastapi.templating import Jinja2Templates

app = fastapi.FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,name="fio.html"
    )


@app.post("/")
async def get_data(fio: Annotated[str, Form()], email: Annotated[str, Form()], phone: Annotated[int, Form()]):
    with open("file.csv", "a") as f:
        f.write(f"\n{fio}\t{email}\t{phone}")
    return "OK"
