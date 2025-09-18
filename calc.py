print("Arithmetic Operations")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid choice")
