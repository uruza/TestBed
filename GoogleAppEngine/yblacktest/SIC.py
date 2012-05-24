import os
import urllib

from google.appengine.ext import blobstore
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import SICDB

class MainHandler(webapp.RequestHandler):
    def get(self):      
	
        info = SICDB.SystemInfo()
        
	# Client System Info
        info.OS = self.request.get("OS")
        info.CPU = self.request.get("CPU")
        info.Core = int(self.request.get("Core"))
        info.RAM = int(self.request.get("RAM"))
        # info.resolution_x = int(self.request.get('res_x')) 
        # info.resolution_y = int(self.request.get('res_y'))
        info.GPU = self.request.get("GPU")
        info.VRAM = int( self.request.get("VRAM") )
        info.VertexShader = self.request.get("VertexShader")
        info.PixelShader = self.request.get("PixelShader")

        # GameOption Info
	info.ResolutionX = int( self.request.get("ResolutionX") )
	info.ResolutionY = int( self.request.get("ResolutionY") )
	info.Shadow = int( self.request.get("Shadow") )
	info.DynamicBright = bool( self.request.get("DynamicBright") )
		
	# Profile Info
	info.Act = int( self.request.get("Act") )
	info.Stage = int( self.request.get("Stage") )
	info.Difficulty = int( self.request.get("Difficulty") )
	info.NumPlayer = int( self.request.get("NumPlayer") )
	info.FPS = float( self.request.get("FPS") )
	info.MaxSPF = float( self.request.get("MaxSPF") )
	info.OverFrameRate = float( self.request.get("OverFrameRate") )
        info.ClientVersion = self.request.get("ClientVersion")
        
        info.put()
        self.response.out.write('ok')
	
        
def main():
    application = webapp.WSGIApplication(
          [('/', MainHandler),
          ], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
	main()
