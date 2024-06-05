from sqlalchemy import Integer, Column
from base import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, nullable=True, unique=True, primary_key=True, autoincrement=True)
