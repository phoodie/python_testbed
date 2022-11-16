#!/usr/bin/env python3

'''
Write a program that prompts for a lucky number. The program should print out a message if the number entered is not an integer.
'''

number = input("Please enter a number: ")

if number.isnumeric():
    print("Valid number")
else:
    print("invalid number")