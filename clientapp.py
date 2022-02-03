from tkinter import *
import client

def connect():
    client.client1()


main = Tk()
main.title("MyApp")
menubar = Menu(main)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")
file.add_separator()
file.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")
menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)

frame = Frame(main, width=500, height= 400)
frame.pack()
main.config(menu=menubar)

btn1= Button(frame,text="Connect",command=connect)
btn1.place(x=10,y=30)



main.mainloop()
