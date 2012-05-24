
import sys
from tkinter import *
from tkinter.filedialog import askopenfilename
import data

userData = data.Data( 'data.xml' )


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def FindGamePath():
   gamePath = askopenfilename()
   EntryGamePath.delete( 0, END )
   EntryGamePath.insert( 0, gamePath )


from xml.dom.minidom import parse
import xml.dom.minidom

dom1 = parse( 'data.xml' )
print ( dom1 )
element = dom1.getElementsByTagName( 'aa' )
print ( element )

def Start():
   """StartWin = Toplevel(root)
   label = Label( StartWin, text="시작 합니다.")
   label.pack(side = LEFT)"""
   file = open( 'data.xml', '+r' )
   data = file.read()
   file.close()
   dom = xml.dom.minidom.parseString( data )
   coll = dom.documentElement
   print( coll )

   if coll.hasAttribute( "bb" ):
      print( "Root element : %s" % coll.getAttribute("bb") )

   
root = Tk()
root.title("Auto Play & Auto Profiling")
root.geometry("500x250")
root.resizable(0,0)

menubar = Menu( root )
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="설정", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="기타", command=donothing)
menubar.add_cascade(label="도구", menu=filemenu)

root.config(menu=menubar)

labelGamePath = Label( root, text="게임실행파일 경로 : ")
labelGamePath.place( x=2, y=5 )
EntryGamePath = Entry(root, bd = 3)
EntryGamePath.place( width = 300, x = 120, y = 5 )
EntryGamePath.insert( 0, userData.gamePath )
btnFind = Button( root, text="...", command = FindGamePath )
btnFind.place( x = 422, y = 5 )

labelID = Label( root, text="아이디                 : ")
labelID.place( x = 2, y = 35 )
EntryID = Entry(root, bd = 3)
EntryID.place( width = 100, x = 120, y = 35 )
EntryID.insert( 0, userData.userID )

labelPass = Label( root, text="패스워드              : ")
labelPass.place( x = 2, y = 65 )
entryPass = Entry(root, bd = 3)
entryPass.place( width = 100, x = 120, y = 65 )
entryPass.insert( 0, userData.userPass )

labelServer = Label( root, text="서버                    : ")
labelServer.place( x = 2, y = 95 )
entryServer = Entry(root, bd = 3)
entryServer.place( width = 100, x = 120, y = 95 )
entryServer.insert( 0, userData.server )

btnStart = Button( root, text="시작", command = Start )

btnStart.place( height = 50, width = 300, x = 100, y = 150 )

root.mainloop()
