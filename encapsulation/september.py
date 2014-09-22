__author__ = 'ednaldafakira'
import webapp2

class  MainHandler(webapp2.RequestHandler):

    def get(self):
        #September delivered
        s = Delivered()#next five objects
        s.sale1 = 40
        s.sale2 = 69
        s.sale3 = 36
        s.sale4 = 89
        s.sale5 = 24
        s.calc_total()
        #self.response.write(s.total)
        p = Page2()
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
class Page2(object):
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
                    <article>
                    <h2>Your Monthly Expenses</h2>
                          <ul>
                               <h3>September</h3>
                               <li>
                                    <h3>Basket of Joy: </h3><p class="price" id="s.sale1">''</p>
                                    <h3>Country Basket Blooms: </h3><p class="price" id="s.sale2">''</p>
                                    <h3>Summer Brights: </h3><p class="price" id="s.sale3">''</p>
                                    <h3>Fashionista Blooms: </h3><p class="price" id="s.sale4">''</p>
                                    <h3>Garden Romance: </h3><p class="price" id="s.sale5">''</p>
                                    <h3 class="total">Total:</h3><p class="total" >''</p>
                               </li>
                          </ul>
                    </article>
           </div>'''
        self.close = """
    </body>
 </html>"""

    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

