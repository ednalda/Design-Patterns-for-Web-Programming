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
    <body '''
        page_body=''' <form method="GET" action="" style="border:1px  #f5f5dc; background-color: green; width:30%;margin:0 20%; padding:2% 20% ">

                         <h1 style="font-family: arial; font-weight:bolder; color: white">Register to post your Add</h1>

                         <label style="color: white">Name: </label><br/><input type="text" name="user" style="width:100%" /><br />
                         <label style="color: white">Address: </label><br/><input type="text" name="address" style="width:100%" /><br />
                         <label style="color: white">Phone: </label><br/><input type="text" name="phone" style="width:100%" /><br /><br /><br />
                         <label style="color: white">Where do you want your add appear? </label><br />
                         <input type="checkbox" name="orlando" value ="orlando" style="color: white">Orlando<br />
                         <input type="checkbox" name="miami" value="miami">Miami<br   />
                         <label style="color: white">Add </label><br/><input type="text" name="add" style="width:100%" /><br /><br /><br />
                         <label style="color: white">Email: </label><br/><input type="text" name="email" style="width:100%" /><br />
                         <label style="color: white">Password: </label><br/><input type="text" name="password" style="width:100%" /><br /><br /><br />
                         <a href="?email=marketing@add.com&user=marketing" style="color: white">Marketing Manager</a><br />
                         <a href="?email=customer@add.com$user=customer"style="color: white">Customer Service</a><br /><br /><br />
                         <input type="submit" value="Submit" style="background-color: white; color: green; width:100%; font-family: arial; font-size: 120%" />'''
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
        else: #if condition above not satisfied, print next line
           self.response.write(page_body)#print out page





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
