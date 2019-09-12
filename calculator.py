def addition(numberone, numbertwo):
    return numberone+numbertwo
def subtraction(numberone, numbertwo):
    return numberone-numbertwo
def multiplication(numberone, numbertwo):
    return numberone*numbertwo
def division(numberone, numbertwo):
    return numberone/numbertwo
numone=0
numtwo=0
op=None
while True:
    try:
        numone=int(input("Enter a number (or a letter to exit): "))
        op=input("Enter an operation: ")
        numtwo=int(input("Enter another number : "))
        if op=="+":
            print("The result of the addition is: {0}".format(addition(numone,numtwo)))
        elif op=="-":
            print("The result of the subtraction is: {0}".format(subtraction(numone,numtwo)))
        elif op=="*":
            print("The result of the multiplication is: {0}".format(multiplication(numone,numtwo)))
        elif op=="/":
            print("The result of the division is: {0}".format(division(numone,numtwo)))
    except ValueError:
        quit()

