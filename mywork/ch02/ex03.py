#!/bin/python

'''
Write a program that prompts twice for an integer.
The program should print the larger of the two numbers.
If the numbers are equal, then the program should indicate it as such.
'''

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

bigger_text = "is bigger than"

if num_1 > num_2:
    print(num_1, bigger_text, num_2)
elif num_1 == num_2:
    print("Both ", num_1, "and", num_2, "are the same")
else:
    print(num_2, bigger_text, num_1)