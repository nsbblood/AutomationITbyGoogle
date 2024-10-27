def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b #!!!! 

sub_result, add_result, mul_result, div_result = calculate_numbers(10, 2) #!!! 
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8

#This will give you wrong results!!
#Your function's return values are important.