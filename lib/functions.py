#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

#!/usr/bin/env python3

def greet(name="programmer"):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet()  # This will print "Hello, programmer!"
    greet("Guido")  # This will print "Hello, Guido!"
    greet_with_default()  # This will print "Hello, programmer!"
    greet_with_default("Guido")  # This will print "Hello, Guido!"

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2
