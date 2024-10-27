import os
import datetime

#os.remove("text2.txt")
#os.mkdir("exampletext.txt")

new_file="exampletext.txt"

if not os.path.exists(new_file):
    with open(new_file,"w") as file:
        file.write("Generated it successfully")
    print("It is created successfully")

else:
    print("It is already exists")


with open("MyNewText.txt",  "w") as file:
    pass

#os.remove("exampletext.txt")

#if os.path.exists("text1.txt")==True:
   # print("Yes it is existed")

size=os.path.getsize("python_tutorial.txt")
print("Python tutorial file size is {} byte(s)".format(size))


# Get the absolute path of the file "spider.txt"
absolute_path = os.path.abspath("text1.txt")

print(absolute_path)

document_directory="/Users/enesarikan/Desktop/automation/Coursera/AutomationITbyGoogle/PythonInteractOperatingSystem/"
file_path=os.path.join(document_directory,"spider.txt")
absolute_path=os.path.abspath(file_path)
print(absolute_path)

timestamp=os.path.getmtime("text1.txt")
print(datetime.datetime.fromtimestamp(timestamp)) #fromtimestamp

print(os.getcwd())

dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
 os.mkdir(dest_dir)