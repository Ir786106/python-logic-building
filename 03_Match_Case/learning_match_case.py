print("--- Warehouse Management System ---")
print("1. Stock | 2. Delivery | 3. Accounts")

option = input("Select an option: ").lower()

match option:
    case "1" | "stock":
        print("📦 Checking Warehouse Stock... All items are in place.")
    case "2" | "delivery":
        print("🚚 Checking Delivery Status... 5 trucks are on the way.")
    case "3" | "accounts":
        print("💰 Accessing Financial Records... Audit in progress.")
    case _:
        print("❌ Invalid Option Selected! Please try again.")