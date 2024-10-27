import re

text = "abcdef"

# Using .
print(re.findall("a.", text))  # Output: ['ab']

# Using .*
print(re.findall("a.*", text))  # Output: ['abcdef']
print(re.findall("a.*f", text))  # Output: ['abcdef']