from pydantic import BaseModel


class BucketItemBase(BaseModel):
    bucketName: str


class KvItemBase(BucketItemBase):
    key: str


class KvItem(KvItemBase):
    value: str


class BucketFile(BucketItemBase):
    relativePath: str


class RenameBucketItem(BucketItemBase):
    newBucketName: str
