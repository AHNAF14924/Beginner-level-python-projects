number = int(input("Enter a number: "))


if number % 2 == 0 and number % 3 == 0:
    print("The number is divisible by both 2 and 3.")
elif number % 2 == 0:
    print("The number is divisible by 2.")
elif number % 3 == 0:
    print("The number is divisible by 3.")

else:
    print("The number is not divisible by 2 or 3.")
