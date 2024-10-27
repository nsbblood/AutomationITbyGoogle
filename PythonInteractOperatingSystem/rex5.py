import re

text = "The date is 2024-10-18."
date = re.search(r"\d{4}-\d{2}-\d{2}", text)
if date:
    print("Date found:", date.group())
else:
    print("No date found.")

'''
\d{4}: Matches four digits representing the year.
-: Matches a literal hyphen.
\d{2}: Matches two digits representing the month.
-: Matches a literal hyphen.
\d{2}: Matches two digits representing the day.
'''

text = "The date is 2024-08-18."
date = re.search(r"\d(4)-\d(2)-\d(2)", text)  # you cant just use paranthesis ?
if date:
    print("Date found:", date.group())
else:
    print("No date found.")