import re

text = "The quick brown fox jumps over the lazy dog"
pattern = r"brown.*dog"

if re.search(pattern, text):
    print("Match found!")

import re

text = "apple,banana;cherry:date"
pattern = r"[,;:]" #when you delete the comma or other expressions the output will change

fruits = re.split(pattern, text)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

