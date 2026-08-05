#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print(f"""



  
 

    <!-- header section ends -->

    <!-- home section starts  -->

    <section class="home" id="home">
      <div class="content">
        <h3><span>fresh</span> and <span>organic</span> products for you</h3>
        <p>
          From our Farm to your Home without any intermediaries
        </p>
        <a href="products.py" class="btn">shop now</a>
      </div>
    </section>

    <!-- home section ends -->
    
    

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

    <!-- products section starts  -->
<section class="learn" id="learn">
      <h1 class="heading">our <span>products</span></h1>

      <div class="box-container">
        

        <div class="box">
          <img src="https://ohmyfacts.com/wp-content/uploads/2024/07/40-facts-about-cabbage-1720521838.jpg" alt="" />
            <h3>cabbage</h3>
            <div class="price">54/- - 80/-</div>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
      <p>
            we also make it easy to directly visit your nearest farms from here and learn the cultivation processes
          </p>
            <a href="products.py" class="btn">add to cart</a>
        </div>
      
      <div class="box">
          <img src="https://wallpapers.com/images/hd/green-leaves-and-oranges-uyqrz6cgd62vbzmh.jpg" alt="" />
            <h3>Orange</h3>
            <div class="price">54/- - 80/-</div>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
      <p>
            we also make it easy to directly visit your nearest farms from here and learn the cultivation processes
          </p>
            <a href="products.py" class="btn">add to cart</a>
        </div>
      
      <div class="box">
          <img src="https://tse1.mm.bing.net/th/id/OIP.s2jWlvW08GwmxHzjvo4s6AHaEy?pid=Api&P=0&h=180" alt="" />
            <h3>onion</h3>
            <div class="price">54/- - 80/-</div>
            <div class="stars">
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
              <i class="fas fa-star"></i>
            </div>
      <p>
            we also make it easy to directly visit your nearest farms from here and learn the cultivation processes
          </p>
            <a href="products.py" class="btn">add to cart</a>
        </div>

       
      </div>
    </section>
    <!--learn section ends-->

    <!-- products section ends -->
    
    
    <!--learn section starts-->
    <section class="learn" id="learn">
      <h1 class="heading">Visit & <span>Learn</span></h1>

      <div class="box-container">
        <div class="box">
          <img src="https://images.unsplash.com/photo-1626488033090-79f63fd81a75?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80" alt="" />
          <h3>Meet our farmers</h3>
          <p>
            In this digital era you can directly reach out to our farmers using this video chat and ask your queries about organic farming
          </p>
          <a href="learn.py" class="btn">read more</a>
        </div>

        <div class="box">
          <img src="https://images.unsplash.com/photo-1592210454359-9043f067919b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt="" />
          <h3>Weather updates</h3>
          <p>
            we update weather reports for farmer's convinience to check daily updates of weather and plan their farming accordingly. 
          </p>
          <a href="https://www.windy.com/-Waves-waves" class="btn">read more</a>
        </div>

       
      </div>
    </section>
    <!--learn section ends-->
    

    

    


   
""")
import footer