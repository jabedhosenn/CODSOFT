print("Welcome to Simple Calculator")

while True:

    print("Choose an option (1-4): ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == "2":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == "3":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == "4":
        print(f"{num1} / {num2} = {num1 // num2}")
    else:
        print("Invalid input")

    again = input("Do you want to perform another calculation? (y/n): ")
    if again == "n":
        break

print("Thanks for using this Calculator!")
