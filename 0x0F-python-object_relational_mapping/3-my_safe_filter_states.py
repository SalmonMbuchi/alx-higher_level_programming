#!/usr/bin/python3
"""prevent sql injection attack"""
import sys
from functools import partial
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    tup = (sys.argv[4],)
    query = """SELECT * FROM states WHERE name = %s"""
    cur.execute(query, tup)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
