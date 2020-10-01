#!/usr/bin/env python3

# This script performs same function as food_menu_1.py, but with a different logic.

import os
os.system("clear")

food_items=["Burger","Pizza","French Fries","Ice-cream"]

print(f"Welcome to our food bazaar :)")
print()
input_food_item=input("Enter the food item name which you want to order : ")
if input_food_item in food_items:
    print(f"Bravo! We have {input_food_item} in our kitchen. We'll deliver it in few minutes :)")
else:
    print(f"Alas! We don't have {input_food_item} in our kitchen. Please visit again next time :(")
