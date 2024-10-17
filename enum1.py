fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

fruits_list=list(enumerate(fruits))
print(fruits_list)

'''fruits_list1=enumerate(fruits)
print(fruits_list1)''' # <enumerate object at 0x104ead490>

