#!/usr/bin/python3
"""prints all City objects"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, select

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

if __name__ == "__main__":
    conn = engine.connect()
    s = select([State.name, City.id, City.name]).select_from(
        City.join(State)
    r=conn.execute(s)
    for row in r.fetchall():
        print(row)
