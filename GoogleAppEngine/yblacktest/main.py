
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from myDataStore import Person

#-----------------------------------------------------------------------------------------
class ReportHandler(webapp.RequestHandler):
    def get(self):
        que = db.Query(Person)
        print que
#-----------------------------------------------------------------------------------------
class DataReceiveHandler(webapp.RequestHandler):
    def get(self):
        info = Person()
        info.name = self.request.get("Name")
        info.area = self.request.get("Area")
        info.put()
        
        self.response.out.write('Input Success')
    
#-----------------------------------------------------------------------------------------
class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write( 'Welcome to yblack test' )

#-----------------------------------------------------------------------------------------
def main():
    application = webapp.WSGIApplication( [ ('/dataReceive/.*', DataReceiveHandler),
                                            ('/report', ReportHandler),
                                            ('/.*', MainHandler) ],
                                          debug=True )
    run_wsgi_app(application)

#-----------------------------------------------------------------------------------------
if __name__ == '__main__':
	main()

#-----------------------------------------------------------------------------------------
