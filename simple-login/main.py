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
        <title>"BoatHouse"</title>
        <link href="css/style.css" rel="stylesheet"  type="text/css"  />
    </head>
    <body> '''
        page_body = ''' <div id="content">
                           <div id="header">
                             <h1> The BoatHouse</h1>
                             <ul>
                               <li><a href="#" class="link">Home</a></li>
                               <li><a href="#" class="link">News</a></li>
                               <li><a href="#" class="link">Favorite</a></li>
                               <li><a href="#" class="link">About</a></li>
                               <li><a href="#" class="link">Log On</a></li>
                             </ul>
                           </div>
                           <form method="GET" action="">
                               <h2>Register to post your Add</h2>
                               <label>Name: </label><br/><input type="text" name="user" class="input" /><br />
                               <label>Address: </label><br/><input type="text" name="address"  class="input" /><br />
                               <label>Phone: </label><br/><input type="text" name="phone"   class="input"/><br /><br /><br />
                               <label>Ad</label><br/><input type="text" name="ad" class="input"/><br /><br /><br />
                               <label>Email: </label><br/><input type="text" name="email" class="input"/><br />
                               <label>Password: </label><br/><input type="text" name="password" class="input" /><br /><br /><br />
                               <input type="checkbox" name="policy" value ="policy"><a href="#" class="link">Agree with Policy</a><br /><br />
                               <input type="submit" value="Submit" class="submit" /> </form>'''
        page_answer = '''
                        <div id="page">
                            <div id="header">
                                  <h1> The BoatHouse</h1>
                                  <ul>
                                     <li><a href="#" class="link">Home</a></li>
                                     <li><a href="#" class="link">News</a></li>
                                     <li><a href="#" class="link">Favorite</a></li>
                                     <li><a href="#" class="link">About</a></li>
                                     <li><a href="#" class="link">Log On</a></li>
                                  </ul>
                            </div>
                            <div id="page_content">
                            <h3>Name:</h3> <h3>Address:</h3> <h3>Phone:</h3> <h3>Email:</h3> <h3>Password:</h3> <h3>Ad:</h3>
                            </div>
                        </div>
        '''
        page_close = '''
                           </div>
    </body>
</html> '''



        if self.request.GET: #stablish condition
           user = self.request.GET['user']#condition true
           address = self.request.GET['address']#condition true
           phone = self.request.GET['phone']#condition true
           ad = self.request.GET['ad']
           email = self.request.GET['email']#condition true
           password = self.request.GET['password']#condition true
           policy = self.request.GET ['policy']
           self.response.write(page_head + page_answer + ' ' + user + '  '  + address + '  ' + phone +  '  ' +   email + '  ' +   password  + '  ' + ad + '  ' + policy + '  ' + page_close)#all condition are true


        else: #if condition above not satisfied, print next line
           self.response.write(page_head + page_body + page_close)#print out page






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)