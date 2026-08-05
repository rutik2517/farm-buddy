#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")

print(f"""
 <!-- footer section starts  -->

    <section class="footer">
      <div class="box-container">
        <div class="box">
          <h3>FarmBuddy <i class="fas fa-seedling"></i></h3>
          <p>
            From our farm to your home without any intermediaries
          </p>
          <div class="share">
            <a href="https://github.com/STRIDER1512/FarmBuddy" class="fab fab fa-github"></a>
            <a href="mailto: farmbuddy2023@gmail.com" class="fas fa-envelope"></a>
            <a href="#" class="fas fa-phone"></a>
            <a href="https://goo.gl/maps/ohjevE4orfM8WPbJ6" class="fas fa-map-marker-alt"></a>
            <div><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1896.16918784813!2d83.41972423862734!3d18.102158695728058!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a3be54aa8834377%3A0xc844be10c2ca754c!2sOm%20Shakti%20Towers!5e0!3m2!1sen!2sin!4v1681492065885!5m2!1sen!2sin" width="300" height="150" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
          </div>
        </div>

          

        <div class="box">
          <h3>quick links</h3>
          <a href="index.py" class="links">
            <i class="fas fa-arrow-right"></i> home
          </a>
          <a href="features.py" class="links">
            <i class="fas fa-arrow-right"></i> features
          </a>
          <a href="categories.py" class="links">
            <i class="fas fa-arrow-right"></i> categories
          </a>
          <a href="products.py" class="links">
            <i class="fas fa-arrow-right"></i> products
          </a>
          <a href="learn.py" class="links">
            <i class="fas fa-arrow-right"></i> Learn
          </a>
          
          
          
         
          
        </div>

        <div class="box">
          <h3>newsletter</h3>
          <p>subscribe for latest updates</p>
          <input type="email" placeholder="your email" class="email" />
          <input type="submit" value="subscribe" class="btn" />
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMdbKS4jP-F6Ug1e9mDgGc6Bre2Y4CYHJFqA&s" class="payment-img" alt="" />
        </div>
      </div>
    </section>

    <!-- footer section ends -->

    <script src="https://unpkg.com/swiper@7/swiper-bundle.min.js"></script>

    <!-- custom js file link  -->
    <script src="script.js"></script>
    <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1%22%3E"> </script>
<df-messenger intent="WELCOME" chat-title="FarmBuddy"
  agent-id="e1f83922-37a6-488b-9c06-b8cc656319b3"
  language-code="en"
></df-messenger>
   
  </body>
</html>
""")