customer_name = input("Enter your name: ").lower()
current_city = input("Enter your city name: ").lower()
cart = float(input("Enter your cart total: "))

store_city = "arifwala" 
eligible_cities = {"lahore", "sahiwal", "multan", "faisalabad", "bahawalpur"}
vip_customers = {"ali", "irfan", "rizwan", "saqib"} 
discount_target = 5000

print("\n=== ORDER SUMMARY ===")

has_free_delivery = False 

if current_city == store_city:
    print("🚚 Store City Detected! Free Delivery applied automatically.")
    has_free_delivery = True

elif current_city in eligible_cities and customer_name in vip_customers:
    print(f"🌟 VIP Member '{customer_name.title()}' from {current_city.title()}! Free Delivery applied.")
    has_free_delivery = True

else:
    delivery_fee = 200
    cart += delivery_fee
    print("🚚 Standard Delivery: Rs. 200 charges apply.")


if has_free_delivery == True:
    if cart >= discount_target:
        discount = 0.10 * cart
        cart -= discount
        print(f"🎁 Congratulations! 10% discount applied. Saved: Rs. {discount:.2f}")
    else:
        print(f"💡 Apni cart value Rs. {discount_target} se zyada karein aur 10% discount payein.")

print(f"💰 Your final total is: Rs. {cart:.2f}")