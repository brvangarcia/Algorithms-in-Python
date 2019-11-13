numbers = [1,2,300,40.5,5,6]

#print(numbers[0])

#numbers[1] = 'Adam'

#print(numbers[1])

# for num in numbers:
#     print(num)

# for i in range(len(numbers)):
#     print(numbers[i])

# print(numbers[:-2])

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    
print(maximum)
