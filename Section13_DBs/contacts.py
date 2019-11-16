#!/usr/bin/env python3

"""
Example for SQL in python
"""

import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print each row
# for row in cursor:
#     print(row)

# unpack and print
# for name, phone, email in cursor:
#     print(name)
#     print(phone)
#     print(email)
#     print("-" * 20)

# print all rows in a list
# print(cursor.fetchall())

# print each row in an iterable manner
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

cursor.close()
db.commit()
db.close()
