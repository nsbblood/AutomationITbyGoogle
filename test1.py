def odd_numbers(maximum):
    return_string = ""  # Initializes the variable as a string
    
    # Iterate over all odd numbers from 1 to the maximum (inclusive)
    for number in range(1, maximum + 1, 2):  # Step of 2 to get only odd numbers
        return_string += str(number) + " "   # Append each odd number and a space
    
    # Remove the last space at the end of the string
    return return_string.strip()


# Test cases
print(odd_numbers(6))  # Output: "1 3 5"
print(odd_numbers(10)) # Output: "1 3 5 7 9"
print(odd_numbers(1))  # Output: "1"
print(odd_numbers(3))  # Output: "1 3"
print(odd_numbers(0))  # Output: ""
