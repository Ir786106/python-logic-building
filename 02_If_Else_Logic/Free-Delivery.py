username=str(input("Enter username: "))
password=str(input("Enter password: "))

if username=="admin" and password=="admin123":
    print("Welcome to Free Delivery!")
    print("---------------------------------------------------------------")
    amount=float(input("Enter your purchase amount: "))
    print("---------------------------------------------------------------")
    if amount>1000:
        print("Congratulations! You are eligible for free delivery.")
    else:
        print("Sorry, you need to spend more than $1000 to qualify for free delivery.")
else:
    print("Invalid username or password. Please try again.")
