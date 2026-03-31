while True:
    print("\n Temperature Calculator ")
    choice = input(
        "1: Enter temperature in Celsius (°C)\n"
        "2: Enter temperature in Fahrenheit (°F)\n"
        "3: Enter temperature in Kelvin (K)\n"
        "4: Exit\n"
        "Enter your choice: ")
    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        fahrenheit = (temp * 9 / 5) + 32
        kelvin = temp + 273.15
        print(f"Celsius: {temp}°C")
        print(f"Fahrenheit: {fahrenheit}°F")
        print(f"Kelvin: {kelvin}K")
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        celsius = (temp - 32) * 5 / 9
        kelvin = celsius + 273.15
        print(f"Fahrenheit: {temp}°F")
        print(f"Celsius: {celsius}°C")
        print(f"Kelvin: {kelvin}K")
    elif choice == "3":
        temp = float(input("Enter temperature in Kelvin: "))
        celsius = temp - 273.15
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Kelvin: {temp}K")
        print(f"Celsius: {celsius}°C")
        print(f"Fahrenheit: {fahrenheit}°F")
    elif choice == "4":
        break
    else:
        print("Invalid choice! Please try again.")