#Ednalda Fakira
#Assigment: Proof of Concept
#Course:Design Patterns for Web Programming
#Instructor: Rebecca Carroll

class AppView(object):
    def __init__(self):
        self.title = "MovieNight!"
        self.css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
 <html>
   <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css" />
   </head>
   <body>
        """

        self.body = ''' <div id ="page">
                            <header>
                              <nav><h1>MovieNight</h1></nav>
                              <h2>Search movies by Actor</h2>
                            </header>
                            <div id="content">

                            </div>
                        </div>

                      '''
        #self.query ='''
                   #<h3>Movie: <p>self.query.show_title</p></h3>
                   #<h3>Cast:  <p>self.query.show_cast</p></h3>
                   #<h3>Director: <p>self.query.director</p></h3>
                   #<h3>Director: <p>self.query.category</p></h3>
                   #<h3>Director: <p>self.query.summary</p></h3>
                   #<p>self.query.poster</p>
        # '''
        self.close = """

                    <div id="footer"><a href="#">MovieNight</a></div>
   </body>
 </html>
       """


    def print_out_view(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

