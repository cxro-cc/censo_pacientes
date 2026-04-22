"""
database.py — Conexión a PostgreSQL y gestión de sesiones con SQLAlchemy.
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# En desarrollo local carga .env, en producción usa variables de Railway
load_dotenv(encoding='utf-8')

DATABASE_URL = os.getenv("DATABASE_URL")

# Validar que DATABASE_URL existe
if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL no está configurada. "
        "En desarrollo local, verifica tu archivo .env. "
        "En producción, configura las variables de entorno en Railway."
    )

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    """Clase base de la que heredan todos los modelos ORM."""
    pass


def get_db():
    """
    Dependencia de FastAPI: entrega una sesión de DB y la cierra al terminar la petición.
    Uso: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    """Clase base de la que heredan todos los modelos ORM."""
    pass


def get_db():
    """
    Dependencia de FastAPI: entrega una sesión de DB y la cierra al terminar la petición.
    Uso: db: Session = Depends(get_db)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
