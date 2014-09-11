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
        page_head = '''<!DOCTYPE HTML>
                      <html>
                        <head>
                           <title>Simple Form</title>
                        </head>
                        <body>'''
                            page_body = '''<form method="GET" action="" >
                                <h1>Register</h1>
                                <label>Name: </label><input type="text" name="user" />
                                <label>Address: </label><input type="text" name="address" />
                                <label>Phone: </label><input type="text" name="phone" />
                                <label>Email: </label><input type="text" name="email" />
                                <label>Password: </label><input type="text" name="password" />
                                <input type="submit" value="Submit"/>'''
                            page_close = '''
                            </form>
                        </body>
                      </html>'''
        if self.request.GET:#condition to execute next line
           user = self.request.GET['user']#request information from the server
           address = self.request.GET['address']#request information from the server
           phone = self.request.GET['phone']#request information from the server
           email = self.request.GET['email']#request information from the server
           password = self.request.GET['password']#request information from the server
        self.response.write(page_head + user + page_body + page_close)#print the information out
        else:
        self.response.write(page_head + page_body + page_close)#print the information out

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
