#!/usr/bin/python3
"""change the name of a State object"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select, update

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

if __name__ == "__main__":
    conn = engine.connect()
    upd = update(State).where(State.id == 2).values(name='New Mexico')
    r = conn.execute(upd)
