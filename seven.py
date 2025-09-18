# Program to print a message based on user input
#print hi, welcome, bye

# Accept input from user
choice = input("Enter your choice (hi, welcome, bye): ").lower()

# Match input to corresponding message
if choice == "hi":
    print("Hi there!")
elif choice == "welcome":
    print("Welcome! Glad you're here.")
elif choice == "bye":
    print("Goodbye! Have a great day.")
else:
    print("Invalid choice. Please enter 'hi', 'welcome', or 'bye'.")
