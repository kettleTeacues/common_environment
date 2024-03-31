from sqlalchemy.orm import Session
from sqlalchemy import select

from db import engine
from models.starter import Hello

def getHello():
    with Session(engine) as session:
        res = session.execute(
            select(Hello)
        ).all()
        return [row[0] for row in res]