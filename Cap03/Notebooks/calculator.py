# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:16:09 2020

@author: Gabriela

Calculator
"""

print('Calculator')
print('Menu')
print('1 - Addition')
print('2 - Subtraction')
print('3 - Multiplication')
print('4 - Division')

opt = int(input('Enter the desired option: '))

if opt == 1:
    num1 = int(input('Insert a number: '))
    num2 = int(input('Insert another one: '))
    print(num1, '+', num2, '=', num1+num2)
elif opt == 2:
    num1 = int(input('Insert a number: '))
    num2 = int(input('Insert another one: '))
    print(num1, '-', num2, '=', num1-num2)
elif opt == 3:
    num1 = int(input('Insert a number: '))
    num2 = int(input('Insert another one: '))
    print(num1, '*', num2, '=', num1*num2)
elif opt == 4:
    num1 = int(input('Insert a number: '))
    num2 = int(input('Insert another one: '))
    print(num1, '/', num2, '=', num1/num2)
else:
    print('Enter a valid option.')