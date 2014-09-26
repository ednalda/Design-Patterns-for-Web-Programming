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
import urllib2
from xml.dom import minidom
from collect import AppForm

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = AppForm()
        view.inputs = [['actor', 'text', 'actor'],['Submit', 'Submit']]
        self.response.write(view.print_out_form())
        if self.request.GET:
            actor = self.request.GET['actor']
            url = "http://netflixroulette.net/api/api.php?actor=" + actor
            request = urllib2.Request(url)
            opener = urllib2.build_opener()
            result = opener.open(request)

            xmldoc = minidom.parse(result)
            self.response.write(xmldoc.getElementsByTagName('show_title')[0].firstChild.nodeValue)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
