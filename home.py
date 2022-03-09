import math
import os
import time


def clr():
    os.system('cls')


def main():
    clr()
    print("""
    Welcome to the ultimate calulator! 🧮
    Select a category to get started!

    1) The Basic Calulator!
    2) Unit Converters!
    3) Geometry!
    4) Extra! NOT DONE YET!
    """)
    cat = input(
        "Please enter an option from 1-3 in numeric form. For example, '5', '8': ")
    if cat == "1":
        calc()
    elif cat == "2":
        conv()
    elif cat == "3":
        geometry()
    elif cat == "4":
        pass


def calc():
    clr()
    operation = (input("""Please enter a valid number input for an operation:
    1) Addition
    2) Subtraction
    3) Multiplication
    4) Division
    5) Exponents (First enter base, then exponent in next step)
    6) Return Remainder

    Enter "back" to go back to the main menu.
    Input: """))
    a = float(input("Please enter the first number for the calculation: "))
    b = float(input("Please enter the second number for the calculation: "))

    if operation == "1":
        print(a, "+", b, "=", a+b)

    elif operation == "2":
        print(a, "-", b, "=", a-b)

    elif operation == "3":
        print(a, "*", b, "=", a*b)

    elif operation == "4":
        print(a, "/", b, "=", a/b)

    elif operation == "5":
        print(a, "raised to the power of", b, "=", pow(a, b))

    elif operation == "6":
        print("The remainder when", a, "is divided by", b, "is", a % b)

    elif operation == "back":
        main()

    else:
        print("Invalid input")

    quit(calc)


def conv():
    clr()
    choice = input("""
    1) Convert miles to kilometres
    2) Convert kilometres to miles
    3) Convert pounds to kilograms
    4) Convert kilograms to pounds
    Please enter a number from 1-4, to go back, enter 'back': """)
    if choice == "1":
        con1()
    if choice == "2":
        con2()
    if choice == "3":
        con3()
    if choice == "4":
        con4()

    quit(conv)


def con1():
    a = float(input("Please enter the number for the conversion: "))
    ans = round(a*1.6, 2)
    print(f"{a} converted to kilometers is {ans}km.")


def con2():
    a = float(input("Please enter the number for the conversion: "))
    ans = round(a/1.6, 2)
    print(f"{a} converted to miles is {ans}miles.")


def con3():
    a = float(input("Please enter the number for the conversion: "))
    ans = round(a/2.2, 2)
    print(f"{a} converted to kilograms is {ans}kg.")


def con4():
    a = float(input("Please enter the number for the conversion: "))
    ans = round(a*2.2, 2)
    print(f"{a} converted to is {ans}lb.")


# geometry codes


def geometry():
    clr()
    option = input("""
    1) Circles
    2) Triangles
    3) Quadrilaterals NOT DONE YET
    4) Solid Shape NOT DONE YET

    Please enter a number from 1-4, to go back, enter 'back': """)
    clr()
    if option == "1":
        option2 = input("""
        1) Find area when circumference given.
        2) Find circumference when area given.
        3) Find Radius and diameter from Circumference.
        4) Find Radius and diameter from Area.

        Please enter a number from 1-4, to go back, enter 'back': """)

    elif option == "2":
        option2 = input("""
        1) Find area when height and base given.
        2) Find hypotenuse when height and base given 
        3) Find the other side when area and one perpendicular side given. NOT DONE YET
        4) Find 1 angle when 2 angles given. NOT DONE YET

        Please enter a number from 1-4, to go back, enter 'back': """)

    elif option == "3":
        option2 = input("""
        1) Find area when circumference given.
        2) Find circumference when area given.
        3) Find Radius and diameter from Circumference.
        4) Find Radius and diameter from Area.

        Please enter a number from 1-4, to go back, enter 'back': """)

    if option == "4":
        option2 = input("""
        1) Find area when circumference given.
        2) Find circumference when area given.
        3) Find Radius and diameter from Circumference.
        4) Find Radius and diameter from Area.

        Please enter a number from 1-4, to go back, enter 'back': """)

    if option == "1" and option2 == "1":
        geo1()
    elif option == "1" and option2 == "2":
        geo2()
    elif option == "1" and option2 == "3":
        geo3()
    elif option == "1" and option2 == "4":
        geo4()
    elif option == "2" and option2 == "1":
        geo5()
    elif option == "2" and option2 == "2":
        geo5()
    elif option == "back":
        geometry()

    quit(geometry)


def geo1():
    a = float(input("Please enter the circumference: "))
    ans = round(math.pi*pow((a/(2*math.pi)), 2), 2)
    print("The area of a circle with circumference", a, "is", ans)


def geo2():
    a = float(input("Please enter the area: "))
    ans = round((2*math.pi)*math.sqrt(a/math.pi))
    print("The circumference of a circle with area", a, "is", ans)


def geo3():
    a = float(input("Please enter the circumference: "))
    ans = round(a/(2*math.pi), 2)
    print("The radius is:", ans)
    ans = round(ans*2, 2)
    print("The diameter is:", ans)


def geo4():
    a = float(input("Please enter the area: "))
    ans = round(math.sqrt(a/math.pi), 2)
    print("The radius is:", ans)
    ans = round(ans*2, 2)
    print("The diameter is:", ans)


def geo5():
    a = float(input("Please enter the height: "))
    b = float(input("Please enter the base: "))
    ans = (a*b)/2
    print("The area of a triangle with height", a, "and base", b, "is", ans)


def geo6():
    a = float(input("Please enter the height: "))
    b = float(input("Please enter the base: "))
    ans = math.sqrt((a*a)+(b*b))
    print("The hypotenuse of a triangle is", ans)


def geo7():
    pass


def geo8():
    pass


def geo9():
    pass


def geo10():
    pass


def quit(function):
    # will be called after fun() finishes.
    time.sleep(2)
    quit = input(
        "Enter 'back' to go back to the previous menu, enter 'main' to return to the main menu. Enter 'exit' to quit.")
    if quit == "back":
        function()
    elif quit == "main":
        main()
    elif quit == "exit":
        exit()


main()
