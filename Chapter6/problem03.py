p1 = input("Make a lot of money: ")
p2 = input("buy now:")
p3 = input ("subscribe to our channel:")
p4 = input("click here:")

message = input("Enter your message here: ")
if p1 in message:
    print("This is a spam message")
elif p2 in message:
    print("This is a spam message")
elif p3 in message:
    print("This is a spam message")
elif p4 in message:
    print("This is a spam message")
else:
    print("This is not a spam message")