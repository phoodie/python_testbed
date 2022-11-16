#!/bin/python

'''
Ask the user to input three numbers representing a lower limit, a higher limit, and a step value.

The program should use a range object to loop through and print the numbers from low to high (inclusive), taking into consideration the step.
'''

high_num = int(input("Please enter highest number: "))
low_num = int(input("Please enter lowest number: "))
step_num = int(input("Please enter step number: "))

for i in range(low_num + 1, high_num, step_num):
    print(i)