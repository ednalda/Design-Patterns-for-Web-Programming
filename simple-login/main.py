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
name:
date:
class:
assignment:
'''
import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): # function that starts everything. Catalyst
    about_button=Button()
    about_button.label="About Us"
    about_button.show_label()
    contact_button=Button()
    contact_button.label="contact Us"
    contact_button.show_label()
        #self.response.write('Hello world!')
        class Button(object):
        	def __init__(self):
        		#print "constructor method of button ran"
        		self.label=""
        		#self.on_roll_over("Hello!!")
        	def click(self):
        		print "I've been clicked"
        	def on_roll_over(self, message):
        	print "You've rolled over my button " + message


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
