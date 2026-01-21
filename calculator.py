def addition(num1, num2):
    try: 
        return float(num1) + float(num2)
    except ValueError: 
        print("Invalid input.")


def subtraction(num1, num2):
    try: 
        return float(num1) - float(num2)
    except ValueError: 
        print("Invalid input.")


def multiplication(num1, num2):
    try: 
        return float(num1) * float(num2)
    except ValueError: 
        print("Invalid input.")


def division(num1, num2):
    try: 
        return float(num1) / float(num2)
    except ValueError: 
        print("Invalid input.")
    except ZeroDivisionError:
        print("Can't divide by zero.")


def power_of(num, pow):
    try: 
        return float(num) ** float(pow)
    except ValueError: 
        print("Invalid input.")


def sqrt_root(num):
    try:
        num = float(num)
        if num < 0:
            raise ValueError("Negative number")
        return num ** 0.5
    except ValueError: 
        print("Invalid input.")