import random


def main():
    # variables
    password_length = None
    special_characters = None
    numbers = None
    uppercase = None
    character_pool = "abcdefghijklmnopqrstuvwxyz"

    # Current mode
    # 0 = password length
    # 1 = special characters
    # 2 = numbers
    # 3 = uppercase
    mode = 0

    # Welcome message
    print("Password Generator")
    print("Created by: IngPleb")
    print("---------------------")
    while True:
        try:
            if mode == 0:
                password_length = int(input("Enter password length: "))
                if password_length < 1:
                    print("Password length must be greater than 0")
                    continue
                mode = 1
            elif mode == 1:
                special_characters = input("Use special characters? (y/n): ")
                if special_characters == "y":
                    special_characters = True
                elif special_characters == "n":
                    special_characters = False
                else:
                    print("Invalid input")
                    continue
                mode = 2
            elif mode == 2:
                numbers = input("Use numbers? (y/n): ")
                if numbers == "y":
                    numbers = True
                elif numbers == "n":
                    numbers = False
                else:
                    print("Invalid input")
                    continue
                mode = 3
            elif mode == 3:
                uppercase = input("Use uppercase? (y/n): ")
                if uppercase == "y":
                    uppercase = True
                elif uppercase == "n":
                    uppercase = False
                else:
                    print("Invalid input")
                    continue
                break
        except ValueError:
            print("Invalid input")

    # Generate character pool
    if special_characters:
        character_pool += "!@#$%^&*()_+"
    if numbers:
        character_pool += "1234567890"
    if uppercase:
        character_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Generate password
    password = ""

    for i in range(password_length):
        password += random.choice(character_pool)

    print("Your password is: " + password)


if __name__ == '__main__':
    main()
