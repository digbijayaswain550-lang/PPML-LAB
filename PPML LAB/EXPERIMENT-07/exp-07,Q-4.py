sequence = "Programming"

uppercase = list(map(str.upper, sequence))

lowercase = list(map(str.lower, sequence))

unique_letters = list(dict.fromkeys(map(str.lower, sequence)))

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Without duplicates:", unique_letters)
