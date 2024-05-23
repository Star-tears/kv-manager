from pydantic import BaseModel


class BucketItemBase(BaseModel):
    bucketName: str


class KvItemBase(BucketItemBase):
    key: str
    value: str


class BucketFile(BucketItemBase):
    relativePath: str
