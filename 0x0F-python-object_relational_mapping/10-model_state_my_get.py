#!/usr/bin/python3
"""prints the first State object"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

if __name__ == "__main__":
    state_name = (sys.argv[4],)
    conn = engine.connect()
    s = select([State.id]).where( % s in State.name)
    r = conn.execute(s, state_name)
    print(r.fetchone())
