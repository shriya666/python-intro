
import os
options=input("Do you want to create new note (type a), delete a note (b), edit a note(c) or print a note(d)? ").lower()
if options== "a":
    name="notesdata/"+ input("name your file ") + ".note"
    f=open(name, "w")
    write=input("write: ")
    f.write(write)
    f.close()
elif options=="b":
    thelist=os.listdir("notesdata")
    print(thelist)
    pick="notesdata/"+input("Pick one ") +".note"
    if os.path.isfile(pick):
        os.remove(pick)
    else:
        print("404 Error. File not found ")c
elif options=="c":
    thelist=os.listdir("notesdata")
    print(thelist)
    pick="notesdata/"+input("Pick one ") +".note"
    if not os.path.isfile(pick):
        print("404 Error. File not Found")
    else:
        f=open(pick, "a")
        write=input("write: ") +"\n"
        f.write(write)
        f.close()
elif options=="d":
    alist=os.listdir("notesdata")
    



