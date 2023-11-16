string = "racecar"

reversed_string = ""

for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
