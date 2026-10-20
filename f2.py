#intersection
l1=[10,40,50,55]
l2=[45,10,50,34]
l3=[]
for element in l1:
    if element in l2 and element not in l3:
        l3.append(element)
print(l3) 