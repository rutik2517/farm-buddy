#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print(f"""
      <br> <br> <br> <br>

 <!-- categories section starts  -->

    <section class="categories" id="categories">
      <h1 class="heading">product <span>categories</span></h1>

      <div class="box-container">
       

        <div class="box">
          <img src="https://eskipaper.com/images/fresh-fruits-1-1.jpg" alt="" />
          <h3>fresh fruits</h3>
          <p>naturally produced fruits</p>
        </div>

        <div class="box">
          <img src="https://domf5oio6qrcr.cloudfront.net/medialibrary/5413/h0119h16207258225642.jpg" alt="" />
          <h3>dairy products</h3>
          <p>freshly made dairy products without preservatives</p>
        </div>
      
      <div class="box">
          <img src="https://sustainablemacleod.org.au/wp-content/uploads/2022/08/fertilisers-1280x960.jpg" alt="" />
          <h3>Fertilizer</h3>
          <p>naturally produced fruits</p>
        </div>
      
      <div class="box">
          <img src="https://www.perfection.com.au/hs-fs/hubfs/Produce_LR_Category_Proprietary%20Fruit%20and%20Vegetables%20Group_Styled_2022_03%20(1).jpg?width=2250&name=Produce_LR_Category_Proprietary%20Fruit%20and%20Vegetables%20Group_Styled_2022_03%20(1).jpg" alt="" />
          <h3>Fruits vegetables</h3>
          <p>naturally produced fruits</p>
        </div>
      </div>
    </section>

    <!-- categories section ends -->



""")
import footer