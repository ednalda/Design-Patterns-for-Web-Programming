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
from pages import Page #impor class Page from pages file
class  MainHandler(webapp2.RequestHandler):

    def get(self):

        s = Delivered()#next five objects
        s.sale1 = 40
        s.sale2 = 69
        s.sale3 = 36
        s.sale4 = 89
        s.sale5 = 24
        s.calc_total()
        s_sales = [[s.sale1, s.sale2, s.sale3, s.sale4, s.sale5],[s.calc_total()]]


        #November delivered
        n = Delivered()
        n.sale1 = 50
        n.sale2 = 55
        n.sale3 = 68
        n.sale4 = 93
        n.sale5 = 32
        n.calc_total()
        n_sales = [[n.sale1, n.sale2, n.sale3, n.sale4, n.sale5], [n.calc_total()]]



        #February delivered
        f = Delivered()
        f.sale1 = 24
        f.sale2 = 12
        f.sale3 = 18
        f.sale4 = 84
        f.sale5 = 34
        f.calc_total()
        f_sales = [[f.sale1, f.sale2, f.sale3, f.sale4, f.sale5], [f.calc_total()]]


        j = Delivered()
        j.sale1 = 50
        j.sale2 = 50
        j.sale3 = 50
        j.sale4 = 50
        j.sale5 = 50
        j.calc_total()
        j_sales = [[j.sale1, j.sale2, j.sale3, j.sale4, j.sale5],[j.calc_total()]]


        #May delivered
        m = Delivered()
        m.sale1 = 50
        m.sale2 = 50
        m.sale3 = 50
        m.sale4 = 50
        m.sale5 = 50
        m.calc_total()
        m_sales = [[m.sale1, m.sale2, m.sale3, m.sale4, m.sale5], [m.calc_total()]]


        s_button = Button ()
        s_button.result = s_sales[0][1]
        s_button.show_result()

        n_button = Button ()
        n_button.result =  n_sales[0][1]
        n_button.show_result()

        f_button = Button ()
        f_button.result = f_sales[0][1]
        f_button.show_result()

        j_button = Button ()
        j_button.result =  j_sales[0][1]
        j_button.show_result()


        m_button = Button ()
        m_button.result =  m_sales[0][1]
        m_button.show_result()

        p = Page()
        self.response.write (p.print_out())



class Delivered(object):#class to call the attributes of objects.
    def __init__(self): #Constrution method to design the object (Delivered)
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





class Button (object):
    def __init__(self):
        self.result=""

    def show_result(self):#click button to call the object.
        self.response.write(self.result)











app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
