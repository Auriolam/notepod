#Base made with tutorial from https://www.instructables.com/Create-a-Simple-Python-Text-Editor/
#Written by  PumpkinSmasher
#Fixed calls for tkinter. (Guides tk inter calls outdated)
#



import os
import sys
v=sys.version_info


from tkinter import *
from tkinter import filedialog

root=Tk("Text Editor")
#root.geometry("650x250")

text=Text(root, height=20, width=30, yscrollcommand=set())
root.title("SP")
text.grid(row=1, column=0, columnspan = 3)
root.resizable(False,False)
def clear_text():
   text.delete("1.0", "end-1c")
   entryname.delete(0,END)

def saveas():

    global text

    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def write_to_textfile():
    global text
    entrytext = entryname.get()
    newdirarray = []
    filelist = ""
    if entrytext == "":
        dir_list = os.listdir()
        for file in dir_list:
            print(file)
            dirdot=file.find(".")
            if dirdot != -1:
                print(dirdot)
                nameoffile = file[:dirdot]
                print(nameoffile)
                newdirarray += [nameoffile]
            else:
                newdirarray += [file]
        for file in newdirarray:
            if file.isnumeric():
                filelist += file
                print(file.isnumeric())

        lenghtfile=len(filelist)
        print(lenghtfile)
        print("filelist yllä")
        lenghtfileint=int(lenghtfile)
        entrytext=(lenghtfileint+1)
        
    print(newdirarray)
    print(entrytext)
    teksti = text.get("1.0", "end-1c")
    tiedosto = str(entrytext)+".txt"
    file= open(tiedosto,"w+")
    file.write(teksti)

buttonsave=Button(root, text="Save", command=write_to_textfile)
buttonsave.grid(row=3, column=1, pady=0, padx=0) 

buttonscrap=Button(root,text="scrap and new", command=clear_text)
buttonscrap.grid(row=3, column=0, pady=0, padx=0)

labelname=Label(root, text = "Filename")
labelname.grid(row=2, column=0, pady=0, padx=0)

entryname=Entry(root)
entryname.grid(row = 2, column =1, pady = 1, padx=0)


root.mainloop()