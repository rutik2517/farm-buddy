#!C:\Python312\python.exe
import cgi 
import cgitb
cgitb.enable()
#import header
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
UserId = form.getvalue("UserId")
total_amount = form.getvalue("total_amount")
#UserID = int(UserID)
#total_amount = int(total_amount)
import mysql.connector
mydb = mysql.connector.connect(
    host="127.0.0.1",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",
    database="farm_buddy_db",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
mycursor=mydb.cursor()
query=f"""INSERT INTO ordermaster(UserId,total_amount)VALUES('{UserId}','{total_amount}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert("Book Order Successfully!");
    location.href="index.py";
    </script>''')