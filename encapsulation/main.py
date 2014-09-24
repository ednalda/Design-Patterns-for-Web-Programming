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
#it connects to class Page in a separate file.
from pages import Page
#it connects to class Delivered from deliveres file.
from deliveres import Delivered
class  MainHandler(webapp2.RequestHandler):
    def get(self):
     #function defines attributes of five objects: s, n, f, j, m
     #get function print_out to print html
     #get function if statement that defines condition for printing class Delivered attributes

        s = Delivered()#defines class delivered attributes for September
        s.sale1 = 40#how much it cost each sales
        s.sale2 = 69
        s.sale3 = 36
        s.sale4 = 89
        s.sale5 = 24
        s.calc_total()#function to calculate the total of September sales.


        #"November" class delivered variables
        n = Delivered()#defines class delivered attributes for November
        n.sale1 = 50#how much it cost each sales
        n.sale2 = 55
        n.sale3 = 68
        n.sale4 = 93
        n.sale5 = 32
        n.calc_total()#function to calculate the total of November sales.


        #February delivered
        f = Delivered()#defines class delivered attributes for February
        f.sale1 = 24#how much it cost each sales
        f.sale2 = 12
        f.sale3 = 18
        f.sale4 = 84
        f.sale5 = 34
        f.calc_total()#function to calculate the total of February sales.



        j = Delivered()#defines class delivered attributes for June
        j.sale1 = 50#how much it cost each sales
        j.sale2 = 50
        j.sale3 = 50
        j.sale4 = 50
        j.sale5 = 50
        j.calc_total()#function to calculate the total of June sales.


        #May delivered
        m = Delivered()#defines class delivered attributes for May
        m.sale1 = 50#how much it cost each sales
        m.sale2 = 50
        m.sale3 = 50
        m.sale4 = 50
        m.sale5 = 50
        m.calc_total()#function to calculate the total of May sales.



        #call class Page to print in this page
        p = Page()
        self.response.write(p.print_out())

        #if the links are requested, it's print_out_data function called to print the data from the self.month
        if self.request.GET:
        #if we have September after name in url
           if    self.request.GET['name'] == 'september':
                 p.month_data = s #part of the html from class Page that holds the class Delivered attributes for each month
                 self.response.write(p.print_out_data())# call function print_out_data from class Page to print Delivered attributes.
        #if we have November after name in url
           elif  self.request.GET ['name'] == 'november':
                 p.month_data = n
                 self.response.write(p.print_out_data())
        #if we have February after name in url
           elif  self.request.GET ['name'] == 'february':
                 p.month_data = f
                 self.response.write(p.print_out_data())
        #if we have June after name in url
           elif  self.request.GET ['name'] == 'june':
                 p.month_data = j
                 self.response.write(p.print_out_data())
        #if we have May after name in url
           elif  self.request.GET ['name'] == 'may':
                 p.month_data = m
                 self.response.write(p.print_out_data())
        #if we don't find any of the names above after name in url, just print same page
           else:
                 self.response.write(p.head + p.body + p.close)
        #the print is empty to avoid the same page print twice.
        else:
           self.response.write('')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
