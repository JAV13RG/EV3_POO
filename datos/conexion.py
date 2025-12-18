from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

DATABASE_URL = (
    f"mysql+mysqlconnector://{config('user')}:{config('password')}"
    f"@{config('server')}:{config('port')}/{config('database')}"
)

motor_db = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=motor_db, autoflush=False, autocommit=False)

def get_session():
    """Crea una sesión nueva por operación (evita sesiones cerradas/reutilizadas)."""
    return SessionLocal()
