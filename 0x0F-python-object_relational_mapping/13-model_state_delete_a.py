#!/usr/bin/python3
"""delete all State objects containing 'a'"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, delete

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

if __name__ == "__main__":
    conn = engine.connect()
    rem = delete(State).where(State.name.like('%a%'))
    r = conn.execute(rem)
