#!/usr/bin/python3
"""lists all cities"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT  cities.id, cities.name, states.name\
        FROM cities INNER JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id")
    for city in cur.fetchall():
        print(city)
    cur.close()
    conn.close()
