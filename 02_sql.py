# Insert Command

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("new.db")
cursor = conn.cursor()

# insert the data
query = " INSERT into population VALUES('New York City', 'NY', 8400000)"
cursor.execute(query)
query = " INSERT into population VALUES ('San Francisco','CA', 800000)"
cursor.execute(query)

# commit the changes
conn.commit()

# close the connection
conn.close()
