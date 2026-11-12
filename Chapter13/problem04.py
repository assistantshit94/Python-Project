def devisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,3545,65,25,5656,485,789,45,212]

f = list(filter(devisible5, a))
print(f)