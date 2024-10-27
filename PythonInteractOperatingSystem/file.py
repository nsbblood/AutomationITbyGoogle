with open('python_tutorial.txt','r') as file:
    content=file.read()
   # print(content[0:10000])
#it opens the file and write until the character that I have wrote...

sorted_content=sorted(content)
#print(sorted_content[0:10000])  #-> it is crazy!!

new_content=content.split("/n")
print(new_content[0:100])

