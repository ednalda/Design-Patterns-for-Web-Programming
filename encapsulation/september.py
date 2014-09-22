__author__ = 'ednaldafakira'


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


