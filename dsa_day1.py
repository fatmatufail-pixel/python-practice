numbers=[8,3,7,4,6,5]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print("Largest",largest)
reversed_list=[]
for i in range(len(numbers)-1,-1,-1):
    reversed_list.append(numbers[i])
print(reversed_list)