
# Menu-Driven Calculator and Unit Converter

CONVERSIONS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


def get_number(message):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


def calculator():
    print("\n--- Basic Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Choose an operation (1-4): ")

    if choice not in ("1", "2", "3", "4"):
        print("Invalid operation!")
        return

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            return
        result = num1 / num2

    print("Result:", result)


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")

    choice = input("Choose a conversion (1-3): ")

    if choice not in ("1", "2", "3"):
        print("Invalid conversion!")
        return

    value = get_number("Enter the value to convert: ")

    if choice == "1":
        result = value * CONVERSIONS["km_to_miles"]
        print(f"{value} km = {result:.2f} miles")

    elif choice == "2":
        result = (value * 9 / 5) + 32
        print(f"{value}°C = {result:.2f}°F")

    elif choice == "3":
        result = value * CONVERSIONS["kg_to_pounds"]
        print(f"{value} kg = {result:.2f} pounds")


def main():
    while True:
        print("\n===== CALCULATOR & UNIT CONVERTER =====")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
