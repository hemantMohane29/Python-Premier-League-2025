print("\nWelcome to the Geometry Set Calculator")
print("Select a shape or calculation to perform:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
print("5. Parallelogram")
print("6. Trapezium")
print("7. Cube")
print("8. Cuboid")
print("9. Sphere")
print("10. Cylinder")
print("11. Cone")
print("12. Hemisphere")
print("13. Coordinate Geometry")
print("0. Exit")

print("/*/*/*/*/*/*/*/*/*")
while True:
    choice = int(input("\nEnter your choice or 0 to exit: "))
    if choice == 0:
        print("Thank you for using the calculator!")
        break

    elif choice == 1:
        print("You have selected Square.....")
        side = float(input("Enter the side of the square: "))
        area = side * side
        perimeter = 4 * side
        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 2:
        print("You have selected Rectangle.....")
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        perimeter = 2 * (length + width)
        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 3:
        print("You have selected Triangle.....")
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        perimeter = a + b + c
        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 4:
        print("You have selected Circle.....")
        radius = float(input("Enter the radius: "))
        pi = 3.1416
        area = pi * radius * radius
        circumference = 2 * pi * radius
        print("Area =", area)
        print("Circumference =", circumference)

    elif choice == 5:
        print("You have selected Paralleogram.....")
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        side = float(input("Enter the side: "))
        area = base * height
        perimeter = 2 * (base + side)
        print("Area =", area)
        print("Perimeter =", perimeter)

    elif choice == 6:
        print("You have selected Trapezium.....")
        base1 = float(input("Enter base1: "))
        base2 = float(input("Enter base2: "))
        height = float(input("Enter height: "))
        area = 0.5 * (base1 + base2) * height
        print("Area =", area)

    elif choice == 7:
        print("You have selected Cube.....")
        side = float(input("Enter side of cube: "))
        surface_area = 6 * side * side
        volume = side * side * side
        print("Surface Area =", surface_area)
        print("Volume =", volume)

    elif choice == 8:
        print("You have selected Cuboid.....")
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        surface_area = 2 * (length * width + width * height + height * length)
        volume = length * width * height
        print("Surface Area =", surface_area)
        print("Volume =", volume)

    elif choice == 9:
        print("You have selected Sphere.....")
        radius = float(input("Enter the radius: "))
        pi = 3.1416
        surface_area = 4 * pi * radius * radius
        volume = (4 / 3) * pi * radius * radius * radius
        print("Surface Area =", surface_area)
        print("Volume =", volume)

    elif choice == 10:
        print("You have selected cylinder.....")
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        pi = 3.1416
        surface_area = 2 * pi * radius * (radius + height)
        volume = pi * radius * radius * height
        print("Surface Area =", surface_area)
        print("Volume =", volume)

    elif choice == 11:
        print("You have selected Cone.....")
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        slant_height = float(input("Enter the slant height: "))
        pi = 3.1416
        surface_area = pi * radius * (radius + slant_height)
        volume = (1 / 3) * pi * radius * radius * height
        print("Surface Area =", surface_area)
        print("Volume =", volume)

    elif choice == 12:
        print("You have selected Hemisphere.....")
        radius = float(input("Enter the radius: "))
        pi = 3.1416
        surface_area = 3 * pi * radius * radius
        volume = (2 / 3) * pi * radius * radius * radius
        print("Surface Area =", surface_area)
        print("Volume =", volume)

    elif choice == 13:
        print("\nCoordinate Geometry Options:")
        print("1. Midpoint")
        print("2. Slope")
        print("3. Distance")
        print("4. Slope-Intercept Form")
        print("5. Point-Slope Form")
        print("6. Standard Line Form")

        sub_choice = int(input("Choose one option: "))
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if sub_choice == 1:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            print("Midpoint = (", mid_x, ",", mid_y, ")")

        elif sub_choice == 2:
            slope = (y2 - y1) / (x2 - x1)
            print("Slope =", slope)

        elif sub_choice == 3:
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            print("Distance =", distance)

        elif sub_choice == 4:
            m = (y2 - y1) / (x2 - x1)
            c = y1 - m * x1
            print("Slope-Intercept Form: y = " + str(m) + "x + " + str(c))

        elif sub_choice == 5:
            m = (y2 - y1) / (x2 - x1)
            print("Point-Slope Form: y -", y1, "= " + str(m) + "(x -", x1, ")")

        elif sub_choice == 6:
            A = y2 - y1
            B = x1 - x2
            C = A * x1 + B * y1
            print("Standard Line Form: " + str(A) + "x + " + str(B) + "y = " + str(C))

        else:
            print("Invalid sub-option!")

    else:
        print("Invalid main option! Please try again.")