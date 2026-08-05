#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
import mysql.connector
form=cgi.FieldStorage()
#print(form)
id=form.getvalue("id")
#print(id)
#print(form)
Name=form.getvalue("Name")
#print(FirstName)

Email=form.getvalue("Email")
#print(Email)

FullName=form.getvalue("Name")
#print(FullName)

Address=form.getvalue("Address")
#print(Address)

Password=form.getvalue("Password")
#print(Password)
PhoneNo=form.getvalue("PhoneNo")
#print(Password)

CardNo=form.getvalue("CardNo")
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
query = f"""
UPDATE register 
SET 
    Name='{Name}',
    Email='{Email}',
    Password='{Password}',
    FullName='{FullName}',
    Address='{Address}',
    PhoneNo='{PhoneNo}',
    CardNo='{CardNo}'
WHERE Id={id}
"""
#print(query)   
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" data Update Successfully");
    location.href="index.py";
    </script>''')