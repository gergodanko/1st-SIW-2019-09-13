import random


x="y"
while x=="y" or x=="Y":
    attacker=[]
    defender=[]
    attunit=0
    defunit=0
    natt=0
    ndef=0
    
        
    while natt==0 or natt>3 :
        while True:
            try:
                natt=int(input("How many units attack? :"))
                break
            except:
                print("That's not a valid input!")
                
       
    while ndef==0 or ndef>2:
        while True:
            try:
                ndef=int(input("How many units defend? :"))
                break
            except :
                print("That's not a valid input!")


    for i in range(natt):
        attacker.append(random.randrange(1,7))
    for i in range(ndef):
        defender.append(random.randrange(1,7))
    attacker.sort(reverse=True)
    defender.sort(reverse=True)
    print("Dice:\n Attacker:")
    for k in attacker:
        print(k,end=" ")
    print(" \n Defender:")
    for l in defender:
        print(l,end=" ")
    if ndef<=natt:
        for j in range(ndef):
            if defender[j]>=attacker[j]:
                attunit+=1
            elif attacker[j]>defender[j]:
                defunit+=1
    elif natt<ndef:
        for j in range(natt):
            if defender[j]>=attacker[j]:
                attunit+=1
            elif attacker[j]>defender[j]:
                defunit+=1
    

    #print("Dice: \n Attacker: {0}\n Defender: {1}".format(attacker,defender))
    print("\nOutcome:\n Attacker: Lost {0} units\n Defender: Lost {1} units".format(attunit,defunit))
    x=input('Do you want to roll the dice again? "y" or "n" : ')
