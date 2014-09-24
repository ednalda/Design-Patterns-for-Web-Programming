__author__ = 'ednaldafakira'

from deliveres import Delivered
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
                                         <ul>
                                            <p><a href="?name=september">September</a></p>
                                            <p><a href="?name=november">november</a></p>
                                            <p><a href="?name=february">february</a></p>
                                            <p><a href="?name=june">june</a></p>
                                            <p><a href="?name=may">may</a></p>
                                         </ul>
                                    </article>
                               </div>
                               '''
        self.month_data = Delivered()


        self.month = ''' <div id = "content">
                    <article>
                    <h2>Your Monthly Expenses</h2>
                          <ul>
                               <li>
                                    <h3 name="data1">Basket of Joy:{self.month_data.sale1}</h3>
                                    <h3>Country Basket Blooms:{self.month_data.sale2} </h3>
                                    <h3>Summer Brights:{self.month_data.sale3} </h3>
                                    <h3>Blooms:{self.month_data.sale4} </h3>
                                    <h3>Garden Romance:{self.month_data.sale5} </h3>
                                    <h3>Total:{self.month_data.total}</h3>
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

    def print_out(self):
        all = self.head + self.body #+ self.close
        all = all.format(**locals())
        return all

    def print_out_data(self):
        a = self.head + self.month + self.close
        a = a.format(**locals())
        return a









