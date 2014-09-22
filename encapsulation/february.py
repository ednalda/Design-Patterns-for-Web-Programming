__author__ = 'ednaldafakira'
import webapp2

class  MainHandler(webapp2.RequestHandler):

    def get(self):
        #February delivered
        f = Delivered()
        f.sale1 = 24
        f.sale2 = 12
        f.sale3 = 18
        f.sale4 = 84
        f.sale5 = 34
        f.calc_total()
        #self.response.write(f.total)
        p = Page4()
        self.response.write (p.print_out())
class Delivered(object):#class to call the attributes of objects.
    def __init__(self):
        self.sale1= 0
        self.sale2= 0
        self.sale3= 0
        self.sale4= 0
        self.sale5= 0
        self.__total= 0 #private attribute only access inside this class
         #decorators treating properties as variables
    @property #getter: to return the total sales. It's accessing the total monthly sales attribute that is private only accessed inside the class Delivered.
    def total(self):#function
        return self.__total # return the total monthly sales attribute

    @total.setter #setter: It gives the ability to update the total monthly sales result as it need.
    def total(self, new_total):
        self.__total = new_total

    def calc_total(self):#function to calculate the total monthly sales by adding the sales together.
        self.__total = self.sale1 + self.sale2 + self.sale3 + self.sale4 + self.sale5
class Page4(object):
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
        self.body = '''
                <div id = "page">
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
                               </div>
                         </div> '''

        self.close = """
    </body>
 </html>"""

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

