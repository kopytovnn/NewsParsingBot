from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import *
from models.user import *

engine = create_engine("sqlite:///Data.db")
Base.metadata.create_all(engine)