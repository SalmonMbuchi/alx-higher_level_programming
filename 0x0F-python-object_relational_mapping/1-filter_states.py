#!/usr/bin/python3
"""lists all states with a name starting with N from the database"""


import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", port=3306,
                       passwd="password", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT DISTINCT id, name FROM states
            WHERE name LIKE 'N%' ORDER BY id ASC")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
conn.close()
