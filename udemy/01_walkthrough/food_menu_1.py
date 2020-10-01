#!/usr/bin/env python3

# This script has food iems in a list
# User enters a food item of his choice
# The script then gives an answer if food item is present in list or not

import os
os.system("clear")

food_items=["Burger","Pizza","French Fries","Ice-cream"]

print(f"Welcome to our food bazaar :)")
print()
input_food_item=input("Enter the food item name which you want to order : ")
if bool(food_items.count(input_food_item)):
    print(f"Bravo! We have {input_food_item} in our kitchen. We'll deliver it in few minutes :)")
else:
    print(f"Alas! We don't have {input_food_item} in our kitchen. Please visit again next time :(")
