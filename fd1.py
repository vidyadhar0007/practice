#sum
def sumnum(*numbers):
    print(sum(numbers))
sumnum(10,20,30,40,34)
#largest
def largest(*args):
    print(max(args))
largest(10,20,30,40,34)
#arg one by one
def largest(*args):
    for i in args:
        print(i)
largest(10,20,30,40,34)
#count of args
def counts(*args):
    print(len(args))
counts("v",1,7,True,7.7)

#seperation even add
def seperates(*args):
    even=[]
    odd=[]
    for i in args:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("even:",even[0:])
    print("odd:",odd[0:])
seperates(1,2,3,4,5,6,7,8,9,10)
