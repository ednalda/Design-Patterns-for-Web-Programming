#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
'''
name:Ednalda Fakira
date:09/11/14
class:Design Patterns for Web Programming - Online
assignment: Simple Form
'''
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
        self.response.write(s._total)#writing the total monthly sales as property as the getter gives access.

        #November delivered
        n = Delivered()
        n.sale1 = 50
        n.sale2 = 55
        n.sale3 = 68
        n.sale4 = 93
        n.sale5 = 32
        n.calc_total()
        self.response.write(n._total)

        #February delivered
        f = Delivered()
        f.sale1 = 24
        f.sale2 = 12
        f.sale3 = 18
        f.sale4 = 84
        f.sale5 = 34
        f.calc_total()
        self.response.write(f._total)

        #June delivered
        j = Delivered()
        j.sale1 = 50
        j.sale2 = 50
        j.sale3 = 50
        j.sale4 = 50
        j.sale5 = 50
        j.calc_total()
        self.response.write(j._total)

        #May delivered
        m = Delivered()
        m.sale1 = 50
        m.sale2 = 50
        m.sale3 = 50
        m.sale4 = 50
        m.sale5 = 50
        m.calc_total()
        self.response.write(m._total)

class Delivered(object):#class to call the attributes of objects.
    def __init__(self):
        self.sale1= 0
        self.sale2= 0
        self.sale3= 0
        self.sale4= 0
        self.sale5= 0
        self.__total= 0 #private attribute only access inside this class

    def calc_total(self):#function to calculate the total sales by adding the sales together.
        self._total = self.sale1 + self.sale2 + self.sale3 + self.sale4 + self.sale5

    #decorators treating properties as variables
    @property #getter: to return the total sales. It's accessing the total monthly sales attribute that is private only accessed inside the class Delivered.
    def total(self):#function
        return self.__total # return the total monthly sales attribute

    @total.setter #setter: It gives the ability to update the total monthly sales result as it need.
    def total(self, new_total):
        self._total = new_total

        if    self.request.GET:#function that checks if objects (Delivered) are requested its need to respond with a result writing the
              s = Delivered()
              n = Delivered()
              f = Delivered()
              j = Delivered()
              m = Delivered()
              self.response.write(self.head + self.body + self.__total + self.close)
        else:
              self.response.write(self.head + self.body + self.close)


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
                                         <p><input type="submit" value= "September" class="submit" /></p>
                                         <p><input type="submit" value= "November" class="submit" /></p>
                                         <p><input type="submit" value= "February" class="submit" /></p>
                                         <p><input type="submit" value= "June" class="submit" /></p>
                                         <p><input type="submit" value= "May" class="submit" /></p>
                                      </ul>
                                    </article>
                                    <aside>
                                    </aside>
                               </div>
                               '''

        self.calculate = '''<div id = "page">
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
        '''
        self.close = """
                                <footer>
                                  <p>Sweet Flower Shop @ 2014</p>
                               </footer>
                       </div>

   </body>
 </html>
       """






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
