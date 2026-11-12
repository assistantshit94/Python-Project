from functools import reduce

l = [111,565,652,221,1545,121]

def greater(a,b):
    if (a > b):
        return a
    return b

print (reduce(greater, l))