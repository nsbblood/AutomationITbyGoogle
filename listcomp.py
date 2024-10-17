multiples = []
for x in range(1,11):
  multiples.append(x*7)

print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

lengths.append(len("Html")) #you can add it's lenght later like this...
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)