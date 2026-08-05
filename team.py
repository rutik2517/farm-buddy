#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print(f"""
   <br> <br> <br> <br>

    <!-- about section starts  -->

    <section class="about" id="about">
      <h1 class="heading">Our <span>Team</span></h1>

      <div class="swiper about-slider">
        <div class="swiper-wrapper">
          <div class="swiper-slide box">
            <img src="https://raw.githubusercontent.com/STRIDER1512/FarmBuddy/main/FarmBuddy/images/Srikar%20Tenneti.jpg" alt="" />
            <p>
              "As the CEO of FarmBuddy, my goal is to create technology that helps our farmers succeed. We're constantly exploring new ideas and pushing the boundaries of what's possible, because we know that every improvement we make can have a real impact on the lives of farmers and the health of our environment."




            </p>
            <a href="https://www.linkedin.com/in/srikar-tenneti-849522235/">Srikar Tenneti-CEO</a>
            
          </div>

          <div class="swiper-slide box">
            <img src="https://raw.githubusercontent.com/STRIDER1512/FarmBuddy/main/FarmBuddy/images/sriraj%20tata.jpeg" alt="" />
            <p>
             "As the COO of FarmBuddy,I'm committed to ensuring that our customers receive the highest quality products and services. We strive to make our farm-to-table model efficient and sustainable, and are constantly exploring new ways to improve our operations."
            </p>
            <a href="https://www.linkedin.com/in/sriraj-tata-0499b7228/">Sriraj Tata-COO</a>
            
          </div>


          <div class="swiper-slide box">
            <img src="https://raw.githubusercontent.com/STRIDER1512/FarmBuddy/main/FarmBuddy/images/sudhish.jpg" alt="" />
            <p>
             "As the CTO of FarmBuddy, I am honored to be part of a team that is dedicated to creating a sustainable and efficient farming ecosystem. Our mission is to revolutionize the way food is grown, distributed and consumed around the world, and to help small-scale farmers thrive in the digital age."
            </p>
            <a href="https://www.linkedin.com/in/sudhish-amiti-491805224/">Sudhish Amiti-CTO</a>
            
          </div>


          <div class="swiper-slide box">
            <img src="https://raw.githubusercontent.com/STRIDER1512/FarmBuddy/main/FarmBuddy/images/himaja.jpg" alt="" />
            <p>
             "As the CFO of FarmBuddy, I am proud to be a part of a team that is committed to creating a positive impact in the agricultural industry. Our goal is to ensure that the farmers we work with have access to the necessary resources and funding to grow their businesses sustainably.
             </p>
            <a href="https://www.linkedin.com/in/himaja-vendra-48581324b/">Himaja Vendra-CFO</a>
            
          </div>
        </div>
      </div>
    </section>

    <!-- review section ends -->


""")
import footer