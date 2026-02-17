print("=== Welcome to Itthad Food Advanced Portal ===")

order_item = input("What would you like to order? (Biryani/Burger/Juice): ").lower()
quantity = int(input("How many units? "))

amount={"biryani":280,"burger":350,"juice":150}

match order_item:
    case "biryani" if quantity >= 10:
        total=amount["biryani"]*quantity
        discount=total*0.20
        print(f"Total Amount: ₹{total}")
        print(f"Discount: ₹{discount}")
        print(f"Amount to Pay: ₹{total - discount}")
        print(f"🎉 Bulk Order! You get a 20% discount on {quantity} Biryanis.")
    case "biryani":
        total=amount["biryani"]*quantity
        print(f"✅ Standard Order: {quantity} Biryani(s) confirmed.")
        
    case "burger" | "pizza": 
        total=amount[order_item]*quantity
        print(f"🍔 Fast Food selected: {quantity} {order_item.title()}(s) preparing.")
        
    case "juice" if quantity >=50 :
        print("⚠️ Warning: We don't have that much stock for Juice!")
    
    case "juice":
         total=amount["juice"]*quantity
         print(f"🥤 Refreshing choice: {quantity} Juice(s) coming right up!")
         print(f"Total Amount: ₹{total}")  
        
    case str(item) if item.isdigit(): 
        print("❌ Error: Please enter a name, not a number!")
        
    case _: 
        print(f"Sorry, {order_item} is not on our menu today.")

print("=== Thank you for using our system! ===")