#!/usr/bin/python3
import cgi
import cgitb
import sqlite3
# Enable error handling
cgitb.enable() 
# Make this an HTML file 
print ("Content-Type: text/html")
print ("")
"""
<!DOCTYPE html> 
<html> 
<head> 
<title>Registration</title> 
</head> 
<body>
"""
# Get form data: 
form_data = cgi.FieldStorage() 
# If not all of the fields are filled out, print an error message: 
if "username" not in form_data or "password" not in form_data:
    print ("Please fill in both username and password.")
else:
    # Get the user name and password:
    user_name = form_data["username"].value
    pass_word = form_data["password"].value
    # Create a tuple containing both the first and last name:
    person = (user_name, pass_word)
# Connect to the database:
    conn = sqlite3.connect("../registration/webapps.db")
    cursor = conn.cursor()
# Check if this person is already in the database:
    cursor.execute("SELECT * FROM login WHERE username=? AND password=?", person)
    person_from_data = cursor.fetchone()
# If the person is already in the database, print an error message.
    if person_from_data != None:
        print (user_name, pass_word, "is already in the database.")
    # Otherwise, insert the login into the database# and print a success message:
    else:
        cursor.execute("INSERT INTO login (username, password) VALUES (?, ?)", person)
        print (user_name, pass_word, "was successfully entered into the database.")
     # Save changes to database
        conn.commit()
     # Close database
        conn.close() 
# Finally, end the HTML page: 
"""
</body> 
</html>
"""
