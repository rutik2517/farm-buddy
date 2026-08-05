#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)

#print(form)
Name=form.getvalue("Name")
#print(FirstName)

Email=form.getvalue("Email")
#print(Email)

Password=form.getvalue("Password")
#print(Password)



mydb = mysql.connector.connect(
    host="localhost",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",
    database="farm_buddy_db",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
#print(mydb)
mycursor=mydb.cursor()


query=f"INSERT INTO register (Name,Email,Password) values ('{Name}','{Email}','{Password}')"""
#print(query)   
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" user add  Successfully");
    location.href="sigup.py";
    </script>''')