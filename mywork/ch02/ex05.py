#!/bin/python

'''
Ask the user to input multiple numbers on one input line.

Split the numbers into a list.

Write a loop that examines each element of the list and displays the ones that are greater than zero.
'''

numbers = input("Enter list of numbers with spacing: ")
format_numbers = numbers.split()

print("Numbers entered are:\n", format_numbers)

for i in format_numbers:
    i = int(i) #convert the numbers to integer
    if i > 0:
        print("Greater than zero: ", i)
