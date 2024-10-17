print(10>1)
#True
print("cat" == "dog")
#False
print (1 != 2)
#True

def hint_username(username):
    surname_lenght=5
    if len(username) < surname_lenght:
        print(f"Invalid username. Must be at least {surname_lenght} characters long")

hint_username("Ali")