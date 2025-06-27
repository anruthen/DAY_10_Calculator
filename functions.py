def add(number1, number2):
    return number1 + number2
def sub(number1, number2):
    return number1 - number2
def mul(number1, number2):
    return number1 * number2
def div(number1, number2):
    return number1 / number2

mathematical_operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
def calculate(n1):
    for symbol in mathematical_operations:
        print(symbol)
    operator = input("Pick an operation: ")
    n2 = float(input("Enter the next number: "))
    result = mathematical_operations[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")
    yes_no = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    again = yes_no == "y"
    #alternative 1
    # again = True if yes_no == "y" else False
    #alternative 2
    # if yes_no == "y":
    #     again = True
    # else:
    #     again = False
    return result, again
