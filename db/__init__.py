from os import getenv
from typing import Any

from sqlalchemy import create_engine, func, desc, and_, or_
from sqlalchemy.orm import (
    Session,
    sessionmaker,
    relationship,
    backref,
    object_session,
    deferred,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.attributes import flag_modified

uri = getenv("DATABASE_URL").replace("postgres://", "postgresql://", 1)
if "sqlite:" in getenv("DATABASE_URL"):
    uri += "?check_same_thread=False"
DB_ENGINE = create_engine(uri)
del uri

DB_SES_LOCAL = sessionmaker(bind=DB_ENGINE, autoflush=False)
DB_BASE = declarative_base()


def get_db():
    db = DB_SES_LOCAL()
    try:
        yield db
    finally:
        db.close()


from .models import *

DB_BASE.metadata.create_all(DB_ENGINE)
