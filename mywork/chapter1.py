#!/usr/bin/python3


"""
Exercise 1
Write a program that prompts for a lucky number. 
The program should print out a message if the number entered is not an integer.
"""

# prompt for integer number input
num = input("Please enter number: ")

# print msg if number is not an integer
if num.isnumeric():
    print("Number is ", num)
else:
    print("Invalid number")