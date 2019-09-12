fib=0
j=1
k=0
n=int(input("How many fibonacci numbers do you need? :"))
for i in range(n):
    print("{0}: {1:>20}".format(i+1,fib))
    fib=j+k
    j=k
    k=fib
