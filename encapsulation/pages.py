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
                                    <ul>
                                        <li><h1><img src="images/logo.jpg" class="logo" />Sweet Flower Shop </h1></li>
                                          <ul class="sub_nav">
                                             <li><a href="#">Home</a></li>
                                             <li><a href="#">Orders</a></li>
                                             <li><a href="#" class="active">Delivered</a></li>
                                             <li><a href="#">Hot Deals</a></li>
                                             <li><a href="#">Sign Out </a></li>
                                          </ul>
                                    </ul>
                                </nav>
                               </header>
                               <div id = "content">
                                    <article>
                                         <ul class="links">
                                            <li><h2><a href="?name=september">September</a></h2></li>
                                            <li><h2><a href="?name=november">November</a></h2></li>
                                            <li><h2><a href="?name=february">February</a></h2></li>
                                            <li><h2><a href="?name=june">June</a></h2></li>
                                            <li><h2><a href="?name=may">May</a></h2></li>
                                         </ul>
                                    </article>
                                    '''


        self.month_data = Delivered()


        self.month = '''
                    <aside>

                          <ul class="links">
                               <li>
                                    <h3>Basket of Joy:  {self.month_data.sale1}</h3>
                                    <h3>Country Basket Blooms:  {self.month_data.sale2} </h3>
                                    <h3>Summer Brights:  {self.month_data.sale3} </h3>
                                    <h3>Blooms:  {self.month_data.sale4} </h3>
                                    <h3>Garden Romance:  {self.month_data.sale5} </h3>
                                    <h3>Total:  {self.month_data.total}</h3>
                               </li>
                          </ul>
                    </aside>
           </div>
                     '''

        self.close = """

                       </div>

   </body>
 </html>
       """

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

    def print_out_data(self):
        a = self.head + self.month + self.close
        a = a.format(**locals())
        return a









