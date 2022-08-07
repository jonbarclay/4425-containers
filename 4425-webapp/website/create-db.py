#!/usr/bin/python3
#Python code start 
''' 
The following is not a CGI script. 
The following is simply a Python script that is used to create the database. 
It should be run once before running the server in order to create the database.  
''' 
import sqlite3 
# Create webapps.db file in registration folder. 
conn = sqlite3.connect("registration/webapps.db")
cursor = conn.cursor() 
# Create the login table. 
cursor.execute("CREATE TABLE login (username text, password text)") 
# Save changes to database
conn.commit()
# Close database
conn.close() 
# Copy end here
