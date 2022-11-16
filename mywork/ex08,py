#!/bin/python

'''
Write a program that prompts twice for an integer.

The program should output the sum of the integers within the range of those two numbers inclusively.

For example, if the user inputs the numbers 10 and 15, then the sum would be 75.

10 + 11 + 12 + 13 + 14 + 15 = 75
'''

num1 = int(input("Enter number "))
num2 = int(input("Enter second number "))

if num1 > num2:
    num1, num2 = num2, num1 #swap variable values

total = 0
for value in range(num1, num2 + 1): # had to + 1 cause it starts at 0
    print("total current: ", total, "+ value current", value)
    total += value
    

print("total =", total)