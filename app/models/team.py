from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    league = Column(String, nullable=False)

    # Relationships
    players = relationship("Player", back_populates="team", cascade="all, delete-orphan")
    home_matches = relationship("Match", foreign_keys="[Match.home_team_name]", back_populates="home_team")
    away_matches = relationship("Match", foreign_keys="[Match.away_team_name]", back_populates="away_team")

    def __repr__(self):
        return f"<Team(name={self.name}, league={self.league})>"
