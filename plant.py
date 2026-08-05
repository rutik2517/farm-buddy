#!C:\Python312\python.exe
import cgi, cgitb
import mysql.connector
cgitb.enable()
import header

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
UserID = form.getvalue("UserID")

# Connect to DB
mydb = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="farm_buddy_db",
    ssl_disabled=True,
    use_pure=True
)
mycursor = mydb.cursor(dictionary=True)

# Fetch user info
mycursor.execute("SELECT * FROM register WHERE id=%s", (UserID,))
myResult = mycursor.fetchone()

# If form submitted with file
if "file" in form and form["file"].filename:
    email = form.getvalue("email")
    description = form.getvalue("Description")
    fileitem = form["file"]
    image_data = fileitem.file.read()

    # Save request
    sql = """INSERT INTO plant_requests (user_id, email, description, image)
             VALUES (%s, %s, %s, %s)"""
    values = (UserID, email, description, image_data)
    mycursor.execute(sql, values)
    mydb.commit()

    print(f"<h2>Plant request submitted successfully for {email}!</h2>")

else:
    # Show form
    print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Plant Detection</title>
<style>
body {{
    margin: 0;
    font-family: 'Segoe UI', Arial, sans-serif;
    background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
    color: #333;
}}
.container {{
    width: 100%;
    max-width: 650px;
    margin: 80px auto;
    text-align: center;
}}
.upload-box {{
    background: #ffffff;
    padding: 35px;
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}}
.upload-box:hover {{
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.2);
}}
input[type="file"], input[type="email"], input[type="text"] {{
    margin: 15px 0;
    padding: 12px;
    width: 90%;
    border: 2px dashed #28a745;
    border-radius: 8px;
    background: #f9fff9;
    cursor: pointer;
    transition: border-color 0.3s ease;
}}
input[type="file"]:hover, input[type="email"]:focus, input[type="text"]:focus {{
    border-color: #218838;
    outline: none;
}}
.btn {{
    background: linear-gradient(135deg, #28a745, #218838);
    color: white;
    border: none;
    padding: 14px 24px;
    font-size: 16px;
    border-radius: 10px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;
}}
.btn:hover {{
    background: linear-gradient(135deg, #218838, #1e7e34);
    transform: scale(1.05);
}}
</style>
</head>
<body>
<div class="container">
  <form action="plantBackEnd.py" method="POST" enctype="multipart/form-data">
        <div class="upload-box">
            <h2>Upload Plant Image</h2>
            <input type="file" id="plantphoto" name="plantphoto" required>
            <input type="email" id="email" name="email" value="{myResult['Email']}" readonly>
            <input type="text" id="description" name="Description" placeholder="Description" required>
            <br>
            <button type="submit" class="btn">Send for Identification</button>
        </div>
    </form>
</div>
</body>
</html>
""")
    