numbers=[1,2,3,2,4,2,5]
target=2
count=0
for num in numbers:
    if num==target:
        count+=1

print("Count:", count)

seen=[]
duplicates=[]
for num in numbers:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

print("Duplicates",duplicates)