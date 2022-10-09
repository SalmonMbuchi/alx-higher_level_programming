#!/usr/bin/python3
"""lists all cities"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = """SELECT cities.name\
      FROM cities INNER JOIN states\
      ON cities.state_id = states.id\
      WHERE states.name = %s"""
    tup = (sys.argv[4],)
    cur.execute(query, tup)
    city = cur.fetchall()
    string = ', '.join(''.join(tup) for tup in city)
    print(string)
    cur.close()
    conn.close()
