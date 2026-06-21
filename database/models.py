from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Text

from database.db import Base

class Prediction(Base):
    __tablename__="predictions"
    id=Column(
        Integer,
        primary_key=True,
        index=True
    )
    prediction=Column(String)
    fraud_probability=Column(Float)
    risk_score=Column(Integer)
    risk_category=Column(String)
    reasons=Column(Text)
    
