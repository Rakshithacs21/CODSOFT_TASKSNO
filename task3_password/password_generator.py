import random
import string

while True:
    print("\n===================================")
    print("      PASSWORD GENERATOR")
    print("===================================")
    print("1. Weak Password")
    print("2. Medium Password")
    print("3. Strong Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank you for using the Password Generator!")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please try again.")
        continue

    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
        continue

    if choice == "1":
        characters = string.ascii_letters
        strength = "Weak"

    elif choice == "2":
        characters = string.ascii_letters + string.digits
        strength = "Medium"

    elif choice == "3":
        characters = string.ascii_letters + string.digits + string.punctuation
        strength = "Strong"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nPassword Strength:", strength)
    print("Generated Password:", password)

    again = input("\nDo you want to generate another password? (Y/N): ")

    if again.lower() != "y":
        print("Thank you for using the Password Generator!")
        break
    