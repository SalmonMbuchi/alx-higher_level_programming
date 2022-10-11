#!/usr/bin/python3
"""add Louisiana to the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, insert, select

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

if __name__ == "__main__":
    conn = engine.connect()
    ins = insert(State).values(name='Louisiana')
    r = conn.execute(ins)
    sel = select([State.id]).where(State.name == 'Louisiana')
    r = conn.execute(sel)
    print(r.fetchone())
