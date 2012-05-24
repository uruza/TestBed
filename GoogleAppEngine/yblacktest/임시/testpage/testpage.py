# print "Welcome to Test Page"

# print 'Content-Type: text/plain'
#print ''
#print 'Hello, world!'

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<html><body>')
        self.response.out.write('</body></html>')

        SystemInfo = db.GqlQuery( "SELECT * FROM SystemInfo" )

#        self.response.out.write(
 #           '<b>%s</b> wrote:' % SystemInfo)


            

application = webapp.WSGIApplication(
                                     [('/testpage', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
