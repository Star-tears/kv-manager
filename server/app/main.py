import argparse
import os

from app.common.config import Config
from app.core import db
from fastapi import FastAPI
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


def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--address", type=str, default="0.0.0.0", help="server listen address"
    )
    parser.add_argument("--port", type=int, default=11028, help="server listen port")
    parser.add_argument(
        "--webserver-path", type=str, default=".web-server", help="webserver path"
    )
    parser.add_argument(
        "--frontend-path", type=str, default="dist", help="frontend path"
    )
    args = parser.parse_args()
    Config.FRONTEND = os.path.join(args.frontend_path)
    Config.WEBSERVER = os.path.join(args.webserver_path)
    db.update_engine()
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        generate_unique_id_function=custom_generate_unique_id,
    )
    app.include_router(api_router, prefix=settings.API_V1_STR)
    app.mount(
        "/assets",
        StaticFiles(directory=os.path.join(Config.FRONTEND, "assets")),
        name="static",
    )
    templates = Jinja2Templates(directory=os.path.join(Config.FRONTEND))

    @app.get("/", response_class=HTMLResponse, tags=["index"])
    async def home(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    uvicorn.run(app, host=args.address, port=args.port, reload=False)


if __name__ == "__main__":
    main()
