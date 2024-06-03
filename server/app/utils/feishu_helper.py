# import lark_oapi as lark
# from lark_oapi.api.translation.v1 import *

# client = (
#     lark.Client.builder()
#     .app_id(Config.FEISHU_APP_ID)
#     .app_secret(Config.FEISHU_APP_SECRET)
#     .log_level(lark.LogLevel.DEBUG)
#     .build()
# )


# def text_translate(source_language, text, target_language):
#     # 构造请求对象
#     request: TranslateTextRequest = (
#         TranslateTextRequest.builder()
#         .request_body(
#             TranslateTextRequestBody.builder()
#             .source_language(source_language)
#             .text(text)
#             .target_language(target_language)
#             .glossary([])
#             .build()
#         )
#         .build()
#     )

#     # 发起请求
#     response: TranslateTextResponse = client.translation.v1.text.translate(request)

#     # 处理失败返回
#     # if not response.success():
#     #     lark.logger.error(
#     #         f"client.translation.v1.text.translate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}"
#     #     )
#     #     return response
#     return response


# def text_detect(text):
#     # 构造请求对象
#     request: DetectTextRequest = (
#         DetectTextRequest.builder()
#         .request_body(DetectTextRequestBody.builder().text(text).build())
#         .build()
#     )

#     # 发起请求
#     response: DetectTextResponse = client.translation.v1.text.detect(request)

#     # 处理失败返回
#     # if not response.success():
#     #     lark.logger.error(
#     #         f"client.translation.v1.text.detect failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}"
#     #     )
#     #     return response
#     return response

import json
from app.common.config import Config
import requests


def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {"app_id": Config.FEISHU_APP_ID, "app_secret": Config.FEISHU_APP_SECRET}

    response = requests.post(url, headers=headers, json=data)
    return json.loads(response.text)["tenant_access_token"]


def text_detect(text):
    url = "https://open.feishu.cn/open-apis/translation/v1/text/detect"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + get_tenant_access_token(),
    }
    data = {"text": text}

    response = requests.post(url, headers=headers, json=data)
    return json.loads(response.text)["data"]["language"]


if __name__ == "__main__":
    print(get_tenant_access_token())
    print(text_detect("你好"))
