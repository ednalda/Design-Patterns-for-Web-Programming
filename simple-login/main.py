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
        <title>"House Hunters"</title>
        <link href="css/style.css" rel="stylesheet"  type="text/css"  />
    </head>
    <body> '''
        page_body = ''' <div id="content">
                           <div id="header">
                             <h1> The BoatHouse</h1>
                             <ul>
                               <li><a href="#">Home</a></li>
                               <li><a href="#">News</a></li>
                               <li><a href="#">Favorits</a></li>
                               <li><a href="#">About</a></li>
                               <li><a href="#">SingOut</a></li>
                             </ul>
                           <p>Pre-Owner boats find in <b>The BoatHouse</b> a place
                        to sale your boats, exchange experience, plan your trips, check reviews, and get the laters about boat technology.
                           </p>
                        </div>
                           <form method="GET" action="">
                               <h2>Register to post your Add</h2>
                               <label>Name: </label><br/><input type="text" name="user"  /><br />
                               <label>Address: </label><br/><input type="text" name="address"  /><br />
                               <label>Phone: </label><br/><input type="text" name="phone"  /><br /><br /><br />
                               <label>Add</label><br/><input type="text" name="add"/><br /><br /><br />
                               <label>Email: </label><br/><input type="text" name="email" /><br />
                               <label>Password: </label><br/><input type="text" name="password" /><br /><br /><br />
                               <label>Agree with Policy</label><input type="checkbox" name="policy" value ="policy"><br /><br />
                               <input type="submit" value="Submit" class="submit" /> </div>'''
        page_close = '''
                           </form>
    </body>
</html> '''


        if self.request.GET: #stablish condition
           user = self.request.GET['user']#condition true
           address = self.request.GET['address']#condition true
           phone = self.request.GET['phone']#condition true
           add = self.request.GET['add']
           email = self.request.GET['email']#condition true
           password = self.request.GET['password']#condition true
           checkbox = self.request.GET['policy']#condition true
           self.response.write('HELLO!  ' + user + '  '  + address + ' ' + phone + ' ' + checkbox + ' ' +  email  + ' ' +  password  + ' ' + add )#all condition are true
        else: #if condition above not satisfied, print next line
           self.response.write(page_body)#print out page






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)