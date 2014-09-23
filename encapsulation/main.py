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
from deliveres import Delivered
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


        s_button = Button()
        s_button.result = s_sales[0][1]
        s_button.show_result()

        n_button = Button()
        n_button.result = n_sales[0][1]
        n_button.show_result()

        f_button = Button()
        f_button.result = f_sales[0][1]
        f_button.show_result()

        j_button = Button()
        j_button.result = j_sales[0][1]
        j_button.show_result()


        m_button = Button()
        m_button.result = m_sales[0][1]
        m_button.show_result()

        p = Page()
        self.response.write(p.print_out())


        if self.request.GET:
        #if we have September after name in url
           if    self.request.GET['name'] == 'september':
                 p.month_data = s
                 self.response.write(p.month + p.close)

           elif  self.request.GET ['name'] == 'november':
                 p.month_data = n
                 self.response.write(p.month + p.close)

           elif  self.request.GET ['name'] == 'february':
                 p.month_data = f
                 self.response.write(p.month + p.close)

           elif  self.request.GET ['name'] == 'june':
                 p.month_data = j
                 self.response.write(p.month + p.close)

           elif  self.request.GET ['name'] == 'may':
                 p.month_data = m
                 self.response.write(p.month + p.close)

           else:

                 self.response.write(p.head + p.body + p.close)
        else:
           self.response.write('')





class Button (object):
    def __init__(self):
        self.result = ""

    def show_result(self):
        self.result = ""














app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
