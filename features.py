#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print(f"""
   <br> <br> <br> <br>
 <!-- features section starts  -->

    <section class="features" id="features">
      <h1 class="heading">our <span>features</span></h1>

      <div class="box-container">
        <div class="box">
          <img src="https://images.unsplash.com/photo-1461354464878-ad92f492a5a0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt="" />
          <h3>fresh and organic</h3>
          <p>
            Here,we sell all the fresh and organic products
          </p>
        </div>

        <div class="box">
          <img src="https://images.unsplash.com/photo-1595246140625-573b715d11dc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt="" />
          <h3>fast delivery</h3>
          <p>
            All the organic products to your doorstep
          </p>
            
          </div>

        <div class="box">
          <img src="https://images.unsplash.com/photo-1628527304948-06157ee3c8a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt="" />
          <h3>easy payments</h3>
          <p>
            here, at farmBuddy payments made easy
          </p>
            
          </div>
      </div>
    </section>

    <!-- features section ends -->


""")
import footer