#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
Email=form.getvalue("Email")
#print(Email)
Password=form.getvalue("Password")
#print(Password)
mydb = mysql.connector.connect(
    host="127.0.0.1",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",
    database="farm_buddy_db",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
mycursor = mydb.cursor()
query=f""" SELECT * FROM register WHERE Email='{Email}' AND Password='{Password}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
if mycursor.rowcount==1:
    id=myresult[0]
    Name=myresult[1]
    print(f'''
    <script>
    localStorage.clear();
    localStorage.setItem("id","{id}");
    localStorage.setItem("FirstName","{Name}");
    alert(" Login Successfully!");
    location.href="index.py";
    </script>''')
else:
    print(f'''
    <script>alert(" Login Unsuccessfully!");
    location.href="sigup.py";
    </script>''')