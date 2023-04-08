from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

DATABASE_URL = "sqlite:///flights.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()


class Airport(Base):
    __tablename__ = "airports"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    icao = Column(String(4), unique=True, nullable=False)


class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True)
    flight_number = Column(String, nullable=False)
    tod = Column(DateTime, nullable=False)
    toa = Column(DateTime, nullable=False)
    departure_airport_id = Column(Integer, ForeignKey('airports.id'), nullable=False)
    arrival_airport_id = Column(Integer, ForeignKey('airports.id'), nullable=False)

    departure_airport = relationship("Airport", foreign_keys=[departure_airport_id])
    arrival_airport = relationship("Airport", foreign_keys=[arrival_airport_id])


Base.metadata.create_all(engine)
