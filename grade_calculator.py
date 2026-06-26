def calculate_average(marks):
    return sum(marks)/len(marks)
def get_grade(average):
    if average>=90:
        return "A"
    elif average>=75:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"
def get_result(grade):
    if grade=="F":
        return "FAIL"
    else:
        return "PASS"
    
student_name=input("Enter student name: ")
num_subjects=int(input("Enter number of subjects: "))
marks=[]
for i in range(num_subjects):
    mark=int(input(f"Enter marks  for subjects {i+1}: "))
    marks.append(mark)

average=calculate_average(marks)
grade=get_grade(average)
result=get_result(grade)

print("\n==== RESULT CARD ====")
print("Name:", student_name)
print("Marks:",marks)
print("Average:",average)
print("Grade:",grade)
print("Result",result)
print("=============================")