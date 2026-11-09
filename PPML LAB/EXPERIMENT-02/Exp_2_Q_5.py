Q = input("Enter a string: ")

print("Reverse:", Q[::-1])

vowels = 0
consonants = 0

for ch in Q:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
