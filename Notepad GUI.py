from tkinter import *
import tkinter .messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
#save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File saved")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
         
         
        
         
      
           
            
def quitApp():
    root.destroy()#destroy window
def cut():
    TextArea.event_generate(("<<Cut>>"))#automactically work like cut
def copy():
    TextArea.event_generate(("<<Copy>>"))#automactically work like copy
def paste():
    TextArea.event_generate(("<<Paste>>"))#automactically work like paste
def about():
    tmsg.showinfo("Notepad","Notepad by Ankur")
    
if __name__=='__main__':
    root=Tk()
    root.title("Ankur ka Notepad")
    root.geometry("644x788")
#Add Textarea
    TextArea=Text(root, font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
#Lets create a menubar
    Menubar=Menu(root)
    #Filemenu starts
    Filemenu=Menu(Menubar, tearoff=0)
#To open new file    
    Filemenu.add_command(label="New",command=newfile)
#To open already existing file
    Filemenu.add_command(label="open",command=openfile)
#To save th ecurrent file
    Filemenu.add_command(label="Save",command=savefile)
    Filemenu.add_separator()
    Filemenu.add_command(label="exit",command=quitApp)
    Menubar.add_cascade(label="File",menu=Filemenu)#everythjing come inside the File .
    #Filemenu ends

    
    #Edit menu starts
    EditMenu=Menu(Menubar,tearoff=0)
#To give feature of cut,copy and paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    Menubar.add_cascade(label="Edit",menu=EditMenu)
    #Editmenu ends   


    #Helpmenu starts
    Helpmenu=Menu(Menubar,tearoff=0)
    Helpmenu.add_command(label="About Notepad",command=about)
    Menubar.add_cascade(label="Help", menu=Helpmenu)
    
    

    root.config(menu=Menubar)
#Adding scrollbar
    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    
    
    root.mainloop()

