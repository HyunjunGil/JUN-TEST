import time


class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def add():
        print("Please first number : ")
        a = input()
        print("Please second number : ")
        b = input()
        print(f"Result of addition is {float(a) + float(b)}!")

    @staticmethod
    def sub(a: int | float, b: int | float):
        print("Please first number : ")
        a = input()
        print("Please second number : ")
        b = input()
        print(f"Result of substraction is {float(a) - float(b)}!")

    @staticmethod
    def mul(a: int | float, b: int | float):
        print("Please first number : ")
        a = input()
        print("Please second number : ")
        b = input()
        print(f"Result of substraction is {float(a) - float(b)}!")

    @staticmethod
    def div(a: int | float, b: int | float):
        print("Please first number : ")
        a = input()
        print("Please second number : ")
        b = input()
        print(f"Result of substraction is {float(a) - float(b)}!")

    @staticmethod
    def print_option():
        print("Choose Option")
        print("(1) ADDITION")
        print("(2) SUBSTRACTION")
        print("(Q) Quit")


def main():

    while True:
        print("------- HYUNJUN'S AMAZING CALCULATOR -------")
        Calculator.print_option()
        a = input()
        if a == "1":
            Calculator.add()
        elif a == "2":
            Calculator.sub()
        elif a == "q" or "Q":
            break
        else:
            print("Invalid input! Please try again")
        time.sleep(1)

    print("Have a nice Day!")


if __name__ == "__main__":
    main()
