students={"student1":{
    "name":"sharan",
    "marks":[99,69,77]
    },
    "student2":{
    "name":"soorya",
    "marks":[90,69,50]
    },
    "student3":{
        "name":"kiran",
        "marks":[90,78,57]
    }

    }
print(students.get("student1").get("name"))
print(students.get("student2").get("marks")[1])
print(students.get("student3").get("marks")[2])
for mark in students.get("student1").get("marks"):
    print(mark)

print(sum(students.get("student2").get("marks")))
print(sum(students.get("student2").get("marks"))/len(students.get("student2").get("marks")))
for names in students.keys():
    print(students.get(names).get("name"))
for name_avg in students.keys():
    print(students.get(name_avg).get("name"),sum(students.get(name_avg).get("marks"))/len(students.get(name_avg).get("marks")))