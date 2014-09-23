__author__ = 'ednaldafakira'
class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
 <html>
   <head>
          <title>{self.title}</title>
          <link href="{self.css}" rel="stylesheet" type="text/css" />
   </head>
   <body>
        """

        self.body = '''<div id = "page">
                               <header>
                                    <nav>
                                      <ul class="nav">
                                          <li><img src="images/logo.jpg" class="logo" /></li>
                                          <li><h1>Sweet Flower  Shop</h1></li>
                                    </ul>
                                          <ul class="sub_nav">
                                             <li><a href="#">Home</a></li>
                                             <li><a href="#">Orders</a></li>
                                             <li><a href="#" class="active">Delivered</a></li>
                                             <li><a href="#">Hot Deals</a></li>
                                             <li><a href="#">Sign Out </a></li>
                                          </ul>

                                    </nav>
                               </header>
                               <div id = "content">
                                    <article>
                                     <form method="GET" action="">
                                         <ul>
                                            <p><a href="?name=september"><input type="submit"  value= "September" class="submit" /></a></p>
                                            <p><a href="?name=november"><input type="submit"  value= "November" class="submit" /></a></p>
                                            <p><a href="?name=february" ><input type="submit" value= "February" class="submit" /></a></p>
                                            <p><a href="?name=june" ><input type="submit"  value= "June" class="submit" /></a></p>
                                            <p><a href="?name=may"><input type="submit"  value= "May" class="submit" /></a></p>
                                         </ul>
                                      </form>
                                    </article>
                                    <aside>
                                    </aside>
                               </div>
                               '''
        self.september = ''' <div id = "content">
                    <article>
                    <h2>Your Monthly Expenses</h2>
                          <ul>
                               <h3>September</h3>
                               <li>
                                    <h3 id="s.sale1">Basket of Joy: </h3>
                                    <h3 id="s.sale2">Country Basket Blooms: </h3>
                                    <h3 id="s.sale3">Summer Brights: </h3>
                                    <h3 id="s.sale4">Fashionista Blooms: </h3>
                                    <h3 id="s.sale5">Garden Romance: </h3>
                                    <h3 class="total">Total:</h3>
                               </li>
                          </ul>
                    </article>
           </div>'''

        self.november = ''' <div id = "content">
                                 <h2>Your Monthly Expenses</h2>
                                   <article>
                                        <ul>
                                           <h3>November</h3>
                                           <li>
                                               <p>Cotton Candy: </p>
                                               <p>Roses: </p>
                                               <p>Tulips: </p>
                                               <p>Daisies: </p>
                                               <p>Gerberas: </p>
                                           </li>
                                        </ul>
                                   </article>
                        </div>'''



        self.february = '''<div id = "content">
                                   <h2>Your Monthly Expenses</h2>
                                   <article>
                                        <ul>
                                             <h3>February</h3>
                                             <li>
                                               <p>Violeta: </p>
                                               <p>Rose beauty: </p>
                                               <p>Regal Orchids: </p>
                                               <p>Yellow Trio Basket: </p>
                                               <p>Sunny Cyclamen: </p>
                                             </li>
                                        </ul>
                                   </article>
                               </div>'''



        self.june= '''<div id = "content">
                                   <h2>Your Monthly Expenses</h2>
                                   <article>
                                        <ul>
                                             <h3>June</h3>
                                             <li>
                                               <p>Country Basket Blooms: </p>
                                               <p>Basket of Joy: </p>
                                               <p>Regal Orchids: </p>
                                               <p>Summer Brights: </p>
                                               <p> Blooms: </p>
                                             </li>
                                        </ul>
                                   </article>
                        </div>'''


        self.may = '''<div id = "content">
                                            <h2>Your Monthly Expenses</h2>
                                            <article>
                                                 <ul>
                                                    <h3>May</h3>
                                                    <li>
                                                         <p>Roses: </p>
                                                         <p>Regal Orchids: </p>
                                                         <p>Daisies: </p>
                                                         <p>Tulips: </p>
                                                         <p>Garden Romance: </p>
                                                     </li>
                                                 </ul>
                                            </article>
                      </div>'''

        self.close = """
                                <footer>
                                  <p>Sweet Flower Shop @ 2014</p>
                               </footer>
                       </div>

   </body>
 </html>
       """


    def  print_out(self):
         all = self.head + self.body + self.close
         all = all.format(**locals())
         return all



         if   self.request.GET:
              september = self.request.GET['september']
              self.response.write(self.head + self.september +  s_button.show_result() + self.close)
         elif self.request.GET:
              november = self.request.GET['november']
              self.response.write(self.head + self.november +  n_button.show_result() + self.close)
         elif self.request.GET:
              february = self.request.GET['february']
              self.response.write(self.head + self.february +  f_button.show_result() + self.close)
         elif self.request.GET:
              june = self.request.GET['june']
              self.response.write(self.head + self.june +  j_button.show_result() + self.close)
         elif self.request.GET:
              may = self.request.GET['may']
              self.response.write(self.head + self.may +  m_button.show_result() + self.close)
         else:
              self.response.write(self.head + self.body + self.close)
