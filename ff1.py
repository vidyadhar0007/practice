import copy
student_details=["kiran",21,[77,69,99]]
student_details1=copy.deepcopy(student_details)
student_details[2][2]=100
print(student_details1)
