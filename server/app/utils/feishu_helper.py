from app.common.config import Config
import lark_oapi as lark
from lark_oapi.api.translation.v1 import *

client = (
    lark.Client.builder()
    .app_id(Config.FEISHU_APP_ID)
    .app_secret(Config.FEISHU_APP_SECRET)
    .log_level(lark.LogLevel.DEBUG)
    .build()
)


def text_translate(source_language, text, target_language):
    # 构造请求对象
    request: TranslateTextRequest = (
        TranslateTextRequest.builder()
        .request_body(
            TranslateTextRequestBody.builder()
            .source_language(source_language)
            .text(text)
            .target_language(target_language)
            .glossary([])
            .build()
        )
        .build()
    )

    # 发起请求
    response: TranslateTextResponse = client.translation.v1.text.translate(request)

    # 处理失败返回
    # if not response.success():
    #     lark.logger.error(
    #         f"client.translation.v1.text.translate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}"
    #     )
    #     return response
    return response


def text_detect(text):
    # 构造请求对象
    request: DetectTextRequest = (
        DetectTextRequest.builder()
        .request_body(DetectTextRequestBody.builder().text(text).build())
        .build()
    )

    # 发起请求
    response: DetectTextResponse = client.translation.v1.text.detect(request)

    # 处理失败返回
    # if not response.success():
    #     lark.logger.error(
    #         f"client.translation.v1.text.detect failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}"
    #     )
    #     return response
    return response
