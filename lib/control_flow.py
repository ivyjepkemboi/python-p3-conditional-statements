#!/usr/bin/env python3

def admin_login(username, password):

    if username == "admin" and password == "12345":
        login = "Access granted"
        return login

    elif username == "ADMIN" and password == "12345":
        login = "Access granted"
        return login

    else: 
        login = "Access denied"
        return login
    

def hows_the_weather(temperature):
    if temperature < 40:
        message = "It's brisk out there!"
        return message

    elif temperature > 40 and temperature < 65:
        message = "It's a little chilly out there!"
        return message

    elif temperature > 85:
        message = "It's too dang hot out there!"
        return message
    
    else:
        message = "It's perfect out there!"
        return message

def fizzbuzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return ("FizzBuzz")
    
    elif num % 3 == 0:
        return ("Fizz")

    elif num % 5 == 0:
        return ("Buzz")

    else:
        return num


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2

    elif operation == "-":
        return num1-num2

    elif operation == "*":
        return num1*num2

    elif operation == "/":
        return num1/num2

    else:
        print ('Invalid operation!')
        return None
