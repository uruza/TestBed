
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#-----------------------------------------------------------------------------------------
class Persion(db.Model):
    name = db.StringProperty()
    area = db.StringProperty()

#-----------------------------------------------------------------------------------------
class DataReceive(webapp.RequestHandler):
    def get(self):
        info = Persion()
        info.name = self.request.get("Name")
        info.area = self.request.get("Area")
        info.put()
        
        self.response.out.write('Input Success')

#-----------------------------------------------------------------------------------------
class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Analysis Main Page')

#-----------------------------------------------------------------------------------------
class TestPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Analysis Test Page')

#-----------------------------------------------------------------------------------------
def NameKey( name=None ):
  """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
  return db.Key.from_path('Name', name or 'default_name')

#-----------------------------------------------------------------------------------------
class ReportPage(webapp.RequestHandler):
    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
 #       self.response.out.write('Analysis Report Page')
        print db.GqlQuery( "SELECT * "
                           "FROM Persion "
                           "WHERE Name" )

#        find = db.GqlQuery( "SELECT * "
#                            "FROM Persion "
#                            "WHERE Name",
#                            'Woojin' )

#        find.name
#        self.response.out.write( find.name )

#-----------------------------------------------------------------------------------------
application = webapp.WSGIApplication( [ ('/main', MainPage),
                                        ('/report', ReportPage),
                                        ('/test', TestPage),
                                        ('/.*', DataReceive)  ],
                                      debug=True )

#-----------------------------------------------------------------------------------------
def main():
    run_wsgi_app(application)

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#-----------------------------------------------------------------------------------------
