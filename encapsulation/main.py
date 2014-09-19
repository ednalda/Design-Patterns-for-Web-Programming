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
                                          <li><h1>Sweet Flower Shop</h1></li></ul>
                                          <ul class="sub_nav">
                                             <li><a href="#">Home</a></li>
                                             <li><a href="#">Talk to Us</a></li>
                                             <li><a href="#">Hot Deals</a></li>
                                             <li><a href="#">Sign Out </a></li>
                                          </ul>
                                      </ul>
                                    </nav>
                               </header>
                               <div id = "content">
                                    <article>
                                        <ul><h2>John Miller</h2>
                                           <li>
                                               <p>Quiz 1: 100</p>
                                               <p>Quiz 2: 87</p>
                                               <p>Quiz 3: 56</p>
                                               <p>Quiz 4: 90</p>
                                               <p>Quiz 5: 69</p>
                                           </li>
                                           <li>
                                               <p>Final Grade <input type="submit" value= "Calculate" class="submit" /></p>
                                           </li>
                                        </ul>

                                        <ul><h2>Mary Smith</h2>
                                             <li>
                                               <p>Quiz 1: 100</p>
                                               <p>Quiz 2: 87</p>
                                               <p>Quiz 3: 56</p>
                                               <p>Quiz 4: 90</p>
                                               <p>Quiz 5: 69</p>
                                           </li>
                                           <li>
                                               <p>Final Grade <input type="submit" value= "Calculate" class="submit" /></p>
                                           </li>
                                        </ul>



                                        <ul><h2>Paul Peace</h2>
                                             <li>
                                               <p>Quiz 1: 100</p>
                                               <p>Quiz 2: 87</p>
                                               <p>Quiz 3: 56</p>
                                               <p>Quiz 4: 90</p>
                                               <p>Quiz 5: 69</p>
                                           </li>
                                          <li>
                                               <p>Final Grade <input type="submit" value= "Calculate" class="submit" /></p>
                                           </li>
                                        </ul>


                                        <ul>
                                           <li><h2>Steven Woods</h2></li>
                                             <li>
                                               <p>Quiz 1: 100</p>
                                               <p>Quiz 2: 87</p>
                                               <p>Quiz 3: 56</p>
                                               <p>Quiz 4: 90</p>
                                               <p>Quiz 5: 69</p>
                                             </li>
                                          <li>
                                               <p>Final Grade <input type="submit" value= "Calculate" class="submit" /></p>
                                           </li>
                                        </ul>



                                        <ul><h2>Tracey Fish</h2>
                                             <li>
                                               <p>Quiz 1: 100</p>
                                               <p>Quiz 2: 87</p>
                                               <p>Quiz 3: 56</p>
                                               <p>Quiz 4: 90</p>
                                               <p>Quiz 5: 69</p>
                                              </li>
                                            <li>
                                               <p>Final Grade <input type="submit" value= "Calculate" class="submit" /></p>
                                           </li>
                                        </ul>

                                    </article>
                                    <article>
                                    </article>
                                    <aside>
                                    </aside>
                               </div>
                               <footer>
                                  <p>footer</p>
                               </footer> '''
        self.close = """

                   </div>
   </body>
 </html>
       """


    def print_out(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
