from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Base for models
Base = declarative_base()

# Create engine
engine = create_engine("sqlite:///fantasy_football.db", echo=False)

# Session factory
SessionLocal = sessionmaker(bind=engine)

# Get a session
def get_session():
    return SessionLocal()

# Initialize database (create tables)
def init_db():
    from app.models import match, players, team  # import models so they register
    Base.metadata.create_all(bind=engine)
