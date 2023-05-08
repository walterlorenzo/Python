"""
Create a program that receives a number and prints its factorial.
"""
number = int(input("Enter a number: "))
if number > 0:
    factorial = 1
    for item in range(1, number + 1):
        factorial = factorial * item
    print(factorial)
