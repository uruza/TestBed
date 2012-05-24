
from google.appengine.ext import db

class SystemInfo(db.Model):
    # Client System Info
    OS = db.StringProperty()
    CPU = db.StringProperty()
    Core = db.IntegerProperty()
    RAM = db.IntegerProperty()
    # resolution_x = db.IntegerProperty()
    # resolution_y = db.IntegerProperty()
    GPU = db.StringProperty()
    VRAM = db.IntegerProperty()
    VertexShader = db.StringProperty()
    PixelShader = db.StringProperty()
	
	
    # GameOption Info
    ResolutionX = db.IntegerProperty()
    ResolutionY = db.IntegerProperty()
    Shadow = db.IntegerProperty()
    DynamicBright = db.BooleanProperty()

    # Profile Info
    Act = db.IntegerProperty()
    Stage = db.IntegerProperty()
    Difficulty = db.IntegerProperty()
    NumPlayer = db.IntegerProperty()
    FPS = db.FloatProperty()
    MaxSPF = db.FloatProperty()
    OverFrameRate = db.FloatProperty()
    ClientVersion = db.StringProperty()
    
    

