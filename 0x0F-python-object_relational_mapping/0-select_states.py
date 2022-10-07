#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
"""connect to database, list states and close the connection"""
conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                       passwd="password", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
conn.close()
