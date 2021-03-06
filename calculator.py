from math import sqrt

print("Dors Calculator")
print("Type 'exit' or press Control-C to quit.")
print("\n")

running = True

class EquationError(Exception):
    pass

def get_equation_parts(array):
    global number_1
    global number_2
    global operator

    if len(array) == 1:
        operator = array[0]
    elif len(array) == 2:
        operator = array[0]
        number_1 = float(array[1])
    elif len(array) == 3:
        operator = array[1]
        number_1 = float(array[0])
        number_2 = float(array[2])
    else:
        raise EquationError

def process_equation():
    equation = input("Enter an equation: ")
    equation_parts = equation.split(" ")
    return equation_parts

def calc():
    global running
    try:
        get_equation_parts(process_equation())
        if operator == "+":
            answer = number_1 + number_2
        if operator == "-":
            answer = number_1 - number_2
        if operator == "*":
            answer = number_1 * number_2
        if operator == "/":
            answer = number_1 / number_2
        if operator == "^":
            answer = number_1 ** number_2
        if operator.lower() == "sqrt":
            answer = sqrt(number_1)
        if operator.lower() == "mod":
            answer = number_1 % number_2
        if operator.lower() == "exit":
            running = False

        return answer

    except KeyboardInterrupt:
        running = False

    except:
        print("Invalid equation.")

if __name__ == "__main__":
    while running == True:
        calc()
