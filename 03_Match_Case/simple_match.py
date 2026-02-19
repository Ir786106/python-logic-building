day = input("Enter day name: ").strip().capitalize()

match day:
    case "Saturday" | "Sunday":
        print(f"✨ {day} is a Weekend! Relax time. 😎")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"💼 {day} is a Working Day. Keep grinding! 🔥")
    case _:
        print("❌ Invalid day name entered.")