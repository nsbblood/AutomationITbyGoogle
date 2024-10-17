def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]    
    return area_code + " " + exchange + "-" + line

print(format_phone("2025551212"))


def greeting_friends(friends):
    for friend in friends:
        print("Hi dear " +friend)

greeting_friends("Byran")
greeting_friends(["Byran"]) #This is a list
greeting_friends(["Byran","Elii","Ns"])