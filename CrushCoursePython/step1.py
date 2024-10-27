'''number_list = []
for number in range(1000):
    number += number  # This doubles the number from the range
    number_list.append(number * number)  # Square the number and append to the list

print(number_list)'''
number_list = []
with open("step1.txt", "w") as file:  # Open the file in write mode
    for number in range(1000):
        number += number  # Double the number
        result = number * number  # Square the number
        number_list.append(result)
        file.write(f"{result}\n")  # Write the result to the file with a newline

print("Results have been saved to step1.txt.")
print(number_list)
