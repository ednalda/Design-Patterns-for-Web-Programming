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
import urllib2#python class to request, receive, and open
import json


from collect import AppForm

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = AppForm()  #AppForm subclass inherits everything (method, variable) from the superclass View
        view.inputs = [['title', 'text', 'movie'],['submit','Submit']]  #array of inputs can be reuse
        self.response.write(view.print_out_form())
        #get information from urllib2 library to request the url
        if self.request.GET:  #if is a request look for key=actor return show_title, movie_cast, movie_director, and movie_poster of the actor requested.
           if self.request.GET:
               title = self.request.GET['title']
               url = "http://netflixroulette.net/api/api.php?title=" + title
               request = urllib2.Request(url)  #variable request value: python class library request url "http://netflixroulette.net/api/api.php?actor="
               opener = urllib2.build_opener()
               result = opener.open(request)

               #parse json
               jsondoc = json.load(result)#json load result
               movie = jsondoc['show_title']
               movie_cast = jsondoc['show_cast']
               movie_director = jsondoc['director']
               movie_category = jsondoc ['category']
               movie_summary = jsondoc ['summary']
               movie_year = jsondoc['release_year']
               self.response.write("Movie:   " + movie   + "<br/>" + "Cast:   " + movie_cast  + "<br/>" + "Director:    " + movie_director + "<br/>" + "Category:   " + movie_category + "<br/>" +  "Summary:    " + movie_summary + "<br/>" "Year   "  + movie_year)

           else:
               self.response.write(view.head + view.body + view.close)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
