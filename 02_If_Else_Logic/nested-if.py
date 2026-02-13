username=str(input("Enter your username: "))
password=str(input("Enter your password: "))

admin_username="admin"
admin_password="admin123"

customer_username="customer"
customer_password="customer123"


if (username==admin_username and admin_password==password) or (username==customer_username and password==customer_password):
    print("Welcome for login successfully.")
    if username==admin_username:
        print("Welcome, admin! You have full access to the system.")
    else:
        print("Welcome, customer! You have limited access to the system.")
else:
    print("username or password is incorrect. Please try again.")