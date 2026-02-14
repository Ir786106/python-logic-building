username=str(input("Enter username: ")).lower()
password=str(input("Enter password: ")).lower()
pin=int(input("Enter PIN: "))

user={"ali", "sara", "mohammad","irfan","saqib"}
passwords={"ali": "ali123", "sara": "sara123", "mohammad": "mohammad123", "irfan": "irfan123", "saqib": "saqib123"}
input_pin={ "ali":1234, "sara":5678, "mohammad":9012, "irfan":3456, "saqib":7890}
is_banned={"ali": False, "sara": False, "mohammad": True, "irfan": False, "saqib": True}
role={"ali": "manager", "sara": "staff", "mohammad": "staff", "irfan": "manager", "saqib": "staff"}
city="arifwala"
if username in user and pin == input_pin.get(username) and password==passwords.get(username):
    if is_banned.get(username, False):
        print("You are banned from accessing the warehouse.")
    else:
        print(f"Welcome {username.title()}! You have {role.get(username.title())} access to the warehouse.")

        user_role = role.get(username)
        order_amount=float(input("Enter the order amount: "))
        city_input=str(input("Enter the city: ")).lower()
        if user_role=="manager":
            if city_input==city:
                taxt=0
                print(f"Your total order amount is: {order_amount:.2f} (no tax applied for orders in {city.title()})")
            else:
                taxt=order_amount*0.05
                order_amount+=taxt
                print(f"Your total order amount is: {order_amount:.2f} (including tax: {taxt:.2f})")
        
        elif user_role=="staff":
            if order_amount>50000:
                print("You are not allowed to process orders above $50,000. Please contact a manager.")
            else:
                taxt=order_amount*0.10
                order_amount+=taxt
                print(f"Your total order amount is: {order_amount:.2f} (including tax: {taxt:.2f})")
else:
    print("Invalid username, password, or PIN. Access denied.")