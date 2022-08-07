#!/usr/bin/python3
import cgi
import cgitb
import sqlite3
import time
from http import cookies
import random
import os
# Enable error handling
cgitb.enable() 
# Make this an HTML file 
cookie = cookies.SimpleCookie()
cookie['lastvisit'] = str(time.time())

print ("Content-Type: text/html")
#print ("Set-Cookie:" + str(random.randint(1,1000000000)))
#print (cookie)
print ("")
"""
<!DOCTYPE html> 
<html> 
<head> 
<title>Data Entry Result</title> 
</head> 
<body>
"""
cookie_string = os.environ.get('HTTP_COOKIE')
if not cookie_string:
    print ('<h1>First visit or cookies disabled</h1>')

else: # Run the page twice to retrieve the cookie
    #print ('<p>The returned cookie string was "' + cookie_string + '"</p>')

    # load() parses the cookie string
    cookie.load(cookie_string)
    # Use the value attribute of the cookie to get it
    lastvisit = float(cookie['lastvisit'].value)

    print ('<p>Your last visit was at',)
    print (time.asctime(time.localtime(lastvisit)), '</p>')
# Get form data: 
form_data = cgi.FieldStorage() 
# If not all of the fields are filled out, print an error message: 
if "username" not in form_data or "password" not in form_data:
    print ("Please fill in both username and password.")
else:
    # Get the username and password:
    user_name = form_data["username"].value
    pass_word = form_data["password"].value
    # Create a tuple containing both the first and password:
    person = (user_name, pass_word)
# Connect to the database:
    conn = sqlite3.connect("../registration/webapps.db")
    cursor = conn.cursor()
# Check if this person is already in the database:
    cursor.execute("SELECT * FROM login WHERE username=? AND password=?", person)
    person_from_data = cursor.fetchone()
# If the person is not in the database, output an error message.
    if person_from_data == None:
        print ("The user", user_name, "was not found in the database. Please try again or sign up for a new account.")
    # Otherwise, print a success message:
    else:
        print ("Welcome", user_name, ".You have logged in successfully")
    # Close database
        conn.close() 
# Finally, end the HTML page: 
"""
</body> 
</html>
"""
