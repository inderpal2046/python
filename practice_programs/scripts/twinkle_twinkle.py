###############################################################################
# File          : twinkle_twinkle.py
# Author        : Inderpal Singh Saini <inderpal2406@gmail.com>
# Created       : 28 May, 2020
# Updated       : 28 May, 2020
# Description   : A platform independent script to display twinkle twinkle little star in specific format. 
################################################################################

# import modules
import os
import platform

def clear_screen():
    OS=platform.system()
    if OS=="Linux":
        os.system("clear")
    else:
        os.system("cls")
    return None

def main():
    clear_screen()
    print(f"Twinkle, twinkle little star,\n\tHow I wonder what you're!\n\t\tUp above the world so high,")
    print(f"\t\tLike a diamond in the sky.\nTwinkle, twinkle little star,\n\tHow I wonder what you're!")
    return None

if __name__=="__main__":
    main()
