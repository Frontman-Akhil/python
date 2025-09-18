#write a program to design a app for movie ticket booking.
#first accept choice of seat (classic rs100/ premium Rs300/ recliner rs500)
#accept number of seats
#now according to seats provide offer
# Amount between 500 to 1500 offer includes(choice of meal worth Rs200 or 20% discount)
# Amount more than 1500 offer include(choice of meal worth Rs500 or 40% discount)
# Movie Ticket Booking App

# Seat types and their prices
seat_prices = {
    "classic": 100,
    "premium": 300,
    "recliner": 500
}

# Display seat options
print("Welcome to Movie Ticket Booking 🎬")
print("Available seat types:")
print("1. Classic - Rs100")
print("2. Premium - Rs300")
print("3. Recliner - Rs500")

# Accept seat choice
seat_choice = input("Enter your seat type (classic/premium/recliner): ").lower()

# Validate seat choice
if seat_choice not in seat_prices:
    print("Invalid seat type selected.")
else:
    # Accept number of seats
    try:
        num_seats = int(input("Enter number of seats: "))
        if num_seats <= 0:
            print("Number of seats must be greater than zero.")
        else:
            # Calculate total amount
            total_amount = seat_prices[seat_choice] * num_seats
            print(f"\nTotal amount: Rs{total_amount}")

            # Provide offers based on amount
            if 500 <= total_amount <= 1500:
                print(" Offer Available:")
                print("1. Free meal worth Rs200")
                print("2. 20% discount")
                offer = input("Choose your offer (meal/discount): ").lower()
                if offer == "meal":
                    print("You selected: Free meal worth Rs200")
                elif offer == "discount":
                    discount = total_amount * 0.20
                    final_amount = total_amount - discount
                    print(f" You selected: 20% discount. Final amount: Rs{final_amount}")
                else:
                    print("Invalid offer choice.")
            elif total_amount > 1500:
                print("🎁 Premium Offer Available:")
                print("1. Free meal worth Rs500")
                print("2. 40% discount")
                offer = input("Choose your offer (meal/discount): ").lower()
                if offer == "meal":
                    print("You selected: Free meal worth Rs500")
                elif offer == "discount":
                    discount = total_amount * 0.40
                    final_amount = total_amount - discount
                    print(f" You selected: 40% discount. Final amount: Rs{final_amount}")
                else:
                    print("Invalid offer choice.")
            else:
                print("No offers available for this amount.")
    except ValueError:
        print("Please enter a valid number of seats.")
