#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
#print("Content-Type: text/html\n")

import header
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
mycursor=mydb.cursor(dictionary=True)
query=f""" SELECT * FROM product """
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchall()
#print(myresult)
tr_html=''
for x in myresult :
    tr_html += f"""
 <div class="box">
       <img src="html/ltr/Product/{x['Id']}/{x['Photo']}" alt="" >
            <h3>{x['ProductName']}<h3>
            <div class="price">Rs-{x['Price']}</div>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
      <p>{x['Description']} </p>
            <a href="product_detils.py?Id={x['Id']}" class="btn">add to cart</a>
        </div>

       
      


       
    """
print(f"""
   <br> <br> <br> <br>


    <section class="learn" id="learn">
      <h1 class="heading">our <span>products</span></h1>

      <div class="box-container">
        

       
      
      
       {tr_html}
      </div>
       
    </section>
    <!--learn section ends-->
""")
import footer