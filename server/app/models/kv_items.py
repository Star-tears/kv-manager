from pydantic import BaseModel


class KvIdItem(BaseModel):
    kvId: int


class KvItemBase(BaseModel):
    key: str
    langKey: str


class KvItem(KvItemBase):
    value: str
    langValue: str
    kvId: int | None = None


class KvRecordItem(BaseModel):
    langValue: str
    kvId: int


class LangKv(BaseModel):
    langKey: str
    langValue: str


class LanguageItemBase(BaseModel):
    lang: str
