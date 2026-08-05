#!C:\Python312\python.exe
import cgi
import cgitb
import os
import mysql.connector

cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

email = form.getvalue("email")
description = form.getvalue("Description")
fi=form["plantphoto"]
#print(fi.filename)
fn=os.path.splitext(fi.filename)
#print(fn[0])
uploudFileName='plant'+fn[1]
#print(uploudFileName)
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
query=f"INSERT INTO  plant (email,description,plantphoto) values ('{email}', '{description}', '{uploudFileName}')"""
#print(query)
mycursor.execute(query)
mydb.commit()
plant_id=mycursor.lastrowid
#print(plant_id)
upload_dir = f"""Plant/{plant_id}"""
#print(upload_dir)
os.makedirs(upload_dir, exist_ok=True)
file_path=os.path.join(upload_dir,uploudFileName)
open(file_path,'wb').write(fi.file.read())
print(f'''
    <script>alert(" Plant Add Successfully!");
    location.href="index.py";
    </script>''')
