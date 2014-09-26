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
        view = AppForm()
        view.inputs = [['actor', 'text', 'actor'],['Submit','Submit']]#can be reuse
        self.response.write(view.print_out_form())
        #get information from urllib2 library to request the url
        if self.request.GET:#if is a request look for key=actor write  movie title and  movie category
           actor = self.request.GET['actor']
           url = "http://netflixroulette.net/api/api.php?actor=" + actor
           request = urllib2.Request(url)
           opener = urllib2.build_opener()
           result = opener.open(request)

           #parse json
           jsondoc = json.load(result)#json load result from the request url and write out as variable value of movie, movie_cast, movie_director, and movie_poster
           movie = jsondoc['show_title']
           movie_cast = jsondoc['show_cast'][0, 1]
           movie_director = jsondoc['director']
           movie_poster = jsondoc['poster']
           self.response.write("Movie " + movie + "Cast " + movie_cast + "Director " + movie_director + "<br/>" + movie_poster)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
