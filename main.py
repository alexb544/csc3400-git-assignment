import calculator

def main():
    while True:
        operation = int(input(
"""
What operation do you want to perform?
1: Add
2: Subtract
3: Multiply
4: Divide
5: Power
6: Square Root
7: Exit the program
>: """
        ))

        match operation:
            case 1:
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter a second number: "))
                print(calculator.add(num1, num2))
            case 2:
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter a second number: "))
                print(calculator.subtract(num1, num2))
            case 3:
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter a second number: "))
                print(calculator.multiply(num1, num2))
            case 4:
                num1 = int(input("Enter a number: "))
                num2 = int(input("Enter a second number: "))
                print(calculator.divide(num1, num2))
            case 5:
                num1 = int(input("Enter a number: "))
                pow = int(input("Enter what power you want: "))
                print(calculator.divide(num, pow))
            case 6:
                num = int(input("Enter a number: "))
                print(calculator.divide(num))
            case 7: 
                break


if __name__ == "__main__":
    main()
