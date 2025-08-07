#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple Mathematical Calculator that perfroms Arithmetic Operations
We will be using Subtraction, Addition, Division, and Multiplications Operations,
"""

def add(*args):
    return sum(args)

def subtract(*args):
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    if not args:
        return None
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error: Division by zero!"
        result /= num
    return result


def calculator():
    print("Welcome to Simple Arithmetic Calculator")
    print("Choose your Operations: ")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter your choice (1/2/3/4): ")


    numbers = input("Enter numbers separated by space: ")
    numbers = list(map(float, numbers.split()))

    if choice == '1':
        print("Result:", add(*numbers))
    elif choice == '2':
        print("Result:", subtract(*numbers))
    elif choice == '3':
        print("Result:", multiply(*numbers))
    elif choice == '4':
        print("Result:", divide(*numbers))
    else:
        print("Invalid operation.")


calculator()
