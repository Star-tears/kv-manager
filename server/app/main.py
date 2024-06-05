import os
from app.common.config import Config
from app.core import db
from fastapi import FastAPI, File
from fastapi import FastAPI, Request
from fastapi.routing import APIRoute
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from app.api.main import api_router
from app.core.config import settings
from fastapi.staticfiles import StaticFiles
import mimetypes

mimetypes.init()
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("image/svg+xml", ".svg")


address = os.getenv("KV_SERVER_ADDRESS", "0.0.0.0")
port = int(os.getenv("KV_SERVER_PORT", 11028))


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


db.update_engine()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
)
app.include_router(api_router, prefix=settings.API_V1_STR)
app.mount(
    "/ts-flow/assets",
    StaticFiles(directory=os.path.join(Config.FRONTEND, "assets")),
    name="static",
)
templates = Jinja2Templates(directory=os.path.join(Config.FRONTEND))


@app.get("/", response_class=HTMLResponse, tags=["index"])
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/ts-flow", response_class=HTMLResponse, tags=["ts-flow"])
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/ts-flow/favicon.ico", tags=["favicon"])
async def favicon():
    # 这里假设你有一个放在static目录下的favicon.ico文件
    return File(
        os.path.join(Config.FRONTEND, "favicon.ico"),
        media_type="image/vnd.microsoft.icon",
    )


if __name__ == "__main__":
    uvicorn.run(app, host=address, port=port, reload=False)
