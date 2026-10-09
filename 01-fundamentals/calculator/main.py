import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

math_functions = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def program():
    print(art.logo)
    print("Welcome to the Python Calculator!")
    repeat = True
    n1 = float(input("Type the first number: "))

    while repeat:
        for symbol in math_functions:
            print(symbol)
        operation = input("Type what operation you want to do: ")
        n2 = float(input("Type the second number: "))
        result = math_functions[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
        keep = input(f" Your result is : {result} to keep using"
                     f" this result for your next operation type y or n\n").lower()
        if keep == "y":
            n1 = result
        else:
            repeat = False
            print("\n * 20")
            program()
program()


