import fastapi
from fastapi import Request
from fastapi.templating import Jinja2Templates

app = fastapi.FastAPI()
templates = Jinja2Templates(directory="templates")
counter = 0
products = [
    "Яблоки", "Вишня", "Хлеб", "Яйца", "Молоко"
]


@app.get("/")
async def root(request: Request):
    global counter
    counter += 1
    return templates.TemplateResponse(
        request=request, name="index.html", context={"counter": counter}
    )


@app.get("/search")
async def search(query: str, request: Request):
    result = list(filter(lambda i: query in i, products))
    return templates.TemplateResponse(
        request=request, name="search.html", context={"result": result}
    )

