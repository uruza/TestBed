
from tkinter import *
from tkinter.filedialog import askopenfilename

class UserDataForm:
    def __init__ ( self, parent, userData ):
        self.labelGamePath = Label( parent, text="게임실행파일 경로 : ")
        self.labelGamePath.place( x=2, y=5 )
        self.EntryGamePath = Entry(parent, bd = 3)
        self.EntryGamePath.place( width = 300, x = 120, y = 5 )
        self.EntryGamePath.insert( 0, userData.gamePath )
        self.btnFind = Button( parent, text="...", command = self.FindGamePath )
        self.btnFind.place( x = 422, y = 5 )

        self.labelID = Label( parent, text="아이디                 : ")
        self.labelID.place( x = 2, y = 35 )
        self.EntryID = Entry(parent, bd = 3)
        self.EntryID.place( width = 100, x = 120, y = 35 )
        self.EntryID.insert( 0, userData.userID )

        self.labelPass = Label( parent, text="패스워드              : ")
        self.labelPass.place( x = 2, y = 65 )
        self.entryPass = Entry(parent, bd = 3)
        self.entryPass.place( width = 100, x = 120, y = 65 )
        self.entryPass.insert( 0, userData.userPass )

        self.labelServer = Label( parent, text="서버                    : ")
        self.labelServer.place( x = 2, y = 95 )
        self.entryServer = Entry(parent, bd = 3)
        self.entryServer.place( width = 100, x = 120, y = 95 )
        self.entryServer.insert( 0, userData.server )


    def FindGamePath( self ):
        gamePath = askopenfilename()
        self.EntryGamePath.delete( 0, END )
        self.EntryGamePath.insert( 0, gamePath )
