#!/usr/bin/python3
"""print the State object with the name passed as argument"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    found = False
    for state in session.query(State):
        if State.name == sys.argv[4]:
            print(f"{State.id}")
            found = True
            break
    if found is False:
        print('Not found')
