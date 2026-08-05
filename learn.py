#!C:\Python312\python.exe
import cgi
import cgitb
cgitb.enable()
#print("Content-Type: text/html\n")
import header
print(f"""
   <br> <br> <br> <br>
<!--learn section starts-->
    <section class="learn" id="learn">
      <h1 class="heading">Visit & <span>Learn</span></h1>

      <div class="box-container">
        <div class="box">
          <iframe width="960" height="415" src="https://www.youtube.com/embed/lTr-tPJ1C9A?si=852Nv1mVIk86xDK7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen width="400px" height="300px"></iframe>
          <h3>Meet our farmers</h3>
          <p>
            In this digital era you can directly reach out to our farmers using this video chat and ask your queries about organic farming
          </p>
         
        </div>

       
          
        </div>

        
      </div>
    </section>
    <!--learn section ends-->


""")
import footer