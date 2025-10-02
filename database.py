from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# apne PostgreSQL ka connection string lagao
DATABASE_URL = DATABASE_URL = "postgresql://postgres:%40Ayushi1610@localhost/myproject"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
