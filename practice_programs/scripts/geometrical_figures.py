###############################################################################
# File          : geometrical_figures.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 30 May, 2020
# Updated       : 30 May, 2020
# Description   : A platform independent script to display statistics about a geometrical figure.
################################################################################

# Defining colors for linux terminal
RED="\033[0;31m"
GR="\033[0;32m"
OR="\033[0;33m"
NC="\033[0m"

# import modules
import os
import platform
import sys
import math

# Defining functions

def clearscreen():
    OS=platform.system()
    if OS=="Linux":
        os.system("clear")
    else:
        os.system("cls")
    return None

def user_input():
    print("Below is the list of different geometrical figures:")
    list_of_figures=["Semicircle","Circle","Triangle","Square","Rectangle","Hemisphere","Sphere","Cube","Cuboid","Cone","Cylinder"]
    for i in list_of_figures:
        index_value=list_of_figures.index(i)
        print(f"{index_value+1}.{i}")
    print()
    #try and except block to catch invalid user input
    try:
        user_input_number=int(input("Please enter your choice [1|2|3|..|10|11] : "))
    except ValueError:
        print(f"{RED}Invalid input.{NC} Please enter a number only [1|2|3|..|10|11]. Exiting script!")
        sys.exit(1)
    if user_input_number in list(range(1,12)):
        index_value=user_input_number-1
        return(list_of_figures[index_value])
    else:
        print(f"Please enter a number from {RED}1 to 11{NC} only. No other number is acceptable. Exiting script!")
        sys.exit(1)
    return None

def semicircle():
    print(f"\nYou have selected Semicircle.")
    radius=eval(input("Enter the radius of semicircle : "))
    print(f"\nProperties of semicircle are as follows:")
    print(f"Diameter : {radius*2}")
    print(f"Area : {math.pi*math.pow(radius,2)/2}")
    print(f"Circumference : {math.pi*radius}")
    return None

def circle():
    print(f"\nYou have selected Circle.")
    radius=eval(input("Enter the radius of circle : "))
    print(f"\nProperties of circle are as follows:")
    print(f"Diameter : {radius*2}")
    print(f"Area : {math.pi*math.pow(radius,2)}")
    print(f"Circumference : {2*math.pi*radius}")
    return None

def triangle():
    print(f"\nYou have selected Triangle.")
    ans=input("Is the triange equilateral? [yes|no] : ")
    if ans=="yes":
        side=eval(input("Enter the length of side of triangle : "))
        print(f"\nProperties of equilateral triangle are as follows:")
        print(f"Perimeter : {3*side}")
        print(f"Semi-perimeter : {3*side/2}")
        print(f"Area : {math.sqrt(3)*math.pow(side,2)/4}")
    elif ans=="no":
        side1=eval(input("Enter the length of first side of triangle : "))
        side2=eval(input("Enter the length of second side of triangle : "))
        side3=eval(input("Enter the length of third side of triangle : "))
        print(f"\nProperties of triangle are as follows:")
        print(f"Perimeter : {side1+side2+side3}")
        print(f"Semi-perimeter : {(side1+side2+side3)/2}")
        perimeter=side1+side2+side3
        sp=perimeter/2
        print(f"Area : {math.sqrt(sp*(sp-side1)*(sp-side2)*(sp-side3))}")
    else:
        print(f"{RED}Invalid input.{NC} Please enter input as [yes|no]. Exiting script!")
        sys.exit(1)
    return None

def square():
    print(f"\nYou have selected Square.")
    side=eval(input("Enter the length of side of square : "))
    print(f"\nProperties of square are as follows:")
    print(f"Diagnol : {math.sqrt(2*math.pow(side,2))}")
    print(f"Perimeter : {4*side}")
    print(f"Semiperimeter : {4*side/2}")
    print(f"Area : {math.pow(side,2)}")
    return None
    
def rectangle():
    print(f"\nYou have selected Rectangle.")
    length=eval(input("Enter the length of rectangle : "))
    breadth=eval(input("Enter the breadth of rectangle : "))
    print(f"\nProperties of rectangle are as follows:")
    print(f"Diagnol : {math.sqrt(math.pow(length,2)+math.pow(breadth,2))}")
    print(f"Perimeter : {2*(length+breadth)}")
    print(f"Semiperimeter : {length+breadth}")
    print(f"Area : {length*breadth}")
    return None

def hemisphere():
    print(f"\nYou have selected Hemisphere.")
    radius=eval(input("Enter the radius of hemisphere : "))
    print(f"\nProperties of hemisphere are as follows:")
    print(f"Diameter : {radius*2}")
    print(f"Curved Surface Area : {2*math.pi*math.pow(radius,2)}")
    print(f"Total Surface Area : {3*math.pi*math.pow(radius,2)}")
    print(f"Volume : {(2*math.pi*math.pow(radius,3))/3}") 
    return None

def sphere():
    print(f"\nYou have selected Sphere.")
    radius=eval(input("Enter the radius of sphere : "))
    print(f"\nProperties of sphere are as follows:")
    print(f"Diameter : {radius*2}")
    print(f"Surface Area : {4*math.pi*math.pow(radius,2)}")
    print(f"Volume : {(4*math.pi*math.pow(radius,3))/3}") 
    return None

def cube():
    print(f"\nYou have selected Cube.")
    side=eval(input("Enter the length of side of cube : "))
    print(f"\nProperties of cube are as follows:")
    print(f"Diagnol : {math.sqrt(3)*side}")
    print(f"Surface Area : {6*math.pow(side,2)}")
    print(f"Volume : {math.pow(side,3)}")
    return None

def cuboid():
    print(f"\nYou have selected Cuboid.")
    length=eval(input("Enter the length of cuboid : "))
    breadth=eval(input("Enter the breadth of cuboid : "))
    height=eval(input("Enter the height of cuboid : "))
    print(f"\nProperties of cuboid are as follows:")
    print(f"Diagnol : {math.sqrt(math.pow(length,2)+math.pow(breadth,2)+math.pow(height,2))}")
    print(f"Surface Area : {2*((length*breadth)+(length*height)+(breadth*height))}")
    print(f"Volume : {length*breadth*height}")
    return None

def cone():
    print(f"\nYou have selected cone.")
    radius=eval(input("Enter the radius of cone : "))
    height=eval(input("Enter the height of cone : "))
    print(f"\nProperties of cone are as follows:")
    print(f"Diameter : {radius*2}")
    slant_height=math.sqrt(math.pow(radius,2)+math.pow(height,2))
    print(f"Slant height : {slant_height}")
    print(f"Curved Surface Area : {math.pi*radius*slant_height}")
    print(f"Total Surface Area : {math.pi*radius*(slant_height+radius)}")
    print(f"Voume : {(math.pi*math.pow(radius,2)*height)/3}")
    return None

def cylinder():
    print(f"\nYou have selected Cylinder.")
    radius=eval(input("Enter the radius of cylinder : "))
    height=eval(input("Enter the height of cylinder : "))
    print(f"\nProperties of cylinder are as follows:")
    print(f"Diameter : {radius*2}")
    print(f"Curved Surface Area : {2*math.pi*radius*height}")
    print(f"Total Surface Area : {2*math.pi*radius*(height+radius)}")
    print(f"Voume : {math.pi*math.pow(radius,2)*height}")
    return None

def main():
    clearscreen()
    print("Welcome :)")
    print("This script will calculate different attributes of a desired geometrical figure.\n")
    print(f"{OR}NOTE: Calculated attributes are in same measurement units as entered input's measurement units.{NC}")
    figure=user_input()
    if figure=="Semicircle":
        semicircle()
    elif figure=="Circle":
        circle()
    elif figure=="Triangle":
        triangle()
    elif figure=="Square":
        square()
    elif figure=="Rectangle":
        rectangle()
    elif figure=="Hemisphere":
        hemisphere()
    elif figure=="Sphere":
        sphere()
    elif figure=="Cube":
        cube()
    elif figure=="Cuboid":
        cuboid()
    elif figure=="Cone":
        cone()
    else:
        cylinder()
    print(f"\nEnd Of Script :)")
    return None

if __name__=="__main__":
    main()
