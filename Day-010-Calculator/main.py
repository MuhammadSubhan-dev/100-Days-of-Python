import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Zero Error! Cannot divide by zero."

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    should_continue = True
    first_number = int(input("What's the first number? : "))
    while should_continue:
        print("+\n-\n*\n/")
        operation = input("What operation do you want to do? : ")
        second_number = int(input("What's the second number? : "))
        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")     #This just print whats being performed on data
        calculate_more = input(
            f"Type 'yes' to continue calculating with {result}, or type 'no' to start a new calculation: ")
        if calculate_more == "no":
            should_continue = False
            print("\n" * 20)
            calculator()
            return
        else:
            first_number = result

calculator()