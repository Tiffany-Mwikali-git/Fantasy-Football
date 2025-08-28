from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    score = Column(String, nullable=True)

    home_team = Column(Integer, ForeignKey("teams.name"), nullable=False)
    away_team = Column(Integer, ForeignKey("teams.name"), nullable=False)

    # Relationships
    home_team = relationship("Team", foreign_keys=[home_team.name], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team.name], back_populates="away_matches")

    def __repr__(self):
        return f"<Match(date={self.date}, score={self.score}, home={self.home_team.name}, away={self.away_team.name})>"
