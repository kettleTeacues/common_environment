from sqlalchemy.orm import Session
from sqlalchemy import select

from db import engine
from models import Hello

def getHello():
    with Session(engine) as session:
        return session.execute(
            select(Hello)
        ).all()