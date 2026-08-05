#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()

import mysql.connector

print("Content-Type: text/html\n")

# Get UserID
form = cgi.FieldStorage()
UserID = form.getvalue("UserID")

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="farm_buddy_db"
)

mycursor = mydb.cursor(dictionary=True)

# Safe query
query = "SELECT * FROM cart WHERE UserID=%s"
mycursor.execute(query, (UserID,))
myresult = mycursor.fetchall()

# Generate HTML items
tr_html = ''
total_amount = 0

if myresult:
    for x in myresult:
        # Safe value handling
        try:
            qty = int(x['Quantity']) if x['Quantity'] not in (None, 'None', '') else 0
        except:
            qty = 0

        try:
            price = int(x['Price']) if x['Price'] not in (None, 'None', '') else 0
        except:
            price = 0

        finalprice = qty * price
        total_amount += finalprice

        tr_html += f"""
        <div class="cart-item">
            <div class="item-info">
                <div class="item-header">
                    <div>
                        <p class="item-specs">ID: {x['Id']}</p>
                        <h3 class="item-name">{x['ProductName']}</h3>
                    </div>
                    <div class="item-price">Rs {price}</div>
                </div>

                <div class="item-controls">
                    <p>Qty: {qty}</p>
                    <p><b>Total: Rs {finalprice}</b></p>

                    <a href="cartDelete.py?Id={x['Id']}&UserID={UserID}" class="remove-btn">
                        Remove
                    </a>
                </div>
            </div>
        </div>
        """
else:
    tr_html = "<p style='padding:20px;'>Your cart is empty</p>"

item_count = len(myresult)

# HTML OUTPUT
print(f"""
<!DOCTYPE html>
<html>
<head>
<title>Cart Page</title>

<style>
body {{
    font-family: Arial;
    background: #f2f2f2;
}}

.container {{
    width: 900px;
    margin: auto;
}}

h1 {{
    text-align: center;
}}

.cart-item {{
    display: flex;
    background: white;
    margin: 15px 0;
    padding: 15px;
    border-radius: 10px;
}}

.item-info {{
    flex: 1;
}}

.item-header {{
    display: flex;
    justify-content: space-between;
}}

.item-name {{
    margin: 0;
}}

.item-price {{
    font-weight: bold;
}}

.item-controls {{
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
}}

.remove-btn {{
    color: red;
    text-decoration: none;
}}

.summary {{
    background: white;
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}}

.checkout-btn {{
    display: block;
    text-align: center;
    background: black;
    color: white;
    padding: 10px;
    text-decoration: none;
    margin-top: 15px;
}}
</style>

</head>

<body>

<div class="container">

<h1>Your Cart ({item_count} Items)</h1>

{tr_html}

<div class="summary">
    <h2>Total: Rs {total_amount}</h2>

    <a href="cartBackEnd.py?UserID={UserID}" class="checkout-btn">
        Checkout
    </a>
</div>

</div>

</body>
</html>
""")