#!C:\Python312\python.exe
import cgi
import cgitb
import mysql.connector
cgitb.enable()
print("Content-Type: text/html\n")
form=cgi.FieldStorage()
UserID = form.getvalue("UserID")
#print(UserID)
proid=form.getvalue('Id')
ProductName=form.getvalue('ProductName')
Price=form.getvalue('Price')
Quantity=form.getvalue("Quantity")

print(Quantity)
mydb = mysql.connector.connect(
    host="localhost",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",
    database="farm_buddy_db",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
mycursor=mydb.cursor(dictionary=True)
query=f"""INSERT INTO cart (proid,ProductName,Price,Quantity,UserID)VALUES('{proid}','{ProductName}','{Price}','{Quantity}','{UserID}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
print(f'''
    <script>alert(" add to cart Successfully!");
    location.href="cart.py?UserID={UserID}";
    </script>''')
 

