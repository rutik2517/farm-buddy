#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")

print(f"""
         <br> <br> <br> <br>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>FarmBuddy</title>

    <link
      rel="stylesheet"
      href="https://unpkg.com/swiper@7/swiper-bundle.min.css"
    />

    <!-- font awesome cdn link  -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    />

    <!-- custom css file link  -->
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <!-- header section starts  -->

    <header class="header">
      <a href="#" class="logo">
        <i class="fas fa-seedling"></i> FarmBuddy
      </a>

      <nav class="navbar">
        <a href="index.py">home</a>
        <a href="features.py">features</a>
      <a href="" id="nav-plant">plant</a>
        <a href="categories.py">categories</a>
        <a href="products.py">products</a>
        <a href="learn.py">Learn</a>
       
        <a href="sigup.py" id="signin-signup">Sign in/up</a>
      
    
       <a href="#"><span id="FirstName"></span></a>
       <a href="" id="nav-myprofile">my Profile</a>
      <a href="Logout.py" id="nav-logout">Logout</a>
      </nav>

       

      <form action="" class="search-form">
        <input type="search" id="search-box" placeholder="search here..." />
        <label for="search-box" class="fas fa-search"></label>
      </form>

      <div class="shopping-cart">
        <div class="box">
          <i class="fas fa-trash"></i>
          <img src="https://raw.githubusercontent.com/STRIDER1512/FarmBuddy/main/FarmBuddy/images/cart-img-1.png" alt="" />
          <div class="content">
            <h3>watermelon</h3>
            <span class="price">44.99/-</span>
            <span class="quantity">qty : 1</span>
          </div>
        </div>
        <div class="box">
          <i class="fas fa-trash"></i>
          <img src="https://raw.githubusercontent.com/STRIDER1512/FarmBuddy/main/FarmBuddy/images/cart-img-2.png" alt="" />
          <div class="content">
            <h3>onion</h3>
            <span class="price">$24.99/-</span>
            <span class="quantity">qty : 1</span>
          </div>
        </div>
        <div class="box">
          
        </div>
        <div class="total">total : $68.98/-</div>
        <a href="" class="btn">checkout</a>
      </div>
      

      
    </header>
""")
print("""
<script>
    document.addEventListener("DOMContentLoaded", function () {
        let firstName = localStorage.getItem("FirstName");
      let UserID = localStorage.getItem("id");

      let urllink="myProfile.py?UserID="+UserID;


      let urllinkk="products.py?UserID="+UserID;

      let sao="plant.py?UserID="+UserID;
      
       

        if (firstName) {
      console.log('xyz');
            document.getElementById("FirstName").textContent = firstName;
            

  document.getElementById("signin-signup").style.display="none";
      document.getElementById("nav-myprofile").href=urllink;
       document.getElementById("nav-plant").href=sao;
         
    
        } else {
      console.log('abc');
            
            document.getElementById("nav-logout").style.display="none";
      document.getElementById("nav-myprofile").style.display="none";
      document.getElementById("nav-plant").style.display="none";
      
        }
    });
</script>
""")