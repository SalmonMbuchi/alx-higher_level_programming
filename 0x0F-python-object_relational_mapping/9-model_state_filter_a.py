#!/usr/bin/python3
"""lists all objects that contain the letter a"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).order_by(State.id)\
        .filter(State.name.like("%a%")).all()
    for obj in res:
        print(f"{obj.id}: {obj.name}")
