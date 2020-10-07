from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Member(Base) :
    __tablename__ = 'member'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    qty = Column(Integer, nullable=False)

    def __repr__(self):
        return '<UserModel model {}>'.format(self.id)