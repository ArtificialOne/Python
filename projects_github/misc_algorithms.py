import numpy

def square_root(n):
    #Attempt a number, perform division, calculate average of two numbers, then divide
    #For example, Square Root of 95. Divide 95 by 9, equals  10.5. Now add 9, our initial number to 10.5 and divide by 2.
    return(numpy.sqrt(n))

def circle_area():
    pi=numpy.pi

    print(f"To determine the diameter of a circle, please enter the radius: ")
    radius=float(input("> "))
    area=pi*(radius**2)

    print(f"The area is: {area}")

def pythagorean_theorem():
    print("To identify hypotenuse of triangle, provide the length of the two sides:")
    print("Side One: ")
    side1=float(input("> "))
        
    print("Side Two: ")
    side2=float(input("> "))

    hypotenuse=numpy.sqrt((side1**2)+(side2**2))
    print(f"The hypotenuse is: {hypotenuse}")

def tsa_cylinder():
    print("Total surface area of a cylinder is 4πr(h + r)")
    print("Please enter the height: ")
    height=float(input("> "))

    print("Please enter the radius: ")
    radius=float(input("> "))

    tsa=2*numpy.pi*radius*(height+radius)
    print(f"The total surface is area is: {tsa}")
            
def tsa_sphere():
    print("Total surface area of a sphere is 4πr^2")
    print("Please enter the radius: ")
    radius=float(input("> "))

    tsa=4*numpy.pi*(radius**2)
    print(f"The total surface is area is: {tsa}")

def tsa_cone():
    print("Total surface area of a cone is πr(r + l) where you need to know the r and l, l is slant, sqrt(r**2 + h**2)")

def tsa_cube():
    print("Total surface area of a cube is 6s^2 where s is the length of the side")
    print("Please enter the length of a side: ")
    s=float(input("> "))

    tsa=6*(s**2)
    print(f"The total surface area of the cube is: {tsa}")
    
def prime_number_finder():    
    print("Please enter a number to identify if Prime")
    num=int(input("> "))

    if num <= 1:
        print("False")
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("False")
        print("True")

def convert_temperature():
    celcius_to_fahrenheit = lambda celcius: (celcius * 9/5) + 32 
    fahrenheit_to_celcius = lambda fahrenheit: (fahrenheit - 32) * 5/9

    celcius = float(input("Enter Celsius temperature: "))
    fahrenheit = celcius_to_fahrenheit(celcius)
    print(f"{celcius} C is {fahrenheit} F")
    
    fahrenheit = float(input("Enter Fahrenheit temperature: "))
    celcius = fahrenheit_to_celcius(fahrenheit)
    print(f"{fahrenheit} F is {celcius} C")
    print (fahrenheit, "F is",celcius, "C")
    
def distance():
    print("1. Convert Feet to Meters")
    print("2. Convert Miles to Kilometers")
    print("3. Convert Kilometers to miles")
    selection = int(input("> "))
    if selection == 1:
        print("Enter Miles: ")
        miles = float(input("> "))
        kilometers = miles * 1.609344
        print(f"{miles} is {round(kilometers, 2)} Kilometers")
    elif selection == 2:
        print("Enter Kilometers: ")
        kilometers = float(input("> "))
        miles = kilometers / 1.609344
        print(f"{kilometers} is {round(miles, 2)} Miles")
    else:
        print("Please enter a valid selection")

def something():
    pass

def convert_pixels():
    width=int(input("Enter width pixels: "))
    height=int(input("Enter height pixels: "))
    print("Is this grayscale? Y/N: ")
    grayscale=str(input("> ").lower())

    if grayscale in ["y" or "yes"]:
        print(f"The total pixel count is {width*height}")
    elif grayscale in ["n" or "no"]:
        print(f"The total pixel count is {3*width*height}")
    else:
        print("Please enter 'Y' or 'N'")

def convert_bytes():
    print("Please select conversion:\n")
    print("1. Bytes to Bits")
    print("2. Kilobytes to Bytes")
    print("3. Megabytes to Kilobytes")
    print("4. Gigabytes to Megabytes")
    print("5. Terabytes to Gigabytes")
    print("6. Petabytes to Terabytes")
    
    while True:
        try:
            selection=(int(input('> ')))
            if selection==1:
                print("Enter Bytes: ")
                bytes=int(input("> "))
                print(f"{bytes} Bytes is {bytes*8} bits")
                break
            elif selection==2:
                print("Enter Kilobytes: ")
                kilobytes=int(input("> "))
                print(f"{kilobytes} Kilobytes is {kilobytes*1024} Bytes")
                break
            elif selection==3:
                print("Enter Megabytes: ")
                megabytes=int(input("> "))
                print(f"{megabytes} Megabytes is {megabytes*1024} Kilobytes")
                break
            elif selection==4:
                print("Enter Gigabytes: ")
                gigabytes=int(input("> "))
                print(f"{gigabytes} Megabytes is {gigabytes*1024} Kilobytes")
                break
            elif selection==5:
                print("Enter Gigabytes: ")
                terabytes=int(input("> "))
                print(f"{terabytes} Terabytes is {terabytes*1024} Kilobytes")
                break
            elif selection==6:
                print("Enter Petabytes: ")
                petabytes=int(input("> "))
                print(f"{petabytes} Petabytes is {petabytes*1024} Kilobytes")
                break
            else:
                print("Please enter a whole number")
                break
        except ValueError:
            print("\nPlease enter a valid option\n")
            break

def percentage_calculator():
    ##Percentage differential
    ##Quick % of number is multiply % absolute value by number, then move decimal
    ##i.e. 39% of 500 = 39*500 = 19500, move two decimal = 195.00
    ##i.e. 105% of 500 = 105*500 = 52500, move two decimal = 525.00

    while True:
        print("What function are you looking to perform?")
        print("1. Providing a percent and number to identify result.")
        print("2. Percentage increase/decrease.")

        try:
            selection=int(input("> "))
        except ValueError:
            print("Please enter 1 or 2")
            continue
        except KeyboardInterrupt:
            break

        if selection==1:
            print("Please enter the percentage of: ")
            try:
                percent_of=float(input("% "))
            except ValueError:
                print("Please enter a number")
                continue
            except KeyboardInterrupt:
                break

            print("Please enter the number trying to find percentage of: ")
            try:
                number=float(input("> "))
            except ValueError:
                print("Please enter a number")
                continue
            except KeyboardInterrupt:
                break
            
            answer=percent_of*number*.010
            print(f"The percent {percent_of}% of {number} is: {answer}\n")

        if selection==2:
            print("Please enter original value: ")
            try:
                origin_val=float(input("> "))
            except ValueError:
                print("Enter a number")
                break
            except KeyboardInterrupt:
                break

            print("Please enter new value: ")
            try:
                new_val=float(input("> "))
            except ValueError:
                print("Enter a number")
                break
            except KeyboardInterrupt:
                break

            if new_val > origin_val:
                percent_increase = ((new_val - origin_val) / origin_val) * 100
                print(f"Your percentage increase is: {round(percent_increase,2)}%\n")
            elif new_val < origin_val:
                percent_decrease = ((origin_val - new_val) / origin_val)* 100
                print(f"Your percentage decrease is: {round(percent_decrease,2)}%\n")
            elif new_val == origin_val:
                print(f"There was no increase or decrease")
            else:
                print("Invalid")

#print(square_root(200))
#circle_area()
#convert_pixels()
#pythagorean_theorem()
#tsa_cylinder()
#tsa_sphere()
#tsa_cone()
#tsa_cube()
percentage_calculator()
#distance()