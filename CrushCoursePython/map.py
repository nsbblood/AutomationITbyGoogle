def multiply_numbers(number):
    return number*44

number=[1,2,3,4,5]

result= map(multiply_numbers,number)
print(list(result)) # you need to convert map to list!