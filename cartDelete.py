#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
Id=form.getvalue("Id")
UserID = form.getvalue("UserID")
#print(Id)
mydb = mysql.connector.connect(
    host="localhost",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",  
    database="farm_buddy_db",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
mycursor=mydb.cursor()
query=f""" Delete From cart where Id={Id}"""
#print(query)
mycursor.execute (query)
mydb.commit()
print(f'''
    <script>alert(" cart item Delete  Successfully!");
    location.href="cart.py?UserID={UserID}";
    </script>''')
 
