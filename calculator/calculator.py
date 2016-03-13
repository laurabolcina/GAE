def calculate(no1, no2, operator):
    """Takes two numbers and an operator and executes operation."""

    if operator not in "+-*/":
        return "Operation is not supported."

    no1 = float(no1)
    no2 = float(no2)

    if operator == "+":
        result = no1 + no2
    elif operator == "-":
        result = no1 - no2
    elif operator == "*":
        result = no1 * no2
    elif operator == "/":
        result = no1 / no2

    return result