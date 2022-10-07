#!/usr/bin/python3
import MySQLdb
import sys
"""takes in an argument and displays all values in states where"""
"""name matches the argument"""


conn = MySQLdb.connect(host="localhost", user="root", port=3306,
                       passwd="password", db="hbtn_0e_0_usa")
cur = conn.cursor()
param = (sys.argv[4],)
cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", param)
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
conn.close()
