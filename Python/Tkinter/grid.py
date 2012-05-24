from tkinter import *

root = Tk()

Label(root, text="Label 1").grid( column=0, row=0 )
Label(root, text="Label 2").grid( column=0, row=1 )

Entry( root ).grid( column=1, row=0 )
Entry( root ).grid( column=1, row=1 )

root.mainloop()
