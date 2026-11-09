d = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}

new_dict = {}

for key, value in d.items():
    if value not in new_dict.values():
        new_dict[key] = value

print("Original Dictionary:", d)
print("Dictionary after removing duplicates:", new_dict)
