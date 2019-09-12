import sys
def hello_name():
    '''
    Prints out "Hello 'name'! ", name given by user as command line argument
    If there is no argument it prints "Hello World!"   
     '''
    try:
        print("Hello {0}!".format(sys.argv[1]))
    except IndexError:
        print("Hello World!")

hello_name()

