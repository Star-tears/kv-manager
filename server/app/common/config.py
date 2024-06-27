from dotenv import load_dotenv
import os

# 加载.env文件，如果存在的话
load_dotenv(".env", override=False)  # 设置override=False表示环境变量优先
active_env = os.getenv("ACTIVE_ENV", "prod")
load_dotenv(f".env.{active_env}", override=False)


class Config:
    FRONTEND = os.path.join("dist")
    WEBSERVER = os.path.join(".web-server")
    FEISHU_APP_ID: str = None
    FEISHU_APP_SECRET: str = None


Config.WEBSERVER = os.getenv("KV_WEBSERVER_PATH", ".web-server")
Config.FRONTEND = os.getenv("KV_FRONTEND_PATH", "dist")
Config.FEISHU_APP_ID = os.getenv("FEISHU_APP_ID")
Config.FEISHU_APP_SECRET = os.getenv("FEISHU_APP_SECRET")
