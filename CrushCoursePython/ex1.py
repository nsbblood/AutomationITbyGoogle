import random
import time
import sys

print(f" Starting time: {time.time()}")

my_string="aabbkkaw"
my_new_string=my_string.upper()
print(my_new_string)

my_string="here we are"
here_new_string=my_string.split(" ")
print(here_new_string)

fruits = ['apple', 'banana', 'grape']
for i, fruit in enumerate(fruits):
    print(f"Fruit {i}: {fruit}")

x = [1, 2, 3, 4, 5]
for i in reversed(x):
    print(i)

x = [1, 2, 2, 3, 4, 4, 5]
print(set(x)) #convert a value to set

y=5
y_new=str(y)
print(y_new)
print(type(y_new))

x = [1, 2, 3, 4, 5]
print(sum(x))  

x = (1, 2, 3, 4, 5,7,8,9,10)
print(sum(x))  

m = {1, 2, 3, 4}
print(m)
print(sum(m))  
m_new=tuple(m)
print(m_new)
print(type(m_new))


x = [1, 2, 3]
y = ['a', 'b', 'c']
for i, j in zip(x, y):
    print(f"{i}: {j}")

x=random.randint(1,20)
print(x)

print(f" End time: {time.time()}")

print(f"Sys version: {sys.version}")