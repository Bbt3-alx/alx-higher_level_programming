#!/usr/bin/python3
""" A script that list all states """


import sys
import MySQLdb


def list_states_with_N(username, password, db_name):
    """a script that lists all states with a name starting with N"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )
    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main.__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states with_n(username, password, db_name)
