student={"name":"Fatma","age":22,"branch":"ECE","college":"DSCE"}
print(student["name"])
student["cgpa"]=8.5
student["age"]=23
print(student)
del student["cgpa"]
print(student)
for key,value in student.items():
    print(key,":",value)