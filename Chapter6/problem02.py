a1 = int(input("Enter your marks a1: "))
a2 = int(input("Enter your marks a2: "))
a3 = int(input("Enter your marks a3: "))
total_percentage = (100 * (a1 + a2 + a3)) / 300
if total_percentage >= 90:
    print("Grade A")
else:
    if total_percentage >= 80:
        print("Grade B")
    else:
        if total_percentage >= 70:
            print("Grade C")
        else:
            if total_percentage >= 60:
                print("Grade D")
            else:
                print("Grade F")