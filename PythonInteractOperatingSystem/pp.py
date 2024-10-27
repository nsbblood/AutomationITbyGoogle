# Append to an existing file
'''with open('example.txt', 'a') as file:
    file.write("\nThis line is appended.")'''

with open('example.txt', 'w') as file:
    file.write("\nThis line is appended.")

# append does not change the whole txt doc like "w"

import os

# Check if a file exists
if os.path.exists('example.txt'):
    print("The file exists.")
else:
    print("The file does not exist.")

# Get the current working directory
print(os.getcwd())

# List files in a directory
print(os.listdir('.'))


import re

# Find all occurrences of 'cat' in a string
text = "The cat sat on the mat with another cat."
matches = re.findall(r'cat', text)
print(matches)  # Output: ['cat', 'cat']



def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

print(validate_email("user@example.com"))  # Valid Email
print(validate_email("user@.com"))  # Invalid Email


text = "Call me at 415-555-1234 or 415-555-4321"
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
phones = re.findall(phone_pattern, text)
print(phones)  # Output: ['415-555-1234', '415-555-4321']

import os

# Move or rename file
os.rename('example.txt', 'newtextname.txt')


log = "User alice logged in at 2023-10-25 08:15"
match = re.search(r'User (\w+) logged in at (\d{4}-\d{2}-\d{2})', log)
if match:
    print(f"User: {match.group(1)}, Date: {match.group(2)}")