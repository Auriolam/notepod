#Base made with tutorial from https://www.instructables.com/Create-a-Simple-Python-Text-Editor/
#Written by  PumpkinSmasher
#Additions by Mikko below
#Fixed calls for tkinter. (Guides tk inter calls outdated)
#Completely different saving function.
#My own UI




import os
import sys
v=sys.version_info


from tkinter import *
from tkinter import filedialog

root=Tk("Text Editor")
#root.geometry("650x250")


#Functions----------------------------------------------------------------------------------------------------
def clear_text():
   text.delete("1.0", "end-1c")
   entryname.delete(0,END)

def saveas():

    global text
    header = entryname.get()

    t = text.get("1.0", "end-1c")
    file1=open("lastopentext.txt", "w+")
    file1.write(header+"."+t)
    file1.close()

def write_to_textfile():
    global text
    entrytext = entryname.get()
    newdirarray = []
    filelist = ""
    if entrytext == "":
        dir_list = os.listdir()
        for file in dir_list:
            #print(file)
            dirdot=file.find(".")
            if dirdot != -1:
                #print(dirdot)
                nameoffile = file[:dirdot]
                #print(nameoffile)
                newdirarray += [nameoffile]
            else:
                newdirarray += [file]
        for file in newdirarray:
            if file.isnumeric():
                filelist += file
                #print(file.isnumeric())

        lenghtfile=len(filelist)
        #print(lenghtfile)
        #print("filelist yllä")
        lenghtfileint=int(lenghtfile)
        entrytext=(lenghtfileint+1)

    #print(newdirarray)
    #print(entrytext)
    teksti = text.get("1.0", "end-1c")
    tiedosto = str(entrytext)+".txt"
    file= open(tiedosto,"w+")
    file.write(teksti)

def read_from_textfile(tiedosto):
    global vanhateksti
    global header
    file=open(tiedosto, "r")
    print(file)
    data = file.read()
    print(data)
    datadot=data.find(".")
    print(datadot)
    header=data[:datadot]
    vanhateksti = data[datadot+1:]
    print("data^^")
    print(header)



def last_open():
    saveas()
    root.destroy()
def open_last_open():
    read_from_textfile("lastopentext.txt")
    

#Setups --------------------------
open_last_open()
text=Text(root, height=20, width=30, yscrollcommand=set())
root.title("SP")
text.grid(row=1, column=0, columnspan = 3)
text.insert("1.0",vanhateksti)
root.resizable(False,False)

buttonsave=Button(root, text="Save", command=write_to_textfile)
buttonsave.grid(row=3, column=1, pady=0, padx=0) 

buttonscrap=Button(root,text="scrap and new", command=clear_text)
buttonscrap.grid(row=3, column=0, pady=0, padx=0)

labelname=Label(root, text = "Filename")
labelname.grid(row=2, column=0, pady=0, padx=0)

entryname=Entry(root)
entryname.insert(0,header)
entryname.grid(row = 2, column =1, pady = 1, padx=0)

root.protocol("WM_DELETE_WINDOW", last_open)
root.mainloop()
