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
import webapp2  # use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):  #function that starts everything. Catalyst
        page_head = ''' <!DOCTYPE HTML>
                          <html>
                             <head>
                                <title>Simple Form</title>
                             </head>
                             <body> '''
                               page_body=''' <form method="GET" action="" >
                                                 <h1>Register to post your Add</h1>
                                                 <label>Name: </label><br/><input type="text" name="user" /><br />
                                                 <label>Address: </label><br/><input type="text" name="address" /><br />
                                                 <label>Phone: </label><br/><input type="text" name="phone" /><br /><br /><br />
                                                 <label>Where do you want your add appear? </label><br />
                                                 <input type="checkbox" name="orlando" value="orlando">Orlando<br />
                                                 <input type="checkbox" name="miami" value="miami">Miami<br   />
                                                 <label>Add </label><br/><input type="text" name="add" /><br /><br /><br />
                                                 <label>Email: </label><br/><input type="text" name="email" /><br />
                                                 <label>Password: </label><br/><input type="text" name="password" /><br /><br /><br />
                                                 <a href="?email=marketing@add.com&user=marketing">Marketing Manager</a><br />
                                                 <a href="?email=customer@add.com$user=customer">Customer Service</a><br /><br /><br />
                                                 <input type="submit" value="Submit"/>'''
                               page_close = '''
                               </form>
                             </body>
                          </html>'''


        if self.request.GET: #stablish condition
           user = self.request.GET['user']#condition true
           address= self.request.GET['address']#condition true
           phone= self.request.GET['phone']#condition true
           orlando = self.request.GET['orlando']#condition true
           miami = self.request.GET['miami']#condition true
           email = self.request.GET['email']#condition true
           password = self.request.GET['password']#condition true
        self.response.write(page_head + user + '' + page_close)#all condition are true, print
        else:if #if condition above not satisfied, print next line
        self.response(page_body)#print out page





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
