light=str(input("Enter traffic light color (red, yellow, green): ")).strip().lower()

match light:
    case "red":
        print("🚦 Red Light: Stop! 🛑")
    case "yellow":
        print("🚦 Yellow Light: Prepare to stop! ⚠️")
    case "green":
        print("🚦 Green Light: Go! ✅")
    case _:
        print("Invalid traffic light color entered. Please use red, yellow, or green.")