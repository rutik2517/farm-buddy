#!C:\Python312\python.exe
import cgi
import cgitb
import header
cgitb.enable()
import mysql.connector
#print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
UserID=form.getvalue("UserID")
#print(UserID)
mydb = mysql.connector.connect(
    host="localhost",  # IMPORTANT: use IP, not 'localhost'
    port="3306",
    user="root",
    password="",  
    database="farm_buddy_db",
    ssl_disabled=True,  # disables SSL completely (recommended for local dev)
    use_pure=True
)
mycursor = mydb.cursor(dictionary=True) 

query=f""" SELECT * FROM register  WHERE id='{UserID}' """

#print(query)
mycursor.execute(query)
myResult=mycursor.fetchone()
#print(myResult)
print("""
<!DOCTYPE html>
<html>
<head>
<title>Register Form</title>
<style>
body{font-family:Arial;background:#f3f4f6;}
.form-box{
    width:400px;
    margin:50px auto;
    background:white;
    padding:20px;
    border-radius:10px;
    box-shadow:0 0 10px #ccc;
}
input,button{
    width:100%;
    padding:10px;
    margin:8px 0;
}
button{
    background:black;
    color:white;
    border:none;
    cursor:pointer;
}
</style>
</head>
""")
print(f"""
<body>

<div class="form-box">
<h2>User Registration</h2>

<form action="register_save.py" method="post">
<input type="text" name="id"  id="id" value="{myResult['Id']}" style="display:none;">
<input type="text" style="border: 1px solid black;" name="Name" id="Name" value="{myResult['Name']}" placeholder="Name" >

<input type="email" name="Email" id="Email" value="{myResult['Email']}" readonly>


<input type="password" style="border: 1px solid black;" name="Password" id="Password" value="{myResult['Password']}" >



<input type="text" style="border: 1px solid black;" name="Address" id="Address" value="{myResult['Address']}" placeholder="Address" >
<input type="text" style="border: 1px solid black;" name="PhoneNo" id="PhoneNo" value="{myResult['PhoneNo']}"  placeholder="PhoneNo">
<input type="text" style="border: 1px solid black;" name="CardNo" id="CardNo" value="{myResult['CardNo']}" placeholder="CardNo" >

<button type="submit">Register Now</button>

</form>
</div>

</body>
</html>
""")




