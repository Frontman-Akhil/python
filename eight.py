#write a program to accept characters from user and print characters are in capital or small letters
# Accept a character from the user
char = input("Enter a character: ")

# Check if the input is a single alphabet character
if len(char) == 1 and char.isalpha():
    if char.isupper():
        print(f"The character '{char}' is a CAPITAL letter.")
    else:
        print(f"The character '{char}' is a small letter.")
else:
    print("Please enter a single alphabet character.")
