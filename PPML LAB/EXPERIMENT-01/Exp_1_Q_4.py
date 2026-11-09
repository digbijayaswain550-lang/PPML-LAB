a = float(input("Enter the number for x^2: "))
b = float(input("Enter the number for x: "))
c = float(input("Enter the constant: "))

D = b * b - (4 * a * c)

print("The discriminant is:", D)

if D > 0:
    root1 = (-b + (D ** 0.5)) / (2 * a)
    root2 = (-b - (D ** 0.5)) / (2 * a)

    print("Two real and different roots.")
    print("Root 1:", root1)
    print("Root 2:", root2)

elif D == 0:
    root1 = -b / (2 * a)

    print("Two real and equal roots.")
    print("Root 1:", root1)
    print("Root 2:", root1)

else:
    real_part = -b / (2 * a)
    imaginary_part = ((-D) ** 0.5) / (2 * a)

    print("Two complex or imaginary roots.")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")
