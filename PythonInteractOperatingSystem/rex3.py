import re

def check_emails(email):

    if re.match(r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]{2,}$", email):
        print("Valid email address")
    else:
        print("Invalid email address")

check_emails("hi@enesarikan.me")
check_emails("hi@enes0.me")
check_emails("hi@hiiii4444.me")
check_emails("hi@şöçüü.me")
check_emails("hi@coolmail.me")
check_emails("_@coolmail_.me")