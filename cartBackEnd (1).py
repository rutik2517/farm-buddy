#!C:\Python312\python.exe

import cgi
import cgitb
import mysql.connector

cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
UserId = form.getvalue("UserId")

# ✅ Safety check
if not UserId:
    print("<h3>Error: UserId missing</h3>")
    exit()

# ✅ Database connection
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="farm_buddy_db"
)

# ✅ Cursor
cursor = mydb.cursor(dictionary=True)

# ✅ Get cart data (SAFE QUERY)
query = "SELECT * FROM cart WHERE UserId=%s"
cursor.execute(query, (UserId,))
cart_data = cursor.fetchall()

# ✅ Calculate total
total_amount = 0
for item in cart_data:
    price = int(item['Price'])
    qty = int(item['Quantity'])
    total_amount += price * qty

# ✅ Get user details
query_user = "SELECT * FROM register WHERE Id=%s"
cursor.execute(query_user, (UserId,))
user = cursor.fetchone()

# अगर user नहीं मिला
if not user:
    print("<h3>User not found</h3>")
    exit()

# ✅ Output HTML
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
    margin: 50px auto;
    background: white;
    padding: 20px;
    border-radius: 10px;
}}

h2 {{
    text-align: center;
}}

input {{
    width: 100%;
    padding: 10px;
    margin: 10px 0;
}}

.btn {{
    background: green;
    color: white;
    padding: 10px;
    border: none;
    width: 100%;
}}
</style>
</head>

<body>

<div class="container">

<h2>Checkout</h2>

<h3>User Details</h3>

<label>Name</label>
<input type="text" value="{user['Name']}" readonly>

<label>Email</label>
<input type="text" value="{user['Email']}" readonly>

<h3>Total Amount: ₹{total_amount}</h3>

<br>

<a href="Order.py?UserId={UserId}&total_amount={total_amount}">
<button class="btn">Place Order</button>
</a>

</div>

</body>
</html>
""")