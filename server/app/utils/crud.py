from app.models.sql_models import KvData, KvRecord
from sqlmodel import Session, and_, select, delete
from sqlalchemy.exc import NoResultFound


def get_kv(session: Session, bucketName: str) -> KvData:
    statement = select(KvData).where(KvData.bucket == bucketName)
    result = session.execute(statement)
    return result.all()


def upsert_kv(session: Session, key: str, value: str, bucketName: str) -> KvData:
    statement = select(KvData).where(
        and_(KvData.key == key, KvData.bucket == bucketName)
    )
    try:
        kv = session.scalars(statement).one()
        kv.value = value
        kv.bucket = bucketName
    except NoResultFound:
        kv = KvData(key=key, value=value, bucket=bucketName)
    session.merge(kv)
    session.commit()
    create_kv_record(session, kv)
    return kv


def create_kv_record(session: Session, kv_data: KvData) -> KvRecord:
    statement = select(KvRecord).where(
        and_(
            KvRecord.key == kv_data.key,
            KvRecord.value == kv_data.value,
            KvRecord.updated_at == KvRecord.updated_at,
            KvRecord.bucket == kv_data.bucket,
        )
    )
    try:
        kv_record = session.scalars(statement).one()
    except NoResultFound:
        kv_record = KvRecord(
            key=kv_data.key,
            value=kv_data.value,
            updated_at=kv_data.updated_at,
            bucket=kv_data.bucket,
        )
        session.add(kv_record)
        session.commit()


def delete_kv(session: Session, key: str, bucketName: str) -> None:
    statement = select(KvData).where(
        and_(KvData.key == key, KvData.bucket == bucketName)
    )
    kv_data = session.scalars(statement).one()
    session.delete(kv_data)
    session.commit()
    delete_kv_record(session, key, bucketName)


def delete_kv_record(session: Session, key: str, bucketName: str) -> None:
    statement = delete(KvRecord).where(
        and_(KvRecord.key == key, KvRecord.bucket == bucketName)
    )
    session.execute(statement)
    session.commit()


def delete_bucket(session: Session, bucketName: str) -> None:
    delete_kv = delete(KvData).where(KvData.bucket == bucketName)
    session.execute(delete_kv)
    delete_kv_record = delete(KvRecord).where(KvRecord.bucket == bucketName)
    session.execute(delete_kv_record)
    session.commit()