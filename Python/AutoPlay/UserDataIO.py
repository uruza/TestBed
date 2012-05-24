
from xml.dom.minidom import parse
import UserData

class UserDataIO:
    def __init__ ( self, userData, filePath ):
        dom = parse( filePath )
        userData.gamePath = dom.getElementsByTagName( 'GAME_PATH' )[0].childNodes[0].data
        userData.userID = dom.getElementsByTagName( 'ID' )[0].childNodes[0].data
        userData.userPass = dom.getElementsByTagName( 'PASS' )[0].childNodes[0].data
        userData.server = dom.getElementsByTagName( 'SERVER' )[0].childNodes[0].data

    def saveXML ( self, userData ):
        dom.getElementsByTagName( 'GAME_PATH' )[0].childNodes[0].data = userData.gamePath
        dom.getElementsByTagName( 'ID' )[0].childNodes[0].data = userData.userID
        dom.getElementsByTagName( 'PASS' )[0].childNodes[0].data = userData.userPass
        dom.getElementsByTagName( 'SERVER' )[0].childNodes[0].data = userData.server
        dom.saveXML()

aaa = UserDataIO

bbb = UserData.UserData


aaa.saveXML(  )
        
