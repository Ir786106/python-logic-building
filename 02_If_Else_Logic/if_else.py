age=int(input("Enter your age: "))
if age>=18:
    if age<=70:
        print("You are eligible for driving license.")
    else:
        print("You are not eligible for driving license because you are too old.")
else:    
    print("You are not eligible for driving license.") 