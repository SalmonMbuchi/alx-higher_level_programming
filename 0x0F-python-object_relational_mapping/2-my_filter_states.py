#!/usr/bin/python3
"""takes in an argument and displays all values in states where"""
"""name matches the argument"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    param = (sys.argv[4],)
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", param)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
