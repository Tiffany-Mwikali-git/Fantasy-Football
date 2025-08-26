from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    goals = Column(Integer, default=0)

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    # Relationships
    team = relationship("Team", back_populates="players")

    def __repr__(self):
        return f"<Player(name={self.name}, position={self.position}, goals={self.goals})>"
