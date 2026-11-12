a = int(input("Enter a number: "))
if a > 18:
    print("You are eligible to vote.")

elif a < 0:
    print("You have entered an invalid number.")

elif a == 18:
    print("You are eligible to vote.")

else:
    print("You are not eligible to vote.")

print("The program has ended.")