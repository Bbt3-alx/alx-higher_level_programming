#!/usr/bin/python3
"""Python script that connect to a MySQL database"""


import MySQLdb
import sys


def list_states(username, password, db_name):
    """Conect tp the MySQL database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
            )
    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to list states
    list_states(username, password, db_name)
