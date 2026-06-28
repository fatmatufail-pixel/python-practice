numbers=[3,7,1,9,4,6]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
second_largest=numbers[0]
for num in numbers:
    if num>second_largest and num<largest:
        second_largest=num
print("Second largest number is:",second_largest)