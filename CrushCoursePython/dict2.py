def letter_counter(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter]=0
        result[letter] +=1
    return result

print(letter_counter("aaaaanbedfdsdf"))
print(letter_counter("Here it is Eminem "))


