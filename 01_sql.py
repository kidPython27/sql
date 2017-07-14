# 01.sql.py
# import sqlite library
import sqlite3 

# create a new database if the database doensnt already exist
conn = sqlite3.connect("new.db")


# get a cursor object to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute(""" CREATE TABLE population(city TEXT, state TEXT, population INT )""")

# clsoe the database connection
conn.close()



