import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }


def calculator():
    print(art.logo)
    continue_calculating = True
    first_number = float(input("What is the first number?: "))
    while continue_calculating:
        operation = input("What operation would you like to perform? +, -, *, /: ")
        second_number = float(input("What is the next number?: "))
        answer = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = answer
        else:
            continue_calculating = False
            print("\n" * 20)
            calculator()


calculator()
