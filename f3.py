def calculate_marks(sub1,sub2,sub3):
    Total=sub1+sub2+sub3
    Avg=Total/3
    return Total,Avg
output=calculate_marks(70,90,77)
print("Total marks:",output[0])
print("Avg:",output[1])