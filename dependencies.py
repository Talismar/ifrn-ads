from db_config.sqlalchemy_connect import SessionFactory

def database_session():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()