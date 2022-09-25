from sqlalchemy import Column, String, Numeric, Integer

from database import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String, index=True)
    price = Column(String)
    departure = Column(String)
    duration = Column(String)
    emission = Column(String)