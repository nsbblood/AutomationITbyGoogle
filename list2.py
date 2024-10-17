fruits_list=""
with open('list2.txt','r') as file:
    contents=file.read()
    fruits_list=contents

'''new_list=fruits_list.split()
print(new_list)'''

new_list=fruits_list.split()
new_list.append("Favorite")
print(new_list)

print(new_list[0])
new_list.pop(3) #index 4 removed
new_list.remove('Favorite')
new_list[2]="Cool?"
print(new_list)
