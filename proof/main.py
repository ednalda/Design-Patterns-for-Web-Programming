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
import webapp2
import urllib2#library
from xml.dom import minidom
from collect import AppForm

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = AppForm()
        view.inputs = [['actor', 'text', 'actor'],['Submit','Submit']]
        self.response.write(view.print_out_form())
        #get information from urllib2 library to request the url
        if self.request.GET:#if is a request look for key=actor write  movie title and  movie category
           search = self.request.GET['actor']
           url = "http://netflixroulette.net/api/api.php?actor=" + search
           request = urllib2.Request(url)
           opener = urllib2.build_opener()
           result = opener.open(request)
           xmldoc = minidom.parse(result)
           self.response.write(xmldoc.getElementsByTagName('show_title')[0].firstChild.nodeValue)
           self.response.write(xmldoc.getElementsByTagName('category')[0].firstChild.nodeValue)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
