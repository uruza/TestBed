import configparser

#-------------------------------------------------------------------------------
class FieldInfo:    

    def __init__( self ):
        self.name
        self.value

#-------------------------------------------------------------------------------
class UnitInfo:
    
    def __init__( self, name ):
        self.name = name
        self.count = 0
        self.fields = []

    def add( self, value ):
        self.count++
        self.fields.get
        

#-------------------------------------------------------------------------------
class TotalInfo:
    
    def __init__( self ):
        self.list = []
        self.unitInfo = UnitInfo('VS10')
        
    def addInfo( self, sysInfo ):
        self.list.append( sysInfo )

    def calculate( self ):
        for each_t in self.list:
            self.unitInfo.add( each_t.vs10 )
            
            

#-------------------------------------------------------------------------------
class UserSystemInfo:
    def __init__( self ):
        print()
    def setVS10( self, value ):
        self.vs10 = value
    def setVS11( self, value ):
        self.vs11 = value
    def setVS20( self, value ):
        self.vs20 = value
    def setVS30( self, value ):
        self.vs30 = value
    def setPS10( self, value ):
        self.ps10 = value
    def setPS11( self, value ):
        self.ps11 = value
    def setPS20( self, value ):
        self.ps20 = value
    def setPS30( self, value ):
        self.ps30 = value

#-------------------------------------------------------------------------------
def readFile( filePath ):
    config = configparser.RawConfigParser()
    config.read( filePath )

    sysInfo = UserSystemInfo()

    sysInfo.setVS10( config.get( 'GraphicCardInfo', 'VS 1.0' ) )
    sysInfo.setVS11( config.get( 'GraphicCardInfo', 'VS 1.1' ) )
    sysInfo.setVS20( config.get( 'GraphicCardInfo', 'VS 2.0' ) )
    sysInfo.setVS30( config.get( 'GraphicCardInfo', 'VS 3.0' ) )

    sysInfo.setPS10( config.get( 'GraphicCardInfo', 'PS 1.0' ) )
    sysInfo.setPS11( config.get( 'GraphicCardInfo', 'PS 1.1' ) )
    sysInfo.setPS20( config.get( 'GraphicCardInfo', 'PS 2.0' ) )
    sysInfo.setPS30( config.get( 'GraphicCardInfo', 'PS 3.0' ) )

    return sysInfo

#-------------------------------------------------------------------------------

def printInfo( sysInfo ):
    print( '---------------------------------------------' )
    print( 'VS_1_0 =', sysInfo.vs10 )
    print( 'VS_1_1 =', sysInfo.vs11 )
    print( 'VS_2_0 =', sysInfo.vs20 )
    print( 'VS_3_0 =', sysInfo.vs30 )
    print( 'PS_1_0 =', sysInfo.ps10 )
    print( 'PS_1_1 =', sysInfo.ps11 )
    print( 'PS_2_0 =', sysInfo.ps20 )
    print( 'PS_3_0 =', sysInfo.ps30 )
    print( '---------------------------------------------' )
    
#-------------------------------------------------------------------------------
if __name__ == "__main__" :
#   iniPath = "E:\[Test]\TestCode\Python\HardwareResearch\Data\ClientSystemInfo.ini"
    iniPath2 = 'Data\ClientSystemInfo (2).ini'
    iniPath3 = "Data\ClientSystemInfo (3).ini"
    iniPath4 = "Data\ClientSystemInfo (4).ini"

#    sysInfoList = []
#    sysInfoList.append( readFile( iniPath2 ) )
#    sysInfoList.append( readFile( iniPath3 ) )
#    sysInfoList.append( readFile( iniPath4 ) )

#    for each_t in sysInfoList:
#        printInfo( each_t )

    totalInfo = TotalInfo()    
    totalInfo.addInfo( readFile( iniPath2 ) )
    totalInfo.calculate()
    
    
    





























