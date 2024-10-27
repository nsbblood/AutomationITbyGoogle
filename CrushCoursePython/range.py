#frange function will enable us to be able to use float steps in our code ( for negative..)
def fneg_range(start, stop, step):
    x = start
    while x > stop: 
        yield x
        x += step

#frange function will enable us to be able to use float steps in our code ( for negative..)
def fpos_range(start, stop, step):
    x = start
    while x < stop: 
        yield x
        x += step

for x in fneg_range(1, -1, -0.1):
    print(x)

for x in fpos_range(1, 2, 0.1):
    print(x)


#If you wont use floats then simply use:
for z in range(0,5,1):
    print(z)