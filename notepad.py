from tkinter import *
from datetime import datetime
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

root=Tk()
root.geometry("450x450")
root.title("Untitled-Dazzler's Notepad v1.0")
root.wm_iconbitmap("l.ico")

#function

#file menu function
def new():
    global result
    root.title("Untitled- Dazzler's Notepad v1.0 ")
    result=None
    textArea.delete(1.0,END)
def openfile():
    result=filedialog.askopenfilename(title="select file to open",defaultextension=".txt",filetypes=[("text files","*.txt"),("all files","*.*")])
    if result =="":
        result=None
    else:
        root.title(os.path.basename(result)+"- Dazzler's Notepad v1.0")
        textArea.delete(1.0,END)
        readfile=open(result,"r")
        for line in readfile:
                     textArea.insert(END,line)
        readfile.close()

def save():
        f=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        f.write(textArea.insert(1.0,END))
        f.close()

#edit menu fuction
def cut():
    textArea.event_generate(("<<Cut>>"))
def copy():
    textArea.event_generate(("<<Copy>>"))
def paste():
    textArea.event_generate(("<<Paste>>"))

#help menu function
def about():
    showinfo("Notepad","By Farhan Dazzler")
def more():
    showinfo("Follow us","https://www.instagram.com/farhan_dazzler/ \n https://www.facebook.com/farhan.mohammed.5836")

#Text Area

textArea=Text(root,bg="gray1",fg="firebrick1",font="Comisansms 15 ",insertbackground="firebrick2")
textArea.pack(expand="true",fill="both")
#adding scrollbar
scrollbar=Scrollbar(textArea)
scrollbar.pack(side="right",fill="y")
scrollbar.config(command=textArea.yview)
textArea.config(yscrollcommand=scrollbar.set)



#date and time


def date_time():
           # datetime object containing current date and time
            now = datetime.now()



            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
           # textArea.insert("date and time =", dt_string)

            w = Label(textArea, text=dt_string, fg="white", bg="black", font=("helvetica", 20))
            w.pack()


#menu
menubar=Menu(root)

#File Menu
file=Menu(menubar,tearoff=0)
file.add_command(label="New",command=new)
file.add_command(label="Save",command=save)
file.add_command(label="Open..." ,command=openfile)
file.add_separator()
file.add_command(label="Exit",command=quit)
menubar.add_cascade(label="File",menu=file)
root.config(menu=menubar)


#Edit Menu
edit=Menu(menubar,tearoff=0)
edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=copy)
edit.add_command(label="Paste",command=paste)
edit.add_separator()
edit.add_command(label="Date and time",command=date_time)

menubar.add_cascade(label="Edit",menu=edit)
root.config(menu=menubar)

#Help menu
help=Menu(menubar,tearoff=0)
help.add_command(label="About Dazzler Notepad",command=about)
help.add_command(label="More About",command=more)
menubar.add_cascade(label="Help",menu=help)
root.config(menu=menubar)



root.mainloop()
