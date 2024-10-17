def is_power_of(number, base):
 # Base case: when number is smaller than base.
    if number < base:
        if number==1:
            return True
        return False

    # Recursive case: keep dividing number by base.
    return is_power_of(number-1, base)


print(is_power_of(8,2))     # Should be True
print(is_power_of(64,4))    # Should be True
print(is_power_of(70,10))   # Should be False

'''for sum in range(5):
    sum += sum
    print(sum)

num1 = 0
num2 = 0'''

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)