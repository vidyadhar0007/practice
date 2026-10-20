a=[10,20,30]
b=a
c=[10,20,30]
print(a is b)
print(a is c)
print(a == c)
print(a is not c)
b.append(40)
print(a,b)
