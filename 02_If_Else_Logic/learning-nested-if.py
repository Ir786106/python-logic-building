# username=str(input("Enter username: "))
print("Welcome to the bank!")
print("                                                              ")
print("Please swipe your card for transaction.")
print("                                                              ")
password=int(input("Enter pin: "))
# user="admin"
p_word=123
if password==p_word:
    print("Swipe successful.")
    print("                                                              ")
    amount=float(input("Enter your purchase amount: "))
    print("                                                              ")
    salary=100000
    if salary > amount:
        print("Amount successfully transferred for new car.")
    else:
        print("Low balance. Amount transfer failed.")
else:
    print("Invalid pin, Please try again.")