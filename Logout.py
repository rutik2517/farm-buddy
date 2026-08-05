#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
print("Content-Type: text/html\n")
print(f'''
    <script>
    localStorage.clear();
    alert(" Logout Successfully!");
    location.href="index.py";
    </script>''')