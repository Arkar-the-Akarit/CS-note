# the cubed values of the first ten integer

cubed_values = [num**3 for num in range(1,11)]

'''
for i in range(1,11):
    cubed_values.append(i**3)
'''


for value in cubed_values:
    print(value)


print('the first three nums are: ',cubed_values[:3])

middleIndex = int(len(cubed_values) /2 )
print('the middle three number: ',cubed_values[middleIndex-1:middleIndex+2])

print('the last three items are: ',cubed_values[-3:])