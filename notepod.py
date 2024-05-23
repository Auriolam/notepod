#
#Making a python project, where I try do make a small notepad program
#
#1. making program to write .txt files.
#2. Read textfiles
#3. only need to read last open .txt
#4. Renaming .txt file
#5. removing open .txt
#6. gui
#7. button for save, makenew (and save last), scrap (and make new)
#8. ??
import os

print("hello world")

#test = input("Write text: ")
#print(test)
def write_to_textfile(tiedosto,teksti):
    tiedosto = tiedosto+".txt"
    teksti
    file= open(tiedosto,"w+")
    file.write(teksti)

def read_from_textfile():
    tiedosto = input("nimi: ")
    file=open("tiedosto", "a+")


def removefile():
    delfile = input("Delfile y/n: ")
    tiedosto = input("nimi: ")
    if delfile == "y":
        try:
            os.remove(tiedosto+".txt")
        except OSError as e:
            # If it fails, inform the user.
            print("Error: %s - %s." % (e.filename, e.strerror))
    else:
        return
    
def main():
    aloitus = input("uusi, lue, poistu u/l/p: ")
    while aloitus != "p":
        if aloitus == "u":
            tiedosto = input("Syötä nimi: ")
            teksti =  input("Syötä sisältö: ")
            write_to_textfile(tiedosto, teksti)
            removefile()
        elif aloitus == "l":
            read_from_textfile()
         
        aloitus = input("uusi, lue, poistu u/l/p: ")

main()
