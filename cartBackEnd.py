#!C:\Python312\python.exe

import cgi
import cgitb
cgitb.enable()
import sys
sys.stdout.reconfigure(encoding='utf-8')
import mysql.connector
import header

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
UserID = form.getvalue("UserID")

# Database Connection
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="farm_buddy_db"
)

mycursor = mydb.cursor(dictionary=True)

# Fetch Cart Data
query = "SELECT * FROM cart WHERE UserID=%s"
mycursor.execute(query, (UserID,))
cart_data = mycursor.fetchall()

# Calculate Total
total_amount = 0
for item in cart_data:
    try:
        price = int(item['Price'])
        qty = int(item['Quantity'])
        total_amount += price * qty
    except:
        pass

# Fetch User Data
query2 = "SELECT * FROM register WHERE id=%s"
mycursor.execute(query2, (UserID,))
user = mycursor.fetchone()

# Handle None
if not user:
    user = {
        "Name": "",
        "Email": "",
        "FullName": "",
        "Address": "",
        "PhoneNo": "",
        "CardNo": ""
    }

print(f"""
<!DOCTYPE html>
<html>
<head>
<title>Checkout</title>

<style>
body {{
    font-family: Arial;
    background: #f2f2f2;
}}

.container {{
    width: 800px;
    margin: auto;
    background: white;
    padding: 20px;
    margin-top: 30px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px gray;
}}

h2 {{
    text-align: center;
}}

input {{
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid #ccc;
}}

.total {{
    font-size: 20px;
    font-weight: bold;
    color: green;
}}

button {{
    width: 100%;
    padding: 12px;
    background: green;
    color: white;
    border: none;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
}}

button:hover {{
    background: darkgreen;
}}

</style>
</head>

<body>
<br>
      <br>
      <br>
<div class="container">
<h2>Checkout Page</h2>

<h3>Billing Details</h3>

<input type="text" value="{user['Name']}" placeholder="Name">
<input type="text" value="{user['Email']}" placeholder="Email">

<input type="text" value="{user['Address']}" placeholder="Address">
<input type="text" value="{user['PhoneNo']}" placeholder="Phone">
<input type="text" value="{user['CardNo']}" placeholder="Card No">

<h3>Your Order</h3>

<p class="total">Total Amount: Rs. {total_amount}</p>

<br>

<a href="Order.py?UserID={UserID}&total_amount={total_amount}">
<button>Place Order</button>
</a>

</div>

</body>
</html>
""")
