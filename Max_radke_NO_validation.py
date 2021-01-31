# Name: Max Radke   Date: January 30, 2021
# College: Oregon State University
# Class: CS 362     Assignment: Homework 3
# Description: Takes an input and tells if it is a leap year
#
# How to run: Open the directory that this file is in with command prompt.
#             Type: "python -u Max_Radke_hw1.py". Follow instructions when running

global Number # Input number variable (str)
global x # Input number variable (int)

print("Enter a number to see if it is a leap year:")
Number = input()
x = int(Number)

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