#!/usr/bin/env python3

'''
Rewrite the preceding exercise to additionally print out how many digits are in the number, if the number is an integer.
'''

number = input("Please enter a number: ")

if number.isnumeric():
    print("Valid number and there are ", len(number), "digits")
else:
    print("invalid number")