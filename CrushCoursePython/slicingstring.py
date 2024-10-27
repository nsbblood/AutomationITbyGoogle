string1 = "Greetings, Earthlings"
print(string1[0])   
print(string1[4:8]) 
print(string1[11:]) 
print(string1[:5])  
print(string1[0:10:2])  #0,2,4..10indexes. It is not tuple so I cant use ","

print(string1[-10:]) #python ounts back from the end of the string

print(string1[55:])

print(string1[0::2])  # Prints “Getns atlns” 
print(string1[::-1])  # Prints “sgnilhtraE ,sgniteerG”
print(string1[::-2])  # Prints “sgnilhtraE ,sgniteerG”
print(string1[::1])  # Prints “sgnilhtraE ,sgniteerG”