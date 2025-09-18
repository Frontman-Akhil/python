# Program to print day based on user input( sunday,monday,tuesday,wednesday,thursday,friday,saturday)

# Accept input from user
choice = input("Enter your choice (s, m, t, w, f, so): ").lower()

# Match input to corresponding day
if choice == 's':
    print("Sunday")
elif choice == 'm':
    print("Monday")
elif choice == 't':
    print("Tuesday")
elif choice == 'w':
    print("Wednesday")
elif choice == 'f':
    print("Friday")
elif choice == 'so':
    print("Saturday")
else:
    print("Invalid choice. Please enter one of: s, m, t, w, f, so.")
