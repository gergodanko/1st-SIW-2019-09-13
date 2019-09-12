import sys
ideabank=open("ideabank.txt", "a+")
ideabankr=open("ideabank.txt","r")
c=1
try:
    if sys.argv[1]=="--help":
        print("--list : Listing all the ideas in your ideabank\n--delete # : Remove an idea by the id of it.")
        quit()
    elif sys.argv[1]=="--list":
        for idea in ideabankr.readlines():
            print("{0}. {1}".format(c,idea))
            c+=1
        quit()
    #elif sys.argv[1]=="--delete":
        #ideabankw=open("ideabank.txt","w")
        #idearead=ideabankr.readlines()
        #x=1
        #for i in range(len(idearead)):
            #if i==(x-1):
                #idearead.pop(i)
            #else:
                #continue
        #for lines in idearead:
            #ideabankw.write(lines)
            
        #for idea in idearead:
            #print("{0}. {1}".format(c,idea))
            #c+=1
        #quit()
    
except IndexError:
    pass

ideabank.writelines("\n"+input("What is your new idea? : "))
ideabank.close()
print("\nYour ideabank:\n")
for idea in ideabankr.readlines():
    print("{0}. {1}".format(c,idea))
    c+=1
ideabankr.close()
