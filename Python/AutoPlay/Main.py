
from tkinter import *
import UserData
import UserDataForm
import UserDataIO
import UserDataIO.saveXML

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def Start():
   StartWin = Toplevel(root)
   label = Label( StartWin, text="시작 합니다.")
   label.pack(side = LEFT)
   userData.gamePath = userDataForm.EntryGamePath.get()
   userData.userID = userDataForm.EntryID.get()
   userData.userPass = userDataForm.entryPass.get()
   userData.server = userDataForm.entryServer.get()
   UserDataIO.saveXML( userData )
   
   
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

userData = UserData.UserData
UserDataIO.UserDataIO( userData, 'data.xml' )
userDataForm = UserDataForm.UserDataForm( root, userData )

btnStart = Button( root, text="시작", command = Start )
btnStart.place( height = 50, width = 300, x = 100, y = 150 )

root.mainloop()
