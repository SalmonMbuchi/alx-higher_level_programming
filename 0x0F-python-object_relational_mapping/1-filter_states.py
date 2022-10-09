#!/usr/bin/python3
"""lists all states with a name starting with N from the database"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name FROM states \
        WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
