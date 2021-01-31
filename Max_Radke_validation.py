# Name: Max Radke   Date: January 30, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 3
# Description: Takes an input and tells if it is a leap year
#
# How to run: Open the directory that this file is in with command prompt.
#             Type: "python -u Max_Radke_hw1.py". Follow instructions when running

import math

global Number # Input number variable (str)
global x # Input number variable (int)

while True: # Input validation
    print("Please enter a year to see if it is a leap year: ")
    Number = input()
    try:
        x = math.sqrt(int(Number)) # Make sure the year isn't negative and that it is a number
    except (ValueError, TypeError):
        print("Input error: make sure you are entering a single positive number and nothing else (ex. 2004)")
    else:
        x = int(Number)
        break

if x % 4 == 0: # Calculate if leap year
    if x % 100 == 0:
        if x % 400 == 0:
            print(Number + " is a leap year")
        else:
            print(Number + " is not a leap year")
    else:
        print(Number + " is a leap year")
else:
    print(Number + " is not a leap year")