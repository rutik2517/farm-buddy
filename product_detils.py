#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
import mysql.connector
import header
#print("Content-Type: text/html\n")
form=cgi.FieldStorage()
#print(form)
Id=form.getvalue("Id")
#print(id)
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
query=f"""SELECT * FROM product WHERE Id='{Id}'"""
#print(query)
mycursor.execute(query)
myresult=mycursor.fetchone()
#print(myresult)
print(f"""
<section class="learn" id="learn">
      <h1 class="heading">our <span>products</span></h1>

      <div class="box-container">
        
 <div class="box">
       <img src="html/ltr/Product/{myresult['Id']}/{myresult['Photo']}" alt="" >
            <h3>{myresult['ProductName']}<h3>
            <div class="price">Rs-{myresult['Price']}</div>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
      <p> {myresult['Description']} </p>
 <form action="addtocart.py"  method="POST" id="addToCartForm">
                            <label >Enter Quantity</label>
                            <input type="text" name="Quantity" id="Quantity" style="border: 1px solid black; color: black;">
                        <br><br>


                            <input type="text" name="Id" id="Id" value="{myresult['Id']}" style="display:none;">
                            <input type="text" name="ProductName" id="ProductName" value="{myresult['ProductName']}" style="display:none;">
                            <input type="text" name="Price" id="Price" value="{myresult['Price']}" style="display:none;">
                            <input type="hidden" name="UserID" id="UserID">
                            <br><br>

                            <button type="submit" class="btn">Add To Cart</button>
                           </form>
       
        </div>

       
      </div>
      
 </div>
       
    </section>
    <!--learn section ends-->
    
""")
print("""

<script>
document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("addToCartForm");

    form.addEventListener("submit", function (e) {

        let userId = localStorage.getItem("id");
        console.log("Submit user id:", userId);

        if (!userId) {
            e.preventDefault();
            alert("Please login first!");
            window.location.href = "Login.py";
            return;
        }

        document.getElementById("UserID").value = userId;
    });

});
</script>
""")
import footer