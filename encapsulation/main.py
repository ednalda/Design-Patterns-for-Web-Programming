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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        self.response.write(p.print_out())

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
                                         <p><input type="submit" value= "Febuary" class="submit" /></p>
                                         <p><input type="submit" value= "June" class="submit" /></p>
                                         <p><input type="submit" value= "May" class="submit" /></p>
                                      </ul>
                                    </article>
                                    <aside>
                                    </aside>
                               </div>
                               '''

        self.calculate = ''' <article>
                                        <h2>Montly Expenses</h2>

                                        <ul>

                                           <h3>September</h3>
                                           <li>
                                               <p>Basket of Joy: $52.95</p>
                                               <p>Country Basket Blooms:$57.95 </p>
                                               <p>Summer Brights: $44.95 </p>
                                               <p>Fashionista Blooms: 69.90</p>
                                               <p>Garden Romance: $49.95 </p>
                                           </li>
                                        </ul>

                                        <ul>
                                           <h3>November</h3>
                                           <li>
                                               <p>Cotton Candy: $39.95</p>
                                               <p>Roses: $43.98</p>
                                               <p>Tulips: $56</p>
                                               <p>Daisies: $42.80</p>
                                               <p>Gerberas: $38.99</p>
                                           </li>
                                        </ul>

                                        <ul>
                                             <h3>Febuary</h3>
                                             <li>
                                               <p>Violetas: $25.90</p>
                                               <p>Rose beauty: $87.98</p>
                                               <p>Regal Orchids: $56.76</p>
                                               <p>Yellow Trio Basket: $90.58</p>
                                               <p>Sunny Cyclamen: $69.43</p>
                                           </li>
                                        </ul>


                                        <ul>
                                             <h3>May</h3>
                                             <li>
                                               <p>Country Basket Blooms:$57.95</p>
                                               <p>Basket of Joy: $52.95: 87</p>
                                               <p>Regal Orchids: $56.76</p>
                                               <p>Summer Brights: $44.95</p>
                                               <p>Fashionista Blooms: 69.90</p>
                                             </li>
                                        </ul>



                                        <ul>
                                             <h3>June</h3>
                                             <li>
                                               <p>Roses: $43.98</p>
                                               <p>Regal Orchids: $56.76</p>
                                               <p>Daisies: $42.80</p>
                                               <p>Tulips: $56</p>
                                               <p>Garden Romance: $49.95</p>
                                              </li>
                                        </ul>
                                </article>
        '''
        self.close = """
                                <footer>
                                  <p>Sweet Flower Shop @ 2014</p>
                               </footer>
                       </div>

   </body>
 </html>
       """


    if  self.request.GET:

        self.response.write (self.head + self.body + self.calculate + self.close)
    else:
        self.response.write (sel.head + self.body + self.close)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
