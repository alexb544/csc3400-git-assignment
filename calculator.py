def add(num1, num2):
    try: 
        return float(num1) + float(num2)
    except ValueError: 
        print("Invalid input.")


def subtract(num1, num2):
    try: 
        return float(num1) - float(num2)
    except ValueError: 
        print("Invalid input.")


def multiply(num1, num2):
    try: 
        return float(num1) * float(num2)
    except ValueError: 
        print("Invalid input.")


def divide(num1, num2):
    try: 
        return float(num1) / float(num2)
    except ValueError: 
        print("Invalid input.")
    except ZeroDivisionError:
        print("Can't divide by zero.")


def power(num, pow):
    try: 
        return float(num) ** float(pow)
    except ValueError: 
        print("Invalid input.")


def square_root(num):
    try:
        num = float(num)
        if num < 0:
            raise ValueError("Negative number")
        return num ** 0.5
    except ValueError: 
        print("Invalid input.")