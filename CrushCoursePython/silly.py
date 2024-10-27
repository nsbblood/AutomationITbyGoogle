'''def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))'''
def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n-1, sum+n)

c = 998
print(recursive_function(c, 0))