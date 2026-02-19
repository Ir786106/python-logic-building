order_id=int(input("Enter order ID: "))
match order_id:
    case id if 1000 <= id < 2000:
        print(f"Order ID {order_id} is in Processing status. 🛒")
    case id if 2000 <= id < 3000:
        print(f"Order ID {order_id} is Shipped. 🚚")
    case id if 3000 <= id < 4000:
        print(f"Order ID {order_id} is Delivered. 📦")
    case id if 4000 <= id < 5000:
        print(f"Order ID {order_id} is Cancelled. ❌")
    case _:
        print("Invalid Order ID entered. Please enter a valid ID between 1000 and 4999.")