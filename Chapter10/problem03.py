class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attrubutr because instance attribute is not present
o.a = 0 #Instance attribute set
print(o.a) #Prints the Instance attributr bcz instance attribute is prensent
print(Demo.a) #Prints the class attribute
