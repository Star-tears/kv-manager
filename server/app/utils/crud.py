from datetime import datetime
from app.models.sql_models import KvData, KvId, KvRecord, Language
from sqlmodel import Session, and_, select, delete, update, alias
from sqlalchemy.orm import aliased
from sqlalchemy.exc import NoResultFound


def create_lang(session: Session, lang: str) -> Language:
    statement = select(Language).where(Language.lang == lang)
    result = session.exec(statement).all()
    if len(result) == 0:
        new_lang = Language(lang=lang)
        session.add(new_lang)
        session.commit()
        session.refresh(new_lang)
        return new_lang
    else:
        return result[0]


def get_lang_list(session: Session) -> list[Language]:
    statement = select(Language)
    result = session.exec(statement).all()
    return result


def upsert_kv(
    session: Session,
    key: str,
    value: str,
    lang_key: str,
    lang_value: str,
    kv_id: int = None,
):
    if kv_id is not None:
        kv_update = upsert_kv_data(
            session, KvData(value=value, language=lang_value, kv_id=kv_id)
        )
    else:
        statement = select(KvData).where(
            and_(KvData.value == key, KvData.language == lang_key)
        )
        try:
            kv = session.scalars(statement).one()
            kv_update = upsert_kv_data(
                session, KvData(value=value, language=lang_value, kv_id=kv.kv_id)
            )
        except NoResultFound:
            kvid = create_kvid(session)
            upsert_kv_data(session, KvData(value=key, language=lang_key, kv_id=kvid.id))
            kv_update = upsert_kv_data(
                session, KvData(value=value, language=lang_value, kv_id=kvid.id)
            )
    return kv_update


def upsert_kv_data(session: Session, kv_data: KvData):
    statement = select(KvData).where(
        and_(KvData.language == kv_data.language, KvData.kv_id == kv_data.kv_id)
    )
    try:
        kv = session.scalars(statement).one()
        if kv.value != kv_data.value:
            kv.updated_at = datetime.now()
            kv.value = kv_data.value
            create_kv_record(session, kv)
    except NoResultFound:
        kv = KvData(
            value=kv_data.value,
            language=kv_data.language,
            kv_id=kv_data.kv_id,
            updated_at=datetime.now(),
        )
        session.add(kv)
        create_kv_record(session, kv)
    session.merge(kv)
    session.commit()
    session.refresh(kv)
    return kv


def create_kvid(session: Session) -> KvId:
    new_kv_id = KvId()
    session.add(new_kv_id)
    session.commit()
    session.refresh(new_kv_id)
    return new_kv_id


def get_kv(session: Session, lang_key: str, lang_value: str):
    B1 = aliased(KvData)
    B2 = aliased(KvData)
    query = (
        select(
            KvId.id,
            B1.value.label("key"),
            B2.value.label("value"),
            B1.language.label("lang_key"),
            B2.language.label("lang_value"),
        )
        .outerjoin(B1, (KvId.id == B1.kv_id) & (B1.language == lang_key))
        .outerjoin(B2, (KvId.id == B2.kv_id) & (B2.language == lang_value))
    )

    # 执行查询并获取结果
    results = session.exec(query).all()
    results_dict = [row._asdict() for row in results]
    return results_dict


def create_kv_record(session: Session, kv_data: KvData):
    statement = select(KvRecord).where(
        and_(
            KvRecord.language == kv_data.language,
            KvRecord.value == kv_data.value,
            KvRecord.updated_at == kv_data.updated_at,
            KvRecord.kv_id == kv_data.kv_id,
        )
    )
    try:
        kv_record = session.scalars(statement).one()
    except NoResultFound:
        kv_record = KvRecord(
            language=kv_data.language,
            value=kv_data.value,
            updated_at=kv_data.updated_at,
            kv_id=kv_data.kv_id,
        )
        session.add(kv_record)
        session.commit()


def get_kv_record(session: Session, lang_value: str, kv_id: int):
    statement = select(KvRecord).where(
        and_(KvRecord.language == lang_value, KvRecord.kv_id == kv_id)
    )
    result = session.exec(statement).all()
    return result


def delete_kv(session: Session, kv_id: int):
    kv_to_delete = session.exec(select(KvId).where(KvId.id == kv_id)).first()
    if kv_to_delete:
        # 由于设置了Relationship和外键约束，删除KvId时应级联删除关联的KvData和KvRecord
        session.delete(kv_to_delete)
        session.commit()
        return f"KvId {kv_id} and associated KvData and KvRecord deleted successfully"
    else:
        return f"No KvId found with id {kv_id}"
