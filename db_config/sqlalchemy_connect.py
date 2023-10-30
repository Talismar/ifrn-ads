from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.data.sqlalchemy_models import Base

DB_URL = "sqlite:///./sql_app.db"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
