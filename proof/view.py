#Ednalda Fakira
#Assigment: Proof of Concept
#Course:Design Patterns for Web Programming
#Instructor: Rebecca Carroll


#MVC = v(view)
class AppView(object):#superclass
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

        self.close = """


   </body>
 </html>
       """


    def print_out_view(self):
        all = self.head + self.body + self.close
        all = all.format(**locals())
        return all

