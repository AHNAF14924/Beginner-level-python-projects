while True:
    number = input("Enter a number: ")
    try:
        number = int(number)
        break
    except ValueError:
        print("That is not a valid number. Please try again.")

print(f"You entered the number {number}")
